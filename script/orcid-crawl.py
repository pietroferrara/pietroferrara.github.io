#########################################################################################
#                                                                                       #
# Script to auto-update publications, people, and news for the ssv website.             #
# This script pulls data from ORCID using their public APIs. To use them, it            #
# is necessary to define an application that can interact with the APIs.                #
#                                                                                       #
# Follow the insructions at https://info.orcid.org/documentation/features/public-api/   #
# to generate an application, and retrieve its ID and SECRET.                           #
#                                                                                       #
# The, use the following command to generate a token for using the API:                 popul
# curl -i -L -H 'Accept: application/json' -d 'client_id=[APP ID]' -d 'client_secret=[APP SECRET]' -d 'scope=/read-public' -d 'grant_type=client_credentials' 'https://orcid.org/oauth/token'
#                                                                                       #
# The response will have the following structure:                                       #
# {                                                                                     #
#   "access_token": "[ACCESS_TOKEN]",                                                   #
#   "token_type": "bearer",                                                             #
#   "refresh_token": "[REFRESH_TOKEN]",                                                 #
#   "expires_in": [EXPIRATION],                                                         #
#   "scope": "/read-public",                                                            #
#   "orcid":null                                                                        #
# }                                                                                     #
# Note that the access token lasts ~20 years.                                           #
#                                                                                       #
# You can then use the generated access token as argument for this script:              #
# python3 orcid-crawl.py [ACCESS_TOKEN]                                                 #
#                                                                                       #
# The script will use such token to issue requests to the ORCID web API:                #
# https://github.com/ORCID/ORCID-Source/tree/main/orcid-api-web                         #
#                                                                                       #
# This script works by taking information out of the 'users.yaml' file located          #
# in the same directory. Such a file should be split in two sections, each              #
# containing a list of user information with <orcid, photo, from, to, student> where    #
# - <orcid> is the user's identifiaction number on ORCID                                #
# - <photo> is the filename of the image living under website_root/images/ to           #
#   use as profile picture for them                                                     #
# - <from> is the date (YYYY-MM-DD) when they joined the lab, used to filter out        #
#   publications published before they joined                                           #
# - <to> is the date (YYYY-MM-DD) when they left the lab, used to filter out            #
#   publications published after they joined (if they are still part of the lab,        #
#   'today' can be used)                                                                #
# - <student> is either 'yes' or 'no' and forces the role to PhD student                #
#                                                                                       #
# An example file is:                                                                   #
# users:                                                                                #
#   - id: 0000-0000-0000-0000                                                           #
#     photo: img1.png                                                                   #
#     from: 2019-01-01                                                                  #
#     to: today                                                                         #
#     student: no                                                                       #
#   - id: 0000-0000-0000-0001                                                           #
#     photo: img2.png                                                                   #
#     from: 2019-09-15                                                                  #
#     to: today                                                                         #
#     student: yes                                                                      #
# past_users:                                                                           #
#   - id: 0000-0000-0000-0002                                                           #
#     photo: img3.png                                                                   #
#     from: 2019-09-01                                                                  #
#     to: 2021-09-30                                                                    #
#     student: no                                                                       #
# external_users:                                                                       #
#   - id: 0000-0000-0000-0003                                                           #
#     photo: img4.png                                                                   #
#     from: 2019-09-01                                                                  #
#     to: 2021-09-30                                                                    #
#     student: no                                                                       #
#                                                                                       #
# The script then will:                                                                 #
# - fill up '../people.md' with the info crawled for each entry in 'users',             #
#   'past_users' and 'external_users', placing them in their respective sections        #
# - fill up '../publications.md' with works from both present and past users that       #
#   were published within the time window of at least one of the autors (to avoid       #
#   duplicates, we discriminate publications based on DOI)                              #
# - generate a news page under '../news/_posts/' named after the publication date       #
#   and the hash of the publication's title, containing a brief text to illustrate      #
#   what was published                                                                  #
# - generate the includes/index_people.html page with the updated photos of all         #
#   and external members, but not the past ones                                         #
#                                                                                       #
#########################################################################################

import requests
import json
import yaml
import sys
from datetime import *
import hashlib
import os
import shutil

class User:
	def __init__(self, name, surname, photo, mail, website, role, org, bio, raw_works):
		self.name = name.title() if name is not None else None
		self.surname = surname.title() if surname is not None else None
		self.photo = photo
		self.mail = mail
		self.website = website
		self.role = role.title() if role is not None else None
		self.org = org.title() if org is not None else None
		self.bio = bio
		self.raw_works = raw_works

	def has_necessary_fields(self):
		return self.name is not None and self.surname is not None and self.photo is not None

	def dump(self):
		position = f'{self.role} @ {self.org}' if self.role is not None and self.org is not None else ''
		email = f'Email: <a href="mailto:{self.mail}">{self.mail}</a><br/>' if self.mail is not None else ''
		website = f'Website: <a href="{self.website}">{self.website}</a>' if self.website is not None else ''
		bio = f'{self.bio}' if self.bio is not None else ''
		return f'''
<div class="div-person-table">
	<div class="div-person-table">
		<div class="div-person-table-col">
			<img src="{{{{ site.baseurl }}}}/images/{self.photo}"/>
		</div>
		<div class="div-person-table-multicol">
			<h3>{self.name} {self.surname}</h3>
			<h5>{position}</h5>
			{email}
			{website}
		</div>
	</div>
</div>
{bio}
<br/><br/>
'''

class Pub:
	def __init__(self, title, pub_date, pub_type, where, doi, url, contribs):
		self.title = title
		self.pub_date = pub_date
		self.pub_type = pub_type
		self.where = where
		self.doi = doi
		self.url = url
		self.contribs = contribs

	def is_out_of_date_period(self):
		return self.pub_date is None

	def has_necessary_fields(self):
		return self.title is not None

	def readable_kind(self):
		if self.pub_type is None:
			return 'article'
		r = self.pub_type.lower().replace('_', ' ').replace('-', ' ')
		if r == 'book':
			r = 'book chapter'
		elif r == 'other':
			r = 'article'
		return r

	def dump(self):
		authors = ', '.join(self.contribs) if self.contribs is not None and len(self.contribs) > 0 else 'Missing authors'
		venue = f' in {self.where}' if self.where is not None else ''
		doi = f' [[DOI]](https://doi.org/{self.doi})' if self.doi is not None else ''
		url = f' [[LINK]]({self.url})' if self.url is not None else ''
		return f'{authors}: _"{self.title}"_,{venue}{doi}{url}\n\n'

	def to_news_page(self):
		authors = ', '.join(self.contribs) if self.contribs is not None and len(self.contribs) > 0 else 'missing authors'
		kind = self.readable_kind()
		starting_kind = kind.capitalize()
		venue = f' in "{self.where}"' if self.where is not None else ''
		avail = f' Available [here](https://doi.org/{self.doi}).' if self.doi is not None else (f' Available [here]({self.url}).' if self.url is not None else '')
		return f'''---
layout: page
title: '{starting_kind} published{venue}!'
---

<small>{{{{ page.date | date: "%-d %B %Y" }}}}</small>

The {kind} "{self.title}", by {authors}, has just been published{venue}!{avail}
'''

def log(*messages):
	if verbose:
		print(*messages)

def query_api(access_token, user_id, method, do_log=False):
	return query_path(access_token, '/' + user_id + '/' + method, do_log)

def query_path(access_token, path, do_log=False):
	headers_dict = {
		'Accept': 'application/vnd.orcid+json',
		'Authorization':'Bearer ' + access_token
	}
	response = requests.get('https://pub.orcid.org/v3.0' + path, headers=headers_dict)
	if do_log:
		log('## Result of querying', path, '##')
		log(response.text)
	return json.loads(response.text)

def access_field(accessor, element, field, default=None, do_log=True):
	try:
		el = accessor(element)
		if do_log:
			log('\t' + field + ':', el)
		return el
	except Exception as e:
		log('\tUnable to retrieve value for', field, ', will use default value', default, '. Reason:', str(e))
		return default

