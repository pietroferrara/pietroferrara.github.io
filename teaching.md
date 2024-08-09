---
layout: page
title: Teaching
nav-include: true
nav-order: 4
---

In this page, you can find informations about:

- [courses I am teaching or I taught in the past](#courses)
- [bachelor and master theses](#theses)

<a name="courses"/>
## Courses

### Bachelor in Computer Science

**Object Oriented programming – Module 1** (from academic year 2020-21)

*Fall semester, 48 hours (~150 students, 2nd year)*

This course is one of the basic educational activities of the Bachelor course in Computer Science that enable the student to gain knowledge and understanding major programming paradigms and acquire the ability to design and implement software.
The aim of the course is to provide knowledge related to the object-oriented programming paradigm as well as specific knowledge of the Java language.

### Master in Computer Science

**Software Architecture** (from academic year 2022-23)

*Fall semester, 48 hours (~20 students, 1st year)*

The main goal of this course is to teach the fundamentals of software architectures (and in particular what aspects should be taken into account when evaluating what architecture to choose to develop a software system), and the most important architectural patterns that are nowadays adopted in modern software systems. The course covers software architecture characteristics (aka, non-functional requirements), monolithic architectures (layered, pipeline, and microkernel), and distributed architectures (service oriented, event-driven, microservices, and serverless).

### Bachelor in Digital Management

**Introduction to coding and data management – Module 2** (from academic year 2019-20)

*Spring semester, 4th period, 30 hours (~140 students, 1st year)*

The goal of this course is to teach students how to cleanse, process and visualize data. In particular, the students will learn how to use a programming language (Python) to read and write data from standard formats, process it to extract useful information (using Numpy and Pandas), and visualize and plot it in order to show and explain its content (using matplotlib and Seaborn).

### Others

**Technological and Digital Innovation for Cultural Organisations** (from academic year 2023-24)

*Fall semester, 22 hous (~40 students, first level master in Management of Cultural Assets and Activities)*

The main goal of this module is to introduce the students to the basic concepts of information
technology and computer science and to provide an overview of the main trending technologies for
cultural activities.

### Courses taught in the past

**Programming and laboratory – A-L 2** (academic year 2020-21 and 2021-22)

*Spring semester, 48 hours (~80 students, 1st year of the Bachelor in Computer Science)*

The goal of this course is to teach students how to devise algorithmic solutions to simple problems. The student will learn and understand the foundations of computer science for what concerns imperative languages and basic algorithms. Moreover, the student will understand problem solvability and the ability to select suitable methods for problem analysis and modeling

**Information systems for the arts** (academic year 2019-20)

*Spring semester, 4th period, 30 hours (~50 students, Master in Economics and Management of Arts and Cultural Activities)*

The course is intended to introduce the main IT technologies used in the management of cultural heritage. In particular, the course will introduce the basic concepts of computers (binary representation of data, architecture, algorithms), how data is structured in information systems (in particular in relational databases), and a concrete language (SQL) that allows to manage such systems.


<a name="theses"/>
## Theses and internships

[This document](https://docs.google.com/document/d/1WNGiEYMJ3bi17p7EzWkX9RVjFFmBqNtf3wpw9At6v6k) provides complete guidelines about bachelor and master thesis under my supervision. Note that I supervise around 30 bachelor theses, few master theses per year, and I am currently the main supervisor of 4 PhD student. Therefore, the time I can allocate to supervise bachelor theses is quite limited, and the guidelines provides you more details about that. Anyway, I *never* refuse to supervise bachelor or master theses that falls into my research and teaching interests.

A list of possible topics follows. Note that some topics might be performed in collaboration with enterprises (so as a stage that is almost mandatory for the bachelor in CS), while others cannot.

- [Event-driven architecture to manage IIoT data](#event) (with Zamperla and Secura Factors)
- [Debugging Python notebook processing data](#debugging) (no enterprise involved)
- [CyberSecurity of robotic systems](#cybersecurity)
- [Extensions of LiSA (Library for Static Analysis)](#extensions) (no enterprise involved)
- [... just propose your idea!](#propose)

If you might be interested in some of these projects, just book an half-an-hour slot of my calendar through [Calendly](https://calendly.com/pietro-ferrara/30min) to discuss it!


<a name="event"/>
### Event-driven architecture to manage IIoT data (with Zamperla and Secura Factors)

Industrial machines produce tons of data. In our particular case, machines (such as rollercosters) at amusements parks are equipped with hundreds of sensors. Those might give important insights to detect anomalies and predict faults. Therefore, collecting such data, moving it to a DB in the cloud and performing different types of (ML) analyses might have an important impact.
The goal of this project is to develop an event-driven architecture (based on RabbitMQ queues) in order to obtain a scalable IT system that download all the data from the different machines, and uploads it to a DB. This project is in collaboration with Zamperla and Secura Factors.


<a name="debugging"/>
### Debugging Python notebook processing data

Nowadays Python became one of the de-facto standard programming languages adopted to read, clean, process and visualize data. Data scientists are not usually expert developers, and they often have a statistical or economical background. Therefore, developing tools and approaches to help them to develop more effective and robust Python data processing scripts is an extremely challenging and interesting topic. Common libraries adopted in such context are numpy, pandas, matplotlib and seaborn. The second module of the course of the course “Introduction to Coding and Data Management” I teach in the bachelor in Digital Management (Moodle space of both modules) provides a reasonable introduction to this world.
The main goal of this project is to (i) explore how data scientists use Python, (ii) develop some analyses in LiSA to provide useful feedback to data scientists, (iii) plug these analysis in common user interfaces for data scientists (e.g., Anaconda notebook and PyCharm), and (iv) perform an experimental assessments of these analysis.
The topic is quite open to contributions by both bachelor students (interested in object-oriented programming and software engineering, especially for the parts about exploration and user interfaces) and master students (interested in the topics of the “Software correctness, security, and reliability” course, especially for the parts about analyses and their experimentation) in Computer Science.

External collaborations: Caterina Urban (INRIA Paris)


<a name="cybersecurity"/>
### CyberSecurity of robotic systems

In recent years, we observed a growth of cybersecurity threats, especially due to the ubiquitous of connected and autonomous devices commonly defined as Internet of Things (IoT) and Industrial IoT (IIoT). Considering the sensitive nature of this information there’s a widespread suspicion concerning the way in which these information flows into the infrastructures. Additionally, with the increase of smart cities and connected environments, this critically is going to enlarge.
To address those problems we can distinguish between two lines of research that we explore in parallel, either studying the security and hardening solutions for the devices or focusing on the communication infrastructures.
In this project, we focus on the data-centric analysis of the infrastructure. Its easy to understand the importance of supporting the key property of computer security: Confidentiality, Integrity, Authenticity, Non-reputation, Availability. However, since we are working with IoT devices the way in which these properties are enforced is not trivial. In fact, we need to consider the intrinsic limitations of the devices, either from the power consumption point of view and the actual computational power available. Additionally, since we want to design solutions that could be applied to a wider scope of devices and developers we need to provide mechanisms with a good tradeoff between security and usability.
This topic is quite wide and open to both bachelor and master students interested in cybersecurity, software engineering, robotic systems, and static analysis. In addition, we recently created Secura Factors, a Ca’ Foscari spin-off focused on the industrialization and commercialization of the results of this project.

Funding: RIR (Reti innovative regionali) VIR2EM project, StartCup Veneto 2020

<a name="extensions"/>
### Extensions of LiSA (Library for Static Analysis)

The Software and System Verification group at UniVE is currently developing LiSA, a Java library that aims to ease the creation and implementation of static analyzers based on the Abstract Interpretation theory. Such analyzer is designed to be easily extended to other domains, programming languages, and properties of interests. Therefore, I am highly interested in any thesis that is focused towards the formalization and implementation of novel extensions of such analyzer. Possible thesis topics range from developing a parser to translate a programming language (e.g., Java, Python or JavaScript) to LiSA Abstract Syntax Tree (suitable for a bachelor theses), to the formalization and/or implementation of well known complex domains (suitable for master theses – a prerequisite in this case would be to have attended the course on “Software correctness, security, and reliability“).

<a name="propose"/>
### ... propose your own idea!

I guess that since you have been studying Computer Science for many years by now you might be interested in developing an information system to support some activities (in which probably you are an expert, or at least a user). I am quite open to supervise also this type of thesis if it contains enough technical work and details that are deep and interesting for a bachelor or master thesis. Just let’s discuss the details and see if this is feasible!