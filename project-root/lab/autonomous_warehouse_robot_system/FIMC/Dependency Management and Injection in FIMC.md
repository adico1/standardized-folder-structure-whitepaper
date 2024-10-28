# **Dependency Management and Injection in FIMC**

### **Purpose**

This document provides an in-depth look at **dependency management** in the **Feature-based, Dependency-driven Folder Structure with Modules and Composition (FIMC)**. Effective dependency management is central to FIMC’s goal of achieving modular autonomy, where each feature operates independently. The document covers FIMC’s use of **dependency injection** for flexible, context-specific dependencies, the distinction between **direct imports** and **injected dependencies**, and how FIMC uses **interfaces** and **contracts** to facilitate interactions between modules without inheritance.

---

## **Contents**

1. **Explicit Dependencies**: How dependency injection promotes modular independence by managing dependencies explicitly within each module.
2. **Direct Imports vs. Dependency Injection**: Guidelines for choosing between direct imports and dependency injection, depending on the nature of the dependency.
3. **Interfaces and Contracts**: Using interface-driven design to specify inter-module interactions without inheritance.
4. **Examples**: Practical examples illustrating dependency injection within features and the use of direct imports for shared utilities.

---

### **1\. Explicit Dependencies**

**Dependency injection** is a foundational principle in FIMC, used to maintain clear and explicit dependencies within each feature. Rather than relying on a global or shared state, FIMC requires each module to declare and receive its dependencies directly, creating a self-contained environment within each feature.

#### **Key Aspects of Dependency Injection in FIMC**

* **Autonomous Modules**: Each module specifies its dependencies through function parameters or module-level configurations, promoting autonomy and isolating feature-specific logic.
* **Flexibility and Substitutability**: Injected dependencies allow modules to adapt to different contexts (e.g., testing, production) by substituting dependencies without altering the module itself.
* **Reducing Global State**: FIMC minimizes reliance on global or shared state, preventing unintended dependencies and making the system more robust and modular.

#### **Example of Dependency Injection in FIMC**

In an autonomous warehouse system, a **robot feature** might need access to various **sensor modules** for detecting obstacles. Instead of the robot module directly importing or initializing sensor dependencies, FIMC uses dependency injection to explicitly pass these dependencies into the robot’s functions.

**robot\_control.py** (within the `robots` feature)

```
# robot_control.py

def initialize_robot(sensors, tasks):
    """
    Initialize the robot with specific sensor and task dependencies.
    """
    # Injected dependencies: sensors and tasks
    for sensor in sensors:
        sensor.activate()

    for task in tasks:
        task.assign_to_robot()
```

In this example, the `sensors` and `tasks` dependencies are injected into `initialize_robot`, allowing different implementations of sensors or tasks to be used. This approach supports modular testing, as mock sensors or tasks can be easily substituted.

---

### **2\. Direct Imports vs. Dependency Injection**

FIMC uses both **direct imports** and **dependency injection** based on the nature of the dependency. Understanding when to use each method is key to managing dependencies in a way that aligns with FIMC’s goals of modularity and flexibility.

#### **Direct Imports: When and Why**

Direct imports are suitable for **standardized, stateless utilities** that are consistent across modules. Using direct imports simplifies the codebase by reducing the need to inject dependencies that do not vary by context or environment. Direct imports improve readability and centralize commonly used functions or configurations.

##### **Example of Direct Imports**

A **logging utility** or **configuration loader** that doesn’t vary across environments can be placed in a `common` directory and imported directly into modules where needed.

**logging.py** (within `common` directory)

```
# logging.py

def log_event(event_type, message):
    print(f"{event_type}: {message}")
```

**robot\_control.py** (within `robots` feature)

```
from common.logging import log_event

def initialize_robot(sensors, tasks):
    log_event("INFO", "Initializing robot with given sensors and tasks.")
    # Additional initialization code
```

In this example, `log_event` is directly imported from the `common` directory. Since logging is a standardized utility, a direct import is efficient and maintains simplicity.

#### **Dependency Injection: When and Why**

Dependency injection is used for **configurable, context-sensitive components** that may vary based on the environment or specific module requirements. Injecting dependencies enables flexible configurations, substitutability, and easier testing, as modules can receive custom implementations or mock versions of dependencies.

##### **Example of Dependency Injection**