def parse_user(access_token, user):
	user_id = user['id']
	log('Processing', user_id)

	record = query_api(access_token, user_id, 'person')
	name = access_field(lambda r: r['name']['given-names']['value'], record, 'name')
	surname = access_field(lambda r: r['name']['family-name']['value'], record, 'surname')
	bio = access_field(lambda r: r['biography']['content'], record, 'bio')
	mail = access_field(lambda r: r['emails']['email'][0]['email'], record, 'mail')
	website = access_field(lambda r: r['researcher-urls']['researcher-url'][0]['url']['value'], record, 'website')

	record = query_api(access_token, user_id, 'activities')

	if user['student']:
		log('\tForcing role to PhD Student')
		role = 'PhD Student'
		org = 'Università Ca\' Foscari Venezia'
	else:
		role = access_field(lambda r: r['employments']['affiliation-group'][0]['summaries'][0]['employment-summary']['role-title'], record, 'role')
		org = access_field(lambda r: r['employments']['affiliation-group'][0]['summaries'][0]['employment-summary']['organization']['name'], record, 'org')

	raw_works = access_field(lambda r: r['works']['group'], record, 'works', default=list(), do_log=False)
	return User(name, surname, user['photo'], mail, website, role, org, bio, raw_works)

def parse_work(access_token, min_date, max_date, work):
	workrecord = query_path(access_token, access_field(lambda r: r['work-summary'][0]['path'], work, 'work path', do_log=False), do_log=False)
	title = access_field(lambda r: r['title']['title']['value'], workrecord, 'title', do_log=False)
	log('Processing', title)

	creation_raw = access_field(lambda r: r['created-date']['value'], workrecord, 'creation')
	year_raw = access_field(lambda r: r['publication-date']['year']['value'], workrecord, 'year')
	month_raw = access_field(lambda r: r['publication-date']['month']['value'], workrecord, 'month')
	day_raw = access_field(lambda r: r['publication-date']['day']['value'], workrecord, 'day')

	year = int(year_raw) if year_raw is not None else None
	month = int(month_raw) if month_raw is not None else 1
	day = int(day_raw) if day_raw is not None else 1

	if year is not None:
		pub_date = date(year, month, day)
		if pub_date < min_date or pub_date > max_date:
			# exclude the publication
			return Pub(None, None, None, None, None, None, None)
	elif creation_raw is not None:
		log('\tMissing date, using creation timestamp instead')
		# according to the docs, creation_raw should contain a formatted ISO timestamp
		# but it seems that it instead contains the milliseconds relative to EPOCH.
		# should this stop working, we need to investigate a new workaround
		pub_date = date(1970, 1, 1) + timedelta(milliseconds=creation_raw)
		log('\t\tProduced date: ' + str(date))
	else:
		# exclude the publication
		return Pub(None, None, None, None, None, None, None)

	pub_type = access_field(lambda r: r['type'], workrecord, 'type')
	where = access_field(lambda r: r['journal-title']['value'], workrecord, 'venue')
	if where is not None:
		where = where.replace("'", "")
	url = access_field(lambda r: r['url']['value'], workrecord, 'url')
	doi = None
	extids = access_field(lambda r: r['external-ids']['external-id'], workrecord, 'external ids', default=list(), do_log=False)
	if extids is not None:
		for extid in extids:
			if access_field(lambda r: r['external-id-type'], extid, 'external id type', do_log=False) == 'doi':
				doi = access_field(lambda r: r['external-id-value'], extid, 'external id')
				break
	contribs = list()
	for contributor in access_field(lambda r: r['contributors']['contributor'], workrecord, 'contributors', default=list(), do_log=False):
		contribs += [access_field(lambda r: r['credit-name']['value'], contributor, 'contributor name')]
	return Pub(title, pub_date, pub_type, where, doi, url, contribs)

def add_news(publication):
	name_hash = hashlib.md5(publication.title.encode('utf-8')).hexdigest()
	news_name = f'{publication.pub_date.year}-{publication.pub_date.month}-{publication.pub_date.day}-paper-{name_hash}'
	log('Generating news for', publication.title, '(', news_name, ')')
	with open(f'../news/_posts/{news_name}.md', 'w') as news:
		news.write(publication.to_news_page())

def populate_publications_page(publications):
	with open('../publications.md', 'w') as file:
		file.write('''---
layout: page
title: Publications
---
''')
		curryear = None
		for publication in publications:
			year = publication.pub_date.year
			if curryear is None:
				curryear = year
				file.write(f'## {curryear}\n\n')
			elif year != curryear:
				curryear = year
				file.write(f'## {curryear}\n\n')

			log('Adding', publication.title, 'to the Publications page')
			file.write(publication.dump())

def populate_people_page(people, past_people, external_people):
	with open('../people.md', 'w') as file:
		file.write('''---
layout: page
title: People
---
''')
		for person in people:
			log('Adding', person.name, person.surname, 'to the People page')
			file.write(person.dump())
		if len(external_people) > 0:
			file.write('## External members\n')
			for person in external_people:
				log('Adding', person.name, person.surname, 'to the People page')
				file.write(person.dump())
		if len(past_people) > 0:
			file.write('## Past members\n')
			for person in past_people:
				log('Adding', person.name, person.surname, 'to the People page')
				file.write(person.dump())

def process_user_and_add(user, people_list, publications_list):
	person = parse_user(access_token, user)
	if person.has_necessary_fields():
		people_list += [person]
	else:
		log('\tUser discarded due to missing fields')

	min_date = user['from']
	max_date = date.today() if user['to'] == 'today' else user['to']
	for work in person.raw_works:
		publication = parse_work(access_token, min_date, max_date, work)
		if publication.is_out_of_date_period():
			log('\tPublication discarded since it is outside of the specified date range')
			continue
		elif not publication.has_necessary_fields():
			log('\tPublication discarded due to missing fields')
			continue
		elif publication.doi is None or any(publication.doi == pub.doi for pub in publications_list):
			log('\tPublication discarded due to missing or duplicate doi')
			continue
		else:
			publications_list += [publication]

def populate_index_people(people, external_people):
	log('Populating ../_includes/index_people.html')
	with open('../_includes/index_people.html', 'w') as file:
		file.write('''<br/>
<h2>Who we are</h2>

<a href="{{ site.baseurl }}/people.html">More info »</a><br><br>

<div class="teambox-container">''')
		for person in people:
			file.write(f'''
	<div class="teambox-card-container teambox-card-width">
    	<img class="teambox-img" src="{{{{ site.baseurl }}}}/images/{person.photo}">
  	</div>''')
		for person in external_people:
			file.write(f'''
	<div class="teambox-card-container teambox-card-width">
    	<img class="teambox-img" src="{{{{ site.baseurl }}}}/images/{person.photo}">
  	</div>''')
		file.write('''
</div>

<div class="div-img-table">
  <div class="div-img-table-row">
    <img class="div-img-table-multicol" src="{{ site.baseurl }}/images/{{ site.groupphoto }}"/>
  </div>
</div>
''')

def sort_by_date(publication):
	return publication.pub_date

if __name__ == '__main__':
	access_token = sys.argv[1]
	global verbose
	verbose = False
	if len(sys.argv) > 2 and sys.argv[2] == 'verbose':
		verbose = True

	with open('users.yaml', 'r') as yamlfile:
		data = yaml.load(yamlfile, Loader=yaml.FullLoader)
	log('Configuration read successfully')

	people = list()
	past_people = list()
	external_people = list()
	publications = list()

	for user in data['users']:
		process_user_and_add(user, people, publications)

	if 'external_users' in data:
		for user in data['external_users']:
			process_user_and_add(user, external_people, publications)

	if 'past_users' in data:
		for user in data['past_users']:
			process_user_and_add(user, past_people, publications)

	publications = sorted(publications, key=sort_by_date)
	# populate_people_page(people, past_people, external_people)
	populate_publications_page(reversed(publications))
	# populate_index_people(people, external_people)

	# cleanup news folder
	# if os.path.exists('../news/_posts/'):
	# 	shutil.rmtree('../news/_posts/')
	# os.makedirs('../news/_posts/')

	# for publication in reversed(publications):
	#	add_news(publication)
