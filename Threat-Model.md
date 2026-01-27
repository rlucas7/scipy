# **Threat Model**

This document builds on the fundamentals of threat modeling.

Libraries are building blocks; their security impacts every application that uses them. 

Thinking like an attacker about your library is a critical step in providing a robust, trusted component to the ecosystem.

Please first read and review the related [NumPy docs](https://numpy.org/doc/stable/reference/security.html). 
The guidelines in that document apply to SciPy equally. 

### **Key Differences for Libraries**

* Consumers are Developers: Your users are other developers integrating your code. They rely on your library's integrity and correct behavior.  
* Integration Points are APIs: The primary interface for attack or misuse is often the public API.  
* Supply Chain Risk: We generally consider these risks as a higher priority than reported vulnerabilities and faced with both, respond accordingly. 
* Side Effects & Resource Usage: Unintended consequences or excessive resource consumption can impact host applications.

### **The STRIDE Threat Categorization**

We STRIDE, a widely adopted framework, to help identify common types of threats:

* **S**poofing: Impersonating someone or something else (e.g., faking identity). 
* **T**ampering: Modifying data or code (e.g., altering a file, changing network packets).  
* **R**epudiation: Denying an action that occurred (e.g., a user denies making a transaction).  
* **I**nformation Disclosure: Revealing sensitive data to unauthorized individuals (e.g., leaking PII, credentials).  
* **D**enial of Service: Preventing legitimate users from accessing a service or resource (e.g., crashing a server, exhausting resources).  
* **E**levation of Privilege: Gaining unauthorized access to higher-level permissions (e.g., a regular user becoming an administrator).

## **Threat Model**

### **1. Library Overview**

* Library Name: SciPy  
* Brief Description: W
  * A python library for scientific computing. SciPy provides algorithms for optimization, integration, interpolation, eigenvalue problems,
  * algebraic equations, differential equations, statistics and many other classes of problems. 

### **2. Scope**

What specific part of your library are you threat modeling today? (Focus on core functionality, new features, or critical interfaces).

* The code under the `scipy` directory in the repo is considered in scope as this code is part of the package which is released to PyPi. 
* The other top level files and directories are related to building and maintaining the repo, the exception being the `subprojects` directory
  which we use to include vendored subprojects source code, usually C, C++, or Cuda code. 

### **3. Conceptual System Diagram**

Visualize your library's interaction points (use [Mermaid](https://mermaid.live/) or a sketch on paper). This might include:

* Your Library's Core Logic: The main processing unit.  
* External Dependencies: These are mainly listed in the `pyproject.toml` file where they are separated out by develepment dependencies or not.
* Data Sources/Sinks: The primary input data comes from the calling process and we do not assume malicious input.  
* Trust Boundaries: Please follow the [NumPy docs](https://numpy.org/doc/stable/reference/security.html)

### **4. Identify Assets**

The valuable things we are trying to protect within the context of the SciPy library are primarily 
the numerical integrity and scientific validity of the scientific calculations. In particular we strive for:

* Integrity of Library Functions: Ensuring our functions behave as expected and don't produce incorrect/malicious output.
* Confidentiality of Processed Data: Our library is not assuming to preserve confidentially of data while the calculations are conducted.  
* Availability/Performance for Host Application: Ensuring SciPy doesn't cause crashes, resource exhaustion, or severe performance degradation in the consuming application.
  We primarily check this by the test harness runs and via the `benchmarks` top level directory which uses [airspeed velocity](https://github.com/airspeed-velocity/asv)
* Reputation: We strive to maintain trust and avoiding supply chain attacks.
* Security of Host Application: To prevent SciPy from being a vector for suuply chain attacks we have a isolated build and release system with a
  simplified build and release process and which a limited number of maintainers have direct access to. The simplicity is a design criteria,
  we believe that simple systems are the easiest to identify and mitigate in the (often stressful) event of a supply chain attack. The simplicity also
  allows the maintainer group to fix things faster which ultimately reduces the impact of the supply chain attack.

### **5. Identify Threats**

For an API change or a change to the build CI/CD system, please work through the STRIDE questions from the perspective of the library, the exercise of
doing so is helpful to think about the use of the function or class given the desirec signature. In particular we recommend to focus on the TRID portion
of STRIDE as these are most applicable given the assumptions in the [NumPy docs](https://numpy.org/doc/stable/reference/security.html). 


### **6. Mitigation/Countermeasures**

In the event that a maintainer identifies a vulnerability from an open PR we may flag the PR on private channels and determine the appropriate next steps.
This may result in closing the PR or other actions to be determined as needed. 

**Remember:** Your library is a trust anchor for many projects. By dedicating time to threat modeling, you enhance not just your own project's security, but the security of the entire open-source ecosystem.
