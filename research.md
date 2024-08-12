---
layout: page
title: Research
nav-include: true
nav-order: 3
---

My research interests are focused on *applying rigorous mathematical theories to enhance software's reliability, security, and performance using static analysis*. Abstract interpretation is a framework applied to develop sound static analyses proving properties on all possible program executions. However, approximation is necessary to achieve computability, and the analysis might produce false alarms. Finding a good balance between precision, efficiency, and soundness depends on specific applications, and it usually requires deep research investigation. I am particularly interested in new scenarios where static analysis might have a relevant impact, and I have focused my recent research activity on mobile and .NET software.

On this page, you can find an almost exhaustive list of projects I am currently involved in:

- [Static Analysis of Microservices](#static6)
- [Static Analysis of Robotic Systems](#static7)
- [Scalable and Innovative Software Architectures](#scalable)
- [LiSA: Library for Static Analysis](#lisa)
- [Security and reliability analysis of smart contracts](#security)
- [Static analysis of machine learning algorithms](#static) (completed)
- [Static security analysis of IoT systems](#static2) (completed)
- [Static taint analysis for privacy](#static3) (completed)
- [Static analysis of .NET programs](#static4) (completed)
- [Static Analysis of Android Automotive Applications](#static5) (completed)

For a comprehensive view of the Software and System Verification group's projects, please visit [this webpage](https://unive-ssv.github.io/projects.html).

*Keywords*: abstract interpretation, static analysis, mobile programs, software engineering, program verification, multithreading, security.


<a name="static6"/>
## Static Analysis of Microservices

Collaborators: Giacomo Zanatta, Teodors Lisovenko

Most software applications developed nowadays are distributed systems in which different [micro]services communicate through synchronous and asynchronous mechanisms. These applications are composed of programs developed in many programming languages and rely on many technologies. However, sound static analysis might be particularly promising in distributed architectures, where exhaustively (or even partially) testing such systems is often prohibitive. This project aims to formalize and implement sound static analysis techniques on these software architectures.


<a name="static7"/>
## Static Analysis of Robotic Systems

Collaborators: Gianluca Caiazza, Giacomo Zanatta, Giacomo Boldini, Ruffin White

Robotic systems are distributed systems where several nodes (aka, robots) communicate with each other through different mechanisms. Security of communication in a robotic network is crucial. If an external node communicates to other nodes without authorization, then the network's overall logical and physical safety might be compromised. We aim to apply sound static analysis techniques to infer access policies on real-world robotic systems based on ROS2.

<a name="scalable"/>
## Scalable and Innovative Software Architectures

Collaborators: Gianluca Caiazza

Software systems are composed of several independently deployed nodes offering different services. Robustness, scalability, and elasticity are just a few of the main properties that those systems are expected to achieve in real-world settings. The goal of this project is to investigate novel software architectures based on modern technologies, such as Docker, Kubernetes, and KEDA. The project is carried out together with industrial partners.


<a name="lisa"/>
## LiSA

Collaborators: Luca Negrini, Vincenzo Arceri, Agostino Cortesi

LiSA (Library for Static Analysis) aims to ease the creation and implementation of static analyzers based on the Abstract Interpretation theory. LiSA provides an analysis engine that works on a generic and extensible control flow graph representation of the program to analyze. You can find more information about LiSA in our [GitHub repository](https://github.com/lisa-analyzer/) and the corresponding [project website](https://lisa-analyzer.github.io/).

<a name="security"/>
## Security and reliability analysis of Smart Contracts

Collaborators: Vincenzo Arceri, Fabio Tagliaferro, Imran Alam, Agostino Cortesi

Blockchain and Smart Contracts are growing in popularity thanks to the hype surrounding them and the wide range of their applications, such as cryptocurrencies, digital securities, and identity management.
The possibility of implementing Smart Contract infrastructures using general-purpose programming languages has become widespread, such as in Cosmos or Hyperledger, where, for example, the Go language can be used to build blockchain applications within these frameworks.
Nevertheless, blockchain development was not a goal in the design of such languages: their use in such a context intrinsically inherits the well-known problems of general-purpose programming languages. Besides, new blockchain-related vulnerabilities arise in such a context: representatives are transaction ordering and timestamp manipulation.
The objective of this project is to identify and implement advanced and sophisticated program analysis approaches to enhance the quality of applications while remaining within the context of general-purpose programming languages.

<a name="static"/>
## Static Analysis of Machine Learning Algorithms

Collaborators: Stefano Calzavara, Claudio Lucchese

Machine learning has proved invaluable for various tasks, yet it also proved vulnerable to evasion attacks, i.e., maliciously crafted perturbations of input data designed to force mispredictions. In this project, we apply static analysis to verify the security of decision tree models against evasion attacks with respect to an expressive threat model, where an arbitrary imperative program can represent the attacker.

### Bibliography

- Stefano Calzavara, Pietro Ferrara, Claudio Lucchese: “Certifying Decision Trees Against Evasion Attacks by Program Analysis”, in Proceedings of ESORICS 2020 


<a name="static2"/>
## Static Security Analysis of IoT systems

Collaborators: Agostino Cortesi, Fausto Spoto (University of Verona, Italy), Amit Mandal (SRM University, Amaravati, India)

IoT systems usually comprise several software layers: the embedded software running on the physical device (aka thing), some edge application that locally manages a physical system composed of several things and is connected to the Internet, some cloud applications providing access to, and storing and visualizing data of the IoT system, and some mobile applications that allow a user to manage the system remotely. Since the overall system interacts with the physical world through sensors and actuators, it is essential to consider the overall system when looking for security vulnerabilities and leakages of sensitive information.

Existing static analysis techniques (particularly taint analysis) focus on single applications in such context. This project aims to extend such techniques to perform inter-program analyses that can detect vulnerabilities due to the interaction between different software layers.

### Bibliography
- Amit Kr Mandal, Pietro Ferrara, Yuliy Khlyebnikov, Agostino Cortesi, Fausto Spoto: “Cross-program taint analysis for IoT systems.”, in Proceedings of SAC 2020 
- Pietro Ferrara, Amit Kr Mandal, Agostino Cortesi, Fausto Spoto: “Cross-Programming Language Taint Analysis for the IoT Ecosystem.”, in ECEASST, Vol. 77 
- Amit Kr Mandal, Federica Panarotto, Agostino Cortesi, Pietro Ferrara, Fausto Spoto: “Static analysis of Android Auto infotainment and on-board diagnostics II apps.”, in Softw. Pract. Exp., Vol. 49 


<a name="static3"/>
## Static Taint Analysis for Privacy

Collaborators: Luca Olivieri, Fausto Spoto

Taint analysis has been successfully applied to detect injection vulnerabilities in Web applications. Such an approach consists of tracking if something tainted (e.g., user input) coming from a source reaches a sink (e.g., execution of a SQL query) without being sanitized (e.g., properly escaped). Static taint analysis has been proven to scale up to industrial programs. At the end of the analysis, one only gets if the tainted data might reach the sink, but not how (i.e., the flow from the source to the sink).

New privacy regulations (such as the EU GDPR) underlined the relevance of proper data treatment. In such a scenario, static analysis can be applied to track how much sensitive data is accessed, managed, and leaked. In particular, we worked on extending existing taint analysis techniques to detect leakages of sensitive data.

### Bibliography

- Pietro Ferrara, Luca Olivieri, Fausto Spoto: “BackFlow: Backward Context-Sensitive Flow Reconstruction of Taint Analysis Results.”, in Proceedings of VMCAI 2020 
- Pietro Ferrara, Fausto Spoto: “Static Analysis for GDPR Compliance.”, in Proceedings of ITASEC 2018 
- Pietro Ferrara, Luca Olivieri, Fausto Spoto: “Tailoring Taint Analysis to GDPR.”, in Proceedings of APF 2018 


<a name="static4"/>
## Static Analysis of .NET Programs

Collaborators: Fausto Spoto, Agostino Cortesi

During the last decade, several semantic static analyzers have been formalized, designed, implemented, and adopted to analyze industrial programs. While many targeted Java programs, only very few dealt with .NET programs. Therefore, we formalized a translation of .NET bytecode into Java bytecode for static analysis purposes. This approach has been implemented into the Julia static analyzer (a commercial analyzer for Java programs).

### Bibliography

- Pietro Ferrara, Agostino Cortesi, Fausto Spoto: “From CIL to Java bytecode: Semantics-based translation for static analysis leveraging.”, in Sci. Comput. Program., Vol. 191 
- Pietro Ferrara, Agostino Cortesi, Fausto Spoto: “CIL to Java-bytecode translation for static analysis leveraging.”, in Proceedings of FormaliSE@ICSE 2018 

<a name="static5"/>
## Static Analysis of Android Auto[motive] Applications

Collaborators: Amit Kr Mandal, Federica Panarotto, Agostino Cortesi, Fausto Spoto

Smartphone and automotive technologies are rapidly converging, letting drivers enjoy communication and infotainment facilities and monitor in-vehicle functionalities, via the On Board Diagnostics (OBD) technology. Among the various automotive apps available in play stores, Android Auto infotainment, and OBD-II apps are widely used and are the most popular choice for smartphone-to-car interaction. Automotive apps have the potential of turning cars into smartphones on wheels, but they can also be the gateway to attacks. This work defined a static analysis identifying potential security risks in Android infotainment and OBD-II apps. It identifies potential security threats and presents a static analyzer for such apps. It has been applied to most of the highly rated infotainment apps available in the Google Play store and on the available open-source OBD-II apps against a set of possible exposure scenarios. Results show that almost 60% of such apps are potentially vulnerable and that 25% pose security threats related to the execution of JavaScript. The analysis of the OBD-II apps shows the possibility of severe Controller Area Network (CAN) injections and privacy violations because of leaks of sensitive information.

### Bibliography

- Amit Kr Mandal, Federica Panarotto, Agostino Cortesi, Pietro Ferrara, Fausto Spoto: “Static analysis of Android Auto infotainment and on-board diagnostics II apps.”, in Softw. Pract. Exp., Vol. 49 
- Federica Panarotto, Agostino Cortesi, Pietro Ferrara, Amit Kr Mandal, Fausto Spoto: “Static Analysis of Android Apps Interaction with Automotive CAN.”, in Proceedings of SmartCom 2018 
- Amit Kr Mandal, Agostino Cortesi, Pietro Ferrara, Federica Panarotto, Fausto Spoto: “Vulnerability analysis of Android auto infotainment apps.”, in Proceedings of CF 2018