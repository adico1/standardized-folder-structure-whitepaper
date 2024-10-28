## **FIMC Principles and Concepts Document**

### **Purpose**

The purpose of this document is to define the core principles behind **Feature-based, Dependency-driven Folder Structure with Modules and Composition (FIMC)** and to provide a detailed explanation of its design choices. FIMC is an architecture that emphasizes modularity, autonomy, and simplicity by structuring code around features, explicit dependency management, and modular composition over inheritance.

---

### **Contents**

#### **1\. Feature-Based Organization**

* **Concept**: FIMC organizes code around discrete, self-contained **features** rather than traditional technical layers, such as controllers, models, or services. Each feature includes all necessary code for a specific functionality or system component, treating it as an independent module.
* **Explanation**:
  * In FIMC, a feature is a high-level function or capability of the system. For example, in a warehouse robot system, `robots`, `sensors`, and `tasks` might each be a main feature.
  * Each feature is organized within its own folder, containing the logic, utilities, and dependencies necessary to operate independently from other features.
  * **Benefits**:
    * **Modularity**: By grouping all code related to a feature into one location, each feature becomes highly modular, making it easier to test, debug, and maintain.
    * **Self-Containment**: This reduces the reliance on global or cross-feature dependencies, allowing each feature to operate as a standalone component.
    * **Scalability**: Features can be added, modified, or removed without impacting other parts of the system, making the system highly adaptable to changes and new requirements.
  * **Example**:
    * A `robots` feature folder would contain all modules related to robot operations (e.g., `picking_robot.py`, `sorting_robot.py`) and would include a `shared` sub-folder if there are utilities specific to robot operations, like `robot_utils.py`.

#### **2\. Dependency Management**

* **Concept**: FIMC relies on **dependency injection** and **explicit dependency management** to avoid tight coupling between features. Each feature or module explicitly defines the dependencies it needs, reducing implicit dependencies and ensuring modular autonomy.
* **Explanation**:
  * **Dependency Injection**: Dependencies are passed into modules as parameters, allowing each module to use only what it needs without hard-coded, global references. This makes it possible to swap or mock dependencies easily, especially useful for testing.
  * **Explicit Dependencies**: Each feature specifies and manages its own dependencies, reducing cross-feature coupling and making it clear which modules rely on which functions or services.
  * **Minimized Cross-Feature Coupling**: Shared utilities are limited to standardized, stateless functions and configurations within a `common` or feature-specific `shared` folder.
* **Benefits**:
  * **Modular Autonomy**: Features operate independently, with minimal dependencies on other parts of the system, reducing the risk of cascading failures and enhancing fault tolerance.
  * **Testing Flexibility**: Dependency injection allows modules to be easily tested in isolation, using mock dependencies as needed to verify each module’s functionality.
  * **Code Readability and Clarity**: Explicit dependencies make each module’s requirements transparent, enhancing readability and reducing the potential for hidden dependencies.
* **Example**:
  * A `sensors` feature may include `proximity_sensor.py`, `weight_sensor.py`, and `camera_sensor.py`, each of which relies on specific utility functions from `sensor_utils.py` within the `sensors/shared` folder. These dependencies are imported directly or injected as needed.

#### **3\. Composition over Inheritance**

* **Concept**: FIMC achieves functionality and extensibility through **composition** rather than inheritance, relying on smaller, composable modules and functions.
* **Explanation**:
  * Instead of creating a complex hierarchy of base and derived classes, FIMC uses **modular components** that each serve a single purpose or encapsulate a small, focused set of functions.
  * **Composition** allows functionality to be assembled by combining modules, where each module or function performs a specific role. Modules interact through explicit calls or interfaces, reducing tight coupling.
* **Benefits**:
  * **Flexibility**: Since modules are not bound by rigid inheritance chains, they can be replaced, updated, or composed into new features without impacting existing code.
  * **Reduced Overhead**: Avoiding inheritance prevents issues like class hierarchies that are hard to maintain, simplifies dependency graphs, and reduces the complexity of understanding module interactions.
  * **Reusability**: Composable modules are reusable across different features, encouraging code reuse without dependency constraints.
* **Example**:
  * In a `control` feature, `control_center.py` can compose the functionality it needs by importing modules from `robots` and `tasks` instead of relying on a base `Robot` or `Task` class hierarchy.

#### **4\. Module-Based Approach**

* **Concept**: FIMC favors **modules** (self-contained scripts or files) and **pure functions** over classes, focusing on stateless, reusable components wherever possible.
* **Explanation**:
  * Each module represents a single unit of functionality within a feature. FIMC typically avoids encapsulating logic in classes; instead, it uses standalone scripts with functions that can be easily imported and composed within other modules.
  * **Stateless Functions**: Functions within modules are kept stateless when possible, reducing side effects and making functions easier to test and reuse.
* **Benefits**:
  * **Simplicity**: Without complex class structures, each module remains small, understandable, and easy to work with.
  * **Improved Testability**: Stateless functions and isolated modules make it easy to write tests and verify functionality without needing to mock class states.
  * **Reduced Cognitive Load**: Without the need to navigate complex class hierarchies, developers can quickly understand and modify each module as needed.
* **Example**:
  * A `picking_robot.py` module in the `robots` feature might contain specific functions for the robot’s picking behavior, while `robot_utils.py` in `shared` might contain reusable functions applicable to multiple types of robots.

#### **5\. Event-Driven Communication and Interface Use**

* **Concept**: FIMC facilitates **inter-module communication** using an **event-driven architecture** and **interface-driven interactions** rather than centralized control structures or inheritance.
* **Explanation**:
  * **Event-Driven Communication**: Modules interact by emitting or listening for events, which allows modules to respond to changes or actions in other parts of the system without direct dependencies. This enables real-time responsiveness and adaptability without coupling modules together.
  * **Interface-Driven Interactions**: Instead of inheriting from shared base classes, each module adheres to defined interfaces, which act as contracts between modules. This approach keeps modules loosely coupled while ensuring they interact in expected ways.
* **Benefits**:
  * **Loose Coupling**: Since modules interact through events or interfaces, they remain independent and replaceable without the risk of breaking functionality in other parts of the system.
  * **Real-Time Adaptability**: Event-driven communication allows modules to react dynamically to changes, ideal for scenarios like real-time data handling or dynamic task assignment.
  * **Scalable and Extensible**: Interfaces allow new modules to be added or existing ones to be updated without impacting the system’s overall structure.
* **Example**:
  * A `control_center.py` in the `control` feature could listen for task completion events from modules within the `tasks` feature, allowing it to reassign tasks without needing to interact directly with individual task modules.

---

### **Conclusion**

The principles behind FIMC—**Feature-Based Organization**, **Dependency Management**, **Composition over Inheritance**, **Module-Based Approach**, and **Event-Driven Communication and Interface Use**—combine to create an architecture that emphasizes **modularity, autonomy, and flexibility**. By organizing code around self-contained features and managing dependencies explicitly, FIMC achieves a highly adaptable structure that is straightforward to test, extend, and maintain.

FIMC’s use of composition over inheritance, modules instead of classes, and event-driven communication allows complex systems to be developed with minimal cross-feature dependencies and without the overhead of traditional OOP hierarchies. These principles make FIMC especially suited to applications requiring modular independence, high adaptability, and simplified dependency management.

