### **Document: Design Patterns and Principles Applied in FIMC**

**Purpose: This document explains the core design principles behind FIMC and illustrates how they are applied in place of traditional OOP design patterns. FIMC achieves flexibility, modularity, and simplicity by using composition, event-driven communication, and interface-based design, all without using classes or inheritance. Practical examples are provided to demonstrate these principles.**

---

## **Contents**

1. **Composition Over Inheritance**
2. **Event-Driven Design**
3. **Interface-Based Design**
4. **Examples**

---

### **1\. Composition Over Inheritance**

**Overview:**
**In FIMC, composition is favored over inheritance, meaning that functionality is achieved by combining small, focused modules rather than building a hierarchy of classes. This approach eliminates tight coupling and allows each feature to remain self-contained and independent.**

**How Composition Works in FIMC:**

* **Each feature (e.g., `robots`, `sensors`) is organized as a module with specific functionality, without creating subclasses or shared parent classes.**
* **Modules use pure functions to implement behavior and compose functionality by importing and combining functions from other modules or shared utilities.**
* **Shared behavior is organized in utility functions within shared or common modules, allowing each feature to independently use these functions as needed without inheriting from a base class.**

**Example of Composition: Consider an Autonomous Warehouse Robot Control System with different robot types, such as `PickingRobot` and `SortingRobot`. Each robot type is implemented as a module that imports and combines shared functions.**

```
# features/robots/picking_robot.py
from common import movement_utils, task_utils

def execute_task(task):
    movement_utils.move_to_location(task["location"])
    task_utils.perform_task(task)
    return "Task completed"

# features/robots/sorting_robot.py
from common import movement_utils, sorting_utils

def execute_task(task):
    movement_utils.move_to_location(task["location"])
    sorting_utils.sort_items(task["items"])
    return "Sorting task completed"
```

**Here, `PickingRobot` and `SortingRobot` achieve functionality by composing shared functions (`movement_utils`, `task_utils`, `sorting_utils`) instead of using a base class. Each robot type is modular and self-contained, allowing flexibility to add or modify behavior independently.**

**Benefits of Composition:**

* **Modularity: Each feature is independently modifiable and testable.**
* **Flexibility: Adding new behaviors or types doesn’t require modifying a base class or hierarchy.**
* **Reduced Coupling: Composition avoids tight coupling, making features more adaptable and easy to test.**

---

### **2\. Event-Driven Design**

**Overview:**
**FIMC uses event-driven communication to facilitate interactions between modules, achieving modular autonomy without central control. Each module can operate independently and react to changes or events, reducing dependencies between modules.**

**How Event-Driven Design Works in FIMC:**

* **Modules communicate by triggering events, where one module initiates an event (e.g., task completion) and other modules listen and respond as needed.**
* **This design decouples modules, allowing each to handle events autonomously.**
* **Event dispatchers or lightweight message-passing functions facilitate this communication, allowing each feature to handle only the events it needs.**

**Example of Event-Driven Communication: In the warehouse system, robots and sensors communicate through events. For example, when a `ProximitySensor` detects an obstacle, it triggers an alert event to which other modules, like `ControlCenter`, can respond.**

```
# features/sensors/proximity_sensor.py
from shared.event_dispatcher import dispatch_event

def detect_obstacle():
    # Logic to detect obstacle
    obstacle_detected = True
    if obstacle_detected:
        dispatch_event("obstacle_detected", {"location": get_sensor_location()})

# features/control/control_center.py
from shared.event_dispatcher import subscribe_to_event

def handle_obstacle(event_data):
    print(f"Obstacle detected at {event_data['location']}. Redirecting robots.")
    # Logic to redirect robots

# Subscribe to the event
subscribe_to_event("obstacle_detected", handle_obstacle)
```

**In this setup:**

* **`ProximitySensor` triggers an `"obstacle_detected"` event.**
* **`ControlCenter` listens for the event and responds without directly coupling to `ProximitySensor`.**

**Benefits of Event-Driven Design:**

* **Independence: Modules operate autonomously, responding to events without direct dependencies.**
* **Flexibility: New modules can subscribe to events without modifying the publisher.**
* **Real-Time Responsiveness: Modules can react to real-time changes, supporting system adaptability without central control.**

---

### **3\. Interface-Based Design**

**Overview:**
**FIMC achieves standardized functionality across modules through interface-based design, using predefined functions and contracts rather than base classes. This allows for predictable interactions and standardization without inheritance.**

**How Interface-Based Design Works in FIMC:**

* **Instead of creating a shared class hierarchy, FIMC modules agree on a set of function names and expected parameters to fulfill specific roles.**
* **These interfaces are defined as function signatures or in documentation, setting a contract for how each module should behave without enforcing a class structure.**
* **This allows for easy substitution or replacement of modules that follow the same interface.**

**Example of Interface-Based Design: In the warehouse system, each sensor module (e.g., `ProximitySensor`, `WeightSensor`) follows an agreed-upon interface that includes methods like `read_data()` and `calibrate()` without a shared class or inheritance.**

```
# features/sensors/proximity_sensor.py
def read_data():
    # Logic specific to reading proximity data
    return {"distance": calculate_distance()}

def calibrate():
    # Proximity sensor-specific calibration logic
    pass

# features/sensors/weight_sensor.py
def read_data():
    # Logic specific to reading weight data
    return {"weight": measure_weight()}

def calibrate():
    # Weight sensor-specific calibration logic
    pass
```

**Here, both `ProximitySensor` and `WeightSensor` adhere to a shared interface by implementing the functions `read_data()` and `calibrate()`, but each is a standalone module with its own unique implementation.**

**Benefits of Interface-Based Design:**

* **Flexibility: Modules aren’t bound to rigid structures and can be easily modified.**
* **Standardization: Interfaces ensure consistency across modules performing similar roles.**
* **Testability: Interfaces enable easy substitution, making testing straightforward without dependencies on a shared class structure.**

---

### **4\. Examples of FIMC Principles in Practice**

**Scenario: Modular Control System with Robots and Sensors**

* **Description: An Autonomous Warehouse Robot Control System uses FIMC principles to manage robots, sensors, and tasks without centralized control.**
* **Composition Example: `PickingRobot` and `SortingRobot` use shared utilities from `movement_utils` and `task_utils` without a shared `Robot` base class.**
* **Event-Driven Example: `ProximitySensor` dispatches an `"obstacle_detected"` event, allowing `ControlCenter` to respond autonomously without direct coupling.**
* **Interface-Based Example: Sensor modules implement `read_data()` and `calibrate()` functions, achieving standardization without inheritance.**

**This example illustrates how FIMC’s design principles enable modular autonomy, real-time responsiveness, and flexibility without OOP’s inheritance and tightly coupled structures. Each component operates independently, while interfaces, events, and composition ensure consistent behavior across the system.**

---

### **Summary**

**The design patterns and principles of FIMC—composition over inheritance, event-driven communication, and interface-based design—allow for a highly modular and adaptable architecture without classes or inheritance. By focusing on independent, self-contained modules and flexible interactions, FIMC supports modularity and extensibility, making it ideal for complex systems that require autonomy and maintainability.**

