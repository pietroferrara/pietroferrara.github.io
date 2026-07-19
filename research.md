---
layout: page
title: Research
subtitle: Static analysis by abstract interpretation, from theory to practice
nav-include: true
nav-order: 3
---

My research interests are focused on *applying rigorous mathematical theories to enhance software's reliability, security, and performance using static analysis*. Abstract interpretation is a framework applied to develop sound static analyses proving properties on all possible program executions. However, approximation is necessary to achieve computability, and the analysis might produce false alarms. Finding a good balance between precision, efficiency, and soundness depends on specific applications, and it usually requires deep research investigation. I am particularly interested in new scenarios and practical applications where static analysis might have a relevant impact; right now, I am particularly keen to apply these theories to modern software architectures (e.g., microservices). In addition, I am interested in modern software architectures per se: their design, and their robustness, scalability, and elasticity in real-world industrial settings.

On this page, you can find an almost exhaustive list of projects I am currently involved in:

- [Static Analysis of Microservices](#static6)
- [Static Analysis of Robotic Systems](#static7)
- [Scalable and Innovative Software Architectures](#scalable)
- [LiSA: Library for Static Analysis](#lisa)
- [Security and reliability analysis of smart contracts](#security) (completed)
- [Static analysis of machine learning algorithms](#static) (completed)
- [Static security analysis of IoT systems](#static2) (completed)
- [Static taint analysis for privacy](#static3) (completed)
- [Static analysis of .NET programs](#static4) (completed)
- [Static Analysis of Android Automotive Applications](#static5) (completed)

For a comprehensive view of the Software and System Verification group's projects, please visit [this webpage](https://unive-ssv.github.io/projects.html).

*Keywords*: abstract interpretation, static analysis, software engineering, software architectures, program verification, microservices, security.

<a name="static6"></a>
## Static Analysis of Microservices

Collaborators: Giacomo Zanatta, Teodors Lisovenko

Most software applications developed nowadays are distributed systems in which different [micro]services communicate through synchronous and asynchronous mechanisms. These applications are composed of programs developed in many programming languages and rely on many technologies. However, sound static analysis might be particularly promising in distributed architectures, where exhaustively (or even partially) testing such systems is often prohibitive. This project aims to formalize and implement sound static analysis techniques on these software architectures.

### Bibliography

- Giacomo Zanatta, Pietro Ferrara, Teodors Lisovenko, Luca Negrini, Gianluca Caiazza, Ruffin White: "Sound Static Analysis for Microservices: Utopia? A preliminary experience with LiSA", in Proceedings of FTfJP 2024 [[DOI]](https://doi.org/10.1145/3678721.3686229)
- Pietro Ferrara: "[Micro]services: threat, challenge, or opportunity for sound static program analysis?", in Proceedings of Microservices 2023

<a name="static7"></a>
## Static Analysis of Robotic Systems

Collaborators: Gianluca Caiazza, Giacomo Zanatta, Giacomo Boldini, Ruffin White

Robotic systems are distributed systems where several nodes (aka, robots) communicate with each other through different mechanisms. Security of communication in a robotic network is crucial. If an external node communicates to other nodes without authorization, then the network's overall logical and physical safety might be compromised. We aim to apply sound static analysis techniques to infer access policies on real-world robotic systems based on ROS2. Our work on automating the extraction of ROS2 security policies was a finalist for the Best Safety, Security, and Rescue Robotics paper award at IROS 2024.

### Bibliography

- Giacomo Zanatta, Gianluca Caiazza, Pietro Ferrara, Luca Negrini, Ruffin White: "Automating ROS2 Security Policies Extraction through Static Analysis", in Proceedings of IROS 2024 [[DOI]](https://doi.org/10.1109/IROS58592.2024.10802507)
- Giacomo Zanatta, Gianluca Caiazza, Pietro Ferrara, Luca Negrini: "Inference of Access Policies through Static Analysis", in International Journal on Software Tools for Technology Transfer, 2024 [[DOI]](https://doi.org/10.1007/s10009-024-00777-8)

<a name="scalable"></a>
## Scalable and Innovative Software Architectures

Collaborators: Gianluca Caiazza

Software systems are composed of several independently deployed nodes offering different services. Robustness, scalability, and elasticity are just a few of the main properties that those systems are expected to achieve in real-world settings. The goal of this project is to investigate novel software architectures based on modern technologies, such as Docker, Kubernetes, and KEDA. The project is carried out together with industrial partners, in particular Zamperla and Galdi.

### Bibliography

- Gianluca Caiazza, Pietro Ferrara, Teodors Lisovenko, Marco Biondo, Davide Tosato: "CoreTrust: Ensuring Data Quality at the Edge", in Proceedings of ECSA 2026 — to appear
- Gianluca Caiazza, Teodors Lisovenko, Pietro Ferrara, Federico Berti, Fabio Ferrari, Alessandro Zaupa, Guowei Zhang: "From Legacy to Intelligent IIoT Systems: Automation, Scalability and Elasticity", in Proceedings of ICSA 2025 [[DOI]](https://doi.org/10.1109/ICSA65012.2025.00033)

<a name="lisa"></a>
## LiSA: Library for Static Analysis

Collaborators: Luca Negrini, Vincenzo Arceri, Agostino Cortesi

LiSA (Library for Static Analysis) aims to ease the creation and implementation of static analyzers based on the Abstract Interpretation theory. LiSA provides an analysis engine that works on a generic and extensible control flow graph representation of the program to analyze. In 2026, JLiSA (the Java frontend of LiSA) arrived 3rd in the Java track of [SV-COMP](https://sv-comp.sosy-lab.org/). You can find more information about LiSA in our [GitHub repository](https://github.com/lisa-analyzer/) and the corresponding [project website](https://lisa-analyzer.github.io/).

### Bibliography

- Giacomo Boldini, Luca Negrini, Luca Olivieri, Pietro Ferrara: "A Modular Framework for Stack-Heap and Value Abstractions", in Proceedings of SAS 2026 — to appear
- Vincenzo Arceri, Luca Negrini, Giacomo Zanatta, Filippo Bianchi, Teodors Lisovenko, Luca Olivieri, Pietro Ferrara: "JLiSA: The Java Frontend of the Library for Static Analysis (Competition Contribution)", in Proceedings of TACAS 2026 [[DOI]](https://doi.org/10.1007/978-3-032-22749-2_30)
- Luca Negrini, Vincenzo Arceri, Luca Olivieri, Agostino Cortesi, Pietro Ferrara: "Teaching through Practice: Advanced Static Analysis with LiSA", in Proceedings of FMTea 2024 [[DOI]](https://doi.org/10.1007/978-3-031-71379-8_3)
- Luca Negrini, Pietro Ferrara, Vincenzo Arceri, Agostino Cortesi: "LiSA: A Generic Framework for Multilanguage Static Analysis", in Intelligent Systems Reference Library, 2023 [[DOI]](https://doi.org/10.1007/978-981-19-9601-6_2)
- Pietro Ferrara, Luca Negrini, Vincenzo Arceri, Agostino Cortesi: "Static analysis for dummies: Experiencing LiSA", in Proceedings of SOAP 2021 [[DOI]](https://doi.org/10.1145/3460946.3464316)

<a name="security"></a>
## Security and reliability analysis of Smart Contracts (completed)

Collaborators: Luca Olivieri, Vincenzo Arceri, Agostino Cortesi

Blockchain and Smart Contracts are growing in popularity thanks to the hype surrounding them and the wide range of their applications, such as cryptocurrencies, digital securities, and identity management.
The possibility of implementing Smart Contract infrastructures using general-purpose programming languages has become widespread, such as in Cosmos or Hyperledger, where, for example, the Go language can be used to build blockchain applications within these frameworks.
Nevertheless, blockchain development was not a goal in the design of such languages: their use in such a context intrinsically inherits the well-known problems of general-purpose programming languages. Besides, new blockchain-related vulnerabilities arise in such a context: representatives are transaction ordering and timestamp manipulation.
The objective of this project was to identify and implement advanced and sophisticated program analysis approaches to enhance the quality of applications while remaining within the context of general-purpose programming languages. More recently, we have also been investigating the quality and security of smart contracts generated by large language models.

### Bibliography

- Luca Olivieri, Dennis Beste, Luca Negrini, Lea Schönherr, Antonio Emanuele Cinà, Pietro Ferrara: "Code Generation of Smart Contracts with LLMs: A Case Study on Hyperledger Fabric", in Proceedings of ISSRE 2025 [[DOI]](https://doi.org/10.1109/ISSRE66568.2025.00034)
- Luca Olivieri, Luca Pasetto, Luca Negrini, Pietro Ferrara: "An Overview of Termination in the Ethereum Blockchain", in Proceedings of BlockTEA 2025 [[DOI]](https://doi.org/10.1007/978-3-032-12335-0_14)
- Luca Olivieri, Luca Negrini, Vincenzo Arceri, Pietro Ferrara, Agostino Cortesi: "Detection of Read-Write Issues in Hyperledger Fabric Smart Contracts", in Proceedings of SAC 2025 [[DOI]](https://doi.org/10.1145/3672608.3707721)
- Luca Olivieri, Luca Negrini, Vincenzo Arceri, Pietro Ferrara, Agostino Cortesi, Fausto Spoto: "Static Detection of Untrusted Cross-Contract Invocations in Go Smart Contracts", in Proceedings of SAC 2025 [[DOI]](https://doi.org/10.1145/3672608.3707728)
- Luca Olivieri, Vincenzo Arceri, Badaruddin Chachar, Luca Negrini, Fabio Tagliaferro, Fausto Spoto, Pietro Ferrara, Agostino Cortesi: "General-Purpose Languages for Blockchain Smart Contracts Development: A Comprehensive Study", in IEEE Access, 2024 [[DOI]](https://doi.org/10.1109/ACCESS.2024.3495535)
- Luca Olivieri, Luca Negrini, Vincenzo Arceri, Badaruddin Chachar, Pietro Ferrara, Agostino Cortesi: "Detection of Phantom Reads in Hyperledger Fabric", in IEEE Access, 2024 [[DOI]](https://doi.org/10.1109/ACCESS.2024.3410019)
- Luca Olivieri, Vincenzo Arceri, Pietro Ferrara, Fausto Spoto, Luca Negrini, Fabio Tagliaferro, Agostino Cortesi: "Information Flow Analysis for Detecting Non-Determinism in Blockchain", in Proceedings of ECOOP 2023 [[DOI]](https://doi.org/10.4230/LIPIcs.ECOOP.2023.23)
- Luca Olivieri, Fabio Tagliaferro, Vincenzo Arceri, Marco Ruaro, Luca Negrini, Agostino Cortesi, Pietro Ferrara, Fausto Spoto, Enrico Talin: "Ensuring determinism in blockchain software with GoLiSA: an industrial experience report", in Proceedings of SOAP 2022 [[DOI]](https://doi.org/10.1145/3520313.3534658)

<a name="static"></a>
## Static Analysis of Machine Learning Algorithms (completed)

Collaborators: Stefano Calzavara, Claudio Lucchese

Machine learning has proved invaluable for various tasks, yet it also proved vulnerable to evasion attacks, i.e., maliciously crafted perturbations of input data designed to force mispredictions. In this project, we applied static analysis to verify the security of decision tree models against evasion attacks with respect to an expressive threat model, where an arbitrary imperative program can represent the attacker.

### Bibliography

- Stefano Calzavara, Pietro Ferrara, Claudio Lucchese: "Certifying machine learning models against evasion attacks by program analysis", in Journal of Computer Security, 2023 [[DOI]](https://doi.org/10.3233/JCS-210133)
- Stefano Calzavara, Pietro Ferrara, Claudio Lucchese: "Certifying Decision Trees Against Evasion Attacks by Program Analysis", in Proceedings of ESORICS 2020 [[DOI]](https://doi.org/10.1007/978-3-030-59013-0_21)

<a name="static2"></a>
## Static Security Analysis of IoT systems (completed)

Collaborators: Agostino Cortesi, Fausto Spoto (University of Verona, Italy), Amit Mandal (SRM University, Amaravati, India)

IoT systems usually comprise several software layers: the embedded software running on the physical device (aka thing), some edge application that locally manages a physical system composed of several things and is connected to the Internet, some cloud applications providing access to, and storing and visualizing data of the IoT system, and some mobile applications that allow a user to manage the system remotely. Since the overall system interacts with the physical world through sensors and actuators, it is essential to consider the overall system when looking for security vulnerabilities and leakages of sensitive information.

Existing static analysis techniques (particularly taint analysis) focus on single applications in such context. This project aimed to extend such techniques to perform inter-program analyses that can detect vulnerabilities due to the interaction between different software layers.

### Bibliography

- Pietro Ferrara, Amit Kr Mandal, Agostino Cortesi, Fausto Spoto: "Static Analysis for Discovering IoT Vulnerabilities", in International Journal on Software Tools for Technology Transfer, 2021 [[DOI]](https://doi.org/10.1007/s10009-020-00592-x)
- Amit Kr Mandal, Pietro Ferrara, Yuliy Khlyebnikov, Agostino Cortesi, Fausto Spoto: "Cross-program taint analysis for IoT systems", in Proceedings of SAC 2020 [[DOI]](https://doi.org/10.1145/3341105.3373924)
- Pietro Ferrara, Amit Kr Mandal, Agostino Cortesi, Fausto Spoto: "Cross-Programming Language Taint Analysis for the IoT Ecosystem", in ECEASST, Vol. 77, 2019

<a name="static3"></a>
## Static Taint Analysis for Privacy (completed)

Collaborators: Luca Olivieri, Fausto Spoto

Taint analysis has been successfully applied to detect injection vulnerabilities in Web applications. Such an approach consists of tracking if something tainted (e.g., user input) coming from a source reaches a sink (e.g., execution of a SQL query) without being sanitized (e.g., properly escaped). Static taint analysis has been proven to scale up to industrial programs. At the end of the analysis, one only gets if the tainted data might reach the sink, but not how (i.e., the flow from the source to the sink).

New privacy regulations (such as the EU GDPR) underlined the relevance of proper data treatment. In such a scenario, static analysis can be applied to track how much sensitive data is accessed, managed, and leaked. In particular, we worked on extending existing taint analysis techniques to detect leakages of sensitive data.

### Bibliography

- Pietro Ferrara, Luca Olivieri, Fausto Spoto: "Static Privacy Analysis by Flow Reconstruction of Tainted Data", in International Journal of Software Engineering and Knowledge Engineering, 2021 [[DOI]](https://doi.org/10.1142/S0218194021500303)
- Pietro Ferrara, Luca Olivieri, Fausto Spoto: "BackFlow: Backward Context-Sensitive Flow Reconstruction of Taint Analysis Results", in Proceedings of VMCAI 2020 [[DOI]](https://doi.org/10.1007/978-3-030-39322-9_2)
- Pietro Ferrara, Luca Olivieri, Fausto Spoto: "Tailoring Taint Analysis to GDPR", in Proceedings of APF 2018 [[DOI]](https://doi.org/10.1007/978-3-030-02547-2_4)
- Pietro Ferrara, Fausto Spoto: "Static Analysis for GDPR Compliance", in Proceedings of ITASEC 2018

<a name="static4"></a>
## Static Analysis of .NET Programs (completed)

Collaborators: Fausto Spoto, Agostino Cortesi

During the last decade, several semantic static analyzers have been formalized, designed, implemented, and adopted to analyze industrial programs. While many targeted Java programs, only very few dealt with .NET programs. Therefore, we formalized a translation of .NET bytecode into Java bytecode for static analysis purposes. This approach has been implemented into the Julia static analyzer (a commercial analyzer for Java programs).

### Bibliography

- Pietro Ferrara, Agostino Cortesi, Fausto Spoto: "From CIL to Java bytecode: Semantics-based translation for static analysis leveraging", in Science of Computer Programming, Vol. 191, 2020 [[DOI]](https://doi.org/10.1016/j.scico.2020.102392)
- Pietro Ferrara, Agostino Cortesi, Fausto Spoto: "CIL to Java-bytecode translation for static analysis leveraging", in Proceedings of FormaliSE 2018 [[DOI]](https://doi.org/10.1145/3193992.3193994)

<a name="static5"></a>
## Static Analysis of Android Auto[motive] Applications (completed)

Collaborators: Amit Kr Mandal, Federica Panarotto, Agostino Cortesi, Fausto Spoto

Smartphone and automotive technologies are rapidly converging, letting drivers enjoy communication and infotainment facilities and monitor in-vehicle functionalities, via the On Board Diagnostics (OBD) technology. Among the various automotive apps available in play stores, Android Auto infotainment, and OBD-II apps are widely used and are the most popular choice for smartphone-to-car interaction. Automotive apps have the potential of turning cars into smartphones on wheels, but they can also be the gateway to attacks. This work defined a static analysis identifying potential security risks in Android infotainment and OBD-II apps. It has been applied to most of the highly rated infotainment apps available in the Google Play store and on the available open-source OBD-II apps against a set of possible exposure scenarios. Results show that almost 60% of such apps are potentially vulnerable and that 25% pose security threats related to the execution of JavaScript.

### Bibliography

- Amit Kr Mandal, Federica Panarotto, Agostino Cortesi, Pietro Ferrara, Fausto Spoto: "Static analysis of Android Auto infotainment and on-board diagnostics II apps", in Software: Practice and Experience, Vol. 49, 2019 [[DOI]](https://doi.org/10.1002/spe.2698)
- Federica Panarotto, Agostino Cortesi, Pietro Ferrara, Amit Kr Mandal, Fausto Spoto: "Static Analysis of Android Apps Interaction with Automotive CAN", in Proceedings of SmartCom 2018 [[DOI]](https://doi.org/10.1007/978-3-030-05755-8_12)
- Amit Kr Mandal, Agostino Cortesi, Pietro Ferrara, Federica Panarotto, Fausto Spoto: "Vulnerability analysis of Android auto infotainment apps", in Proceedings of CF 2018 [[DOI]](https://doi.org/10.1145/3203217.3203278)

## Current funded projects

- **HEALTH-AI** (European Union, Erasmus+, 2025–2028): bridging the gap between healthcare and AI by equipping professionals and students with the knowledge, skills, and ethical awareness needed for safe and effective AI integration in clinical practice, through an Adaptive AI Curriculum, a co-creation platform for engineers and healthcare professionals, and the HealthAI Ethics Guideline.
- **SUPREME** (Regione Veneto, Reti Innovative Regionali, 2025–2026): human-centric Industry 5.0 systems to monitor and optimize industrial plants in terms of reliability, energy efficiency, and quality control.
- **SATCO** (Regione Veneto, Reti Innovative Regionali, 2025–2026): a constellation of satellites offering on-demand optical and laser signal intelligence services.
- **Digital platform 5.0 transformation** (SMACT Competence Center, 2025–2026, Principal Investigator): a scalable and elastic software architecture to collect and elaborate data coming from rollercoasters, in collaboration with Zamperla SPA.
- **EcoDigify** (European Union, Erasmus+, 2024–2027): a future-oriented interdisciplinary university program on sustainable digitalization.

## Completed funded projects

- **Static Analysis for Data Scientists** (Ca' Foscari University of Venice, SPIN project, 2021–2023, Principal Investigator): an effective tool based on static analysis to help data scientists develop Python scripts for data processing.
- **SERICS – Security and Rights in the Cyberspace** (Italian Ministry of University and Research, Partenariati Estesi, 2023–2025): methodologies to identify, detect, prevent, and fix security vulnerabilities in software (Spoke 6, Software and System Security).
- **iNEST – Interconnected Nord-Est Innovation Ecosystem** (Italian Ministry of University and Research, Ecosistemi dell'Innovazione, 2022–2025): specification and validation of functional and security requirements of robotic software (Spoke 3, task leader).
- **IAM access control policies verification and inference** (Amazon Research Awards, AWS Automated Reasoning, 2021–2022, Principal Investigator): abstract interpretation techniques to over-approximate the string values computed by applications using AWS cloud services, in order to infer and validate IAM access control policies.