Consider a **database module** that interacts with various data sources. To support different environments (e.g., testing vs. production), FIMC can inject a `Database` instance configured for the specific context rather than relying on direct imports.

**sensor\_data.py** (within `sensors` feature)

```
def store_sensor_data(sensor_data, database):
    """
    Store sensor data using an injected database dependency.
    """
    database.save(sensor_data)
```

Here, `database` is passed into `store_sensor_data` as a parameter, allowing different database implementations (e.g., in-memory database for testing, PostgreSQL for production) to be used as needed.

---

### **3\. Interfaces and Contracts**

FIMC’s modular structure avoids inheritance-based dependencies by relying on **interface-driven design**. Interfaces or contracts define the expected interactions between modules, allowing each module to specify its requirements and functionalities without tightly coupling to a shared base class.

#### **Why Interfaces and Contracts?**

* **Loose Coupling**: Interfaces provide a contract for interactions, enabling modules to interact without direct dependencies on each other’s internal implementations.
* **Flexibility**: By using interfaces instead of inheritance, FIMC allows modules to be updated or replaced without modifying the rest of the system, which is essential for maintaining modularity.
* **Interchangeability**: Interfaces make it easy to swap out modules that adhere to the same interface, facilitating testing and component replacement.

#### **Example of Interface-Driven Design**

Suppose we have an **event dispatcher** interface that multiple modules (e.g., `robots`, `sensors`) use for event communication. The event dispatcher defines the expected methods, which each module can implement according to its needs.

**event\_dispatcher.py** (within `common` directory)

```
# event_dispatcher.py

class EventDispatcherInterface:
    def dispatch_event(self, event_type, payload):
        raise NotImplementedError("Subclasses must implement dispatch_event method.")
```

**robot\_events.py** (within `robots` feature)

```
from common.event_dispatcher import EventDispatcherInterface

class RobotEventDispatcher(EventDispatcherInterface):
    def dispatch_event(self, event_type, payload):
        # Custom implementation for dispatching robot events
        print(f"Dispatching robot event: {event_type} with payload: {payload}")
```

By implementing `EventDispatcherInterface`, `RobotEventDispatcher` provides a custom way of dispatching robot events, allowing different modules to use the same contract without needing a shared inheritance structure.

---

### **4\. Examples**

#### **Example 1: Dependency Injection in Feature Modules**

Consider a **sensor feature** that interacts with different types of sensors based on specific environmental conditions. Using dependency injection, we can pass in the required sensors as dependencies.

**proximity\_sensor.py** (within `sensors` feature)

```
def detect_obstacle(environment, sensor):
    """
    Detect obstacles using an injected sensor dependency.
    """
    return sensor.scan(environment)
```

Here, `sensor` is injected as a dependency, allowing flexibility in the type of sensor used for obstacle detection.

#### **Example 2: Direct Imports for Stateless Utilities**

When modules need access to global configuration data, direct imports from a `common` configuration module can be more efficient.

**config\_loader.py** (within `common` directory)

```
# config_loader.py

config = {
    "database_url": "http://database.local",
    "max_connections": 5
}

def get_config(key):
    return config.get(key)
```

**camera\_sensor.py** (within `sensors` feature)

```
from common.config_loader import get_config

def initialize_camera():
    db_url = get_config("database_url")
    # Use db_url to initialize the camera
```

Directly importing `get_config` from `config_loader` provides a consistent way to access configuration data without needing to inject it explicitly, simplifying dependencies for standardized configurations.

---

### **Summary**

Dependency management in FIMC is designed to maintain modular independence and flexibility, supporting modular autonomy without complex inheritance structures. Here’s a recap:

* **Explicit Dependencies**: Dependency injection ensures that modules declare dependencies explicitly, allowing for autonomy, flexibility, and adaptability.
* **Direct Imports vs. Dependency Injection**: Direct imports are used for consistent, stateless utilities, while dependency injection handles context-sensitive dependencies.
* **Interfaces and Contracts**: FIMC uses interfaces to define interactions between modules, maintaining loose coupling and flexibility.
* **Examples**: Real-world scenarios demonstrate dependency injection for flexible configurations and direct imports for standardized utilities.

By managing dependencies explicitly, FIMC supports a highly modular and adaptable structure, allowing each feature to operate independently and interchangeably without the rigid structures of traditional OOP.

