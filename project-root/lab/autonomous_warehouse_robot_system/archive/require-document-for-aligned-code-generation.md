To ensure AI can accurately generate the two projects (OOP and Feature-Isolated Modular Composition) according to the plan, it’s essential to prepare a set of clear, structured documents. These documents should define the project structure, features, dependencies, and specific file requirements to guide AI in generating code that aligns with the architecture and comparison criteria. Here’s a list of key documents to prepare:

---

### **1\. Project Overview Document**

* **Purpose**: Provides AI with a high-level understanding of the project’s purpose, key features, and the two architectural approaches.
* **Contents**:
  * **Project Description**: Brief overview of the Autonomous Warehouse Robot Control System, including key components (e.g., robots, sensors, tasks, central control).
  * **Architectures**: Description of both architectures (OOP and FIMC) and the intended structural and operational differences.
  * **Objectives**: Clear statement of the goals (e.g., modularity, cognitive simplicity, performance equivalence).

---

### **2\. Architecture Specifications Document**

* **Purpose**: Clearly distinguishes the structure and principles of OOP versus FIMC for AI to apply consistently across both projects.
* **Contents**:
  * **OOP Architecture**: Define the class hierarchy (e.g., `Robot` base class, `Sensor` base class, `Task` base class), use of inheritance, encapsulation, and specific design patterns (e.g., Observer, Factory, Singleton).
  * **FIMC Architecture**: Define the folder structure, module boundaries, dependency-driven composition, and restrictions (e.g., avoiding classes in favor of modules, dependency injection rather than inheritance).
  * **Code Generation Rules**:
    * For **OOP**: Emphasize the use of classes, inheritance hierarchies, and polymorphic interfaces.
    * For **FIMC**: Use module-based functions and minimal interfaces, prioritize dependency injection, and avoid centralized structures.

---

### **3\. Component Specifications Document**

* **Purpose**: Provides detailed specifications for each core component, including robots, sensors, tasks, and the central control unit.
* **Contents**:
  * **Robots**: Specifications for `PickingRobot`, `SortingRobot`, and `InspectionRobot`, detailing their core functionality, interactions, and differences in OOP vs. FIMC.
  * **Sensors**: Specifications for `ProximitySensor`, `WeightSensor`, and `CameraSensor`, detailing how they generate data and interact with robots and tasks.
  * **Tasks**: Specifications for tasks like `PickItemTask`, `SortItemTask`, and `AvoidObstacleTask`, including configuration, assignment, and completion logic.
  * **Central Control Unit**: Differences in the OOP implementation (e.g., Singleton pattern, centralized coordination) and the FIMC approach (modular and minimal centralized logic).

---

### **4\. Configuration and Event Handling Document**

* **Purpose**: Defines how configuration and event handling should be implemented in each architecture, ensuring consistent structure across the project.
* **Contents**:
  * **Static Configuration Files**: Define the contents and format of `robot_config.json`, `sensor_config.json`, and `task_config.json`.
  * **Configuration Loader**:
    * **OOP**: Specify the `ConfigLoader` class, its static methods, and centralized configuration management.
    * **FIMC**: Define `config_loader.py`, static retrieval methods, and the lack of centralized control.
  * **Event Handling**:
    * **OOP**: Describe decentralized event handling within class methods, with possible observer pattern usage.
    * **FIMC**: Specify the use of in-module event handling functions for isolated interactions (task completion, alerts).

---

### **5\. Error Handling and Testing Guidelines**

* **Purpose**: Provides guidelines for error handling in each architecture, along with initial test scenarios AI should implement for verifying each component’s functionality and independence.
* **Contents**:
  * **Error Handling**:
    * **OOP**: Define the `SafetyController` and decentralized error handling in each class, with a template for retry logic.
    * **FIMC**: Specify in-module error handling functions, using the minimal template to ensure independence and avoid central dependency.
  * **Resilience Testing Scenarios**:
    * Provide test scenarios for each component (e.g., sensor failure, task retry) to verify error handling works as intended in each architecture.

---

### **6\. Extensibility and Cognitive Load Document**

* **Purpose**: Guides AI in designing the project structure to support extensibility while tracking cognitive load (simplicity in understanding and adding new components).
* **Contents**:
  * **Component Addition Specifications**: Provide specifications for new components (e.g., `ScanningRobot`, `TemperatureSensor`, `InspectItemTask`) and the steps to integrate these into each architecture.
  * **Implementation Time**: Describe metrics for measuring the time required to add new components, focusing on simplicity and minimal interdependencies.

---

### **7\. Cross-Language Flexibility Guide**

* **Purpose**: Explains FIMC’s language-agnostic structure and includes guidelines for portability to other languages.
* **Contents**:
  * **Modular Design in FIMC**: Outline how FIMC’s module-based design with dependency injection can be adapted to other languages, unlike OOP’s class-based structures.
  * **Example Translation**: Provide an example of translating one module from Python to another language (e.g., JavaScript or Go) to illustrate the process.

---

### **Summary**

Together, these documents will ensure that AI has a precise, structured roadmap for generating the two projects according to your specifications. With each document focusing on a specific aspect of architecture, functionality, or project organization, you’ll achieve consistent, well-aligned outputs across both OOP and FIMC projects. This documentation will also set a foundation for measuring key metrics in modularity, cognitive load, scalability, and maintainability as specified in the plan.

