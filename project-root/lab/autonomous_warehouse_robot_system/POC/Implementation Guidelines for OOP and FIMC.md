# **Implementation Guidelines for OOP and FIMC**

### **Objective**

**This document provides specific guidelines for structuring an autonomous warehouse robot control system in both Object-Oriented Programming (OOP) and Feature-based Dependency-Driven Folder Structure with Modules and Composition (FIMC) architectures. It details best practices for structuring classes and handling dependencies, events, and communication in each paradigm.**

---

## **Object-Oriented Programming (OOP) Structure**

### **Core Principles**

**In OOP, use classes to encapsulate the properties and behaviors of the system’s entities. Leverage inheritance and polymorphism to promote reusability and adaptability within a hierarchical structure. Encapsulation, inheritance, and polymorphism will drive the class structure.**

### **Class and Inheritance Structure**

1. **Robot Class Hierarchy:**
   * **Base Class: Create a `Robot` base class containing shared properties and methods such as `id`, `position`, `status`, and basic `move()` functionality.**
   * **Derived Classes: Create specialized robot classes (e.g., `PickerRobot`, `TransportRobot`) inheriting from `Robot` to handle specific tasks. Each subclass can override methods or add specialized attributes relevant to its function.**

```
class Robot:
    def __init__(self, robot_id, position):
        self.robot_id = robot_id
        self.position = position
        self.status = "idle"

    def move(self, target_position):
        # Implement movement logic
        pass

class PickerRobot(Robot):
    def __init__(self, robot_id, position):
        super().__init__(robot_id, position)
        # Additional attributes or methods specific to picking tasks

    def pick_item(self, item):
        # Implement picking logic
        pass
```

3. **Sensor Class Hierarchy:**
   * **Base Class: Define a `Sensor` class with a `detect()` method to abstract common functionality.**
   * **Derived Classes: Create specific sensor types (e.g., `InfraredSensor`, `UltrasonicSensor`) inheriting from `Sensor` to implement detection behaviors.**

```
class Sensor:
    def detect(self):
        # Default detection logic
        pass

class InfraredSensor(Sensor):
    def detect(self):
        # Specific detection logic for infrared
        pass
```

5. **Task Management:**
   * **Create a `Task` class with subclasses (`PickTask`, `TransportTask`, etc.) to encapsulate task types.**
   * **The `TaskManager` class acts as a central authority that assigns tasks based on robot availability and status.**

```
class Task:
    def __init__(self, task_id, description):
        self.task_id = task_id
        self.description = description

class PickTask(Task):
    def __init__(self, task_id, item):
        super().__init__(task_id, "Pick Task")
        self.item = item

```

### **Communication and Coordination**

* **Centralized Communication: The `TaskManager` and `Robot` classes communicate directly via method calls, centralizing task assignment.**
* **Error Handling: Implement exception handling within methods (e.g., `move()`, `detect()`) and propagate exceptions up to the `TaskManager` when necessary.**
* **Polymorphism: Use polymorphism for task handling across different robot types, allowing the `TaskManager` to assign tasks to any robot regardless of its subclass.**

---

## **FIMC Structure**

### **Core Principles**

**In FIMC, modularity and autonomy are achieved through feature-based modules and explicit dependency injection. FIMC avoids shared base classes, using interfaces and event-driven communication instead. Each feature operates as a standalone module, interacting with others through dependency injection and events.**

### **Feature Modules and Dependency Injection**

1. **Navigation Module:**
   * **Implement as an independent module that handles movement and pathfinding.**
   * **Inject dependencies, such as `obstacle_detector` and `position_tracker`, to provide required data.**
   * **Expose a `move_to(position)` function that interacts with injected dependencies for path calculation and obstacle checks.**

```
class Navigation:
    def __init__(self, obstacle_detector):
        self.obstacle_detector = obstacle_detector

    def move_to(self, position):
        if not self.obstacle_detector.is_obstacle_in_path(position):
            # Move logic here
            pass
```

3. **TaskAssignment Module:**
   * **This module assigns tasks based on robot status and availability. Use dependency injection to receive an event dispatcher for notifying other modules of task assignments.**
   * **Expose a `assign_task(robot_id, task)` function to handle assignments and broadcast events.**

```
class TaskAssignment:
    def __init__(self, event_dispatcher):
        self.event_dispatcher = event_dispatcher

    def assign_task(self, robot_id, task):
        self.event_dispatcher.broadcast("task_assigned", robot_id, task)

```

5. **ObstacleDetection Module:**
   * **Feature module for detecting obstacles in real-time. Inject specific sensor dependencies (e.g., `InfraredSensor`) based on context.**
   * **Expose a `is_obstacle_in_path(position)` function that returns obstacle status, allowing `Navigation` to make safe routing decisions.**

```
class ObstacleDetection:
    def __init__(self, sensor):
        self.sensor = sensor

    def is_obstacle_in_path(self, position):
        return self.sensor.detect(position)
```

7. **Communication Module:**
   * **This module acts as an event dispatcher, coordinating status updates and task notifications among features. It centralizes events but does not manage direct dependencies.**
   * **Use an `EventDispatcher` class that provides `subscribe(event, callback)` and `broadcast(event, *args)` methods, allowing modules to interact without hard-coded dependencies.**

```
class EventDispatcher:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event, callback):
        if event not in self.listeners:
            self.listeners[event] = []
        self.listeners[event].append(callback)

    def broadcast(self, event, *args):
        for callback in self.listeners.get(event, []):
            callback(*args)
```


### **Event-Driven Communication and Interaction**

* **Event Handling: Use an `EventDispatcher` for asynchronous, decoupled communication. Each module subscribes to events it cares about (e.g., `task_assigned`, `obstacle_detected`), allowing them to respond as necessary.**
* **Loose Coupling: Inject dependencies explicitly to avoid tight coupling. Modules only interact through the event dispatcher or injected dependencies, supporting modular independence.**
* **Flexibility and Testing: Modules are easily testable, as dependencies can be mocked or swapped out independently without altering the overall system.**

### **Summary of Key Differences**

| Aspect | OOP | FIMC |
| ----- | ----- | ----- |
| **Modularity** | **Centralized classes with inheritance hierarchies** | **Autonomous feature modules with dependency injection** |
| **Communication** | **Centralized communication via method calls** | **Decentralized, event-driven with dispatcher** |
| **Dependency Management** | **Tight coupling through class relationships** | **Loose coupling via explicit dependency injection** |
| **Error Handling** | **Exception handling within centralized classes** | **Error handling within modules, easy to isolate** |
| **Flexibility** | **Less flexible as classes are tightly coupled** | **Highly flexible, modular with independent features** |

---

### **Conclusion**

**This document outlines a balanced implementation for both OOP and FIMC in an autonomous warehouse robot control system. Each section provides guidelines on setting up classes, modules, dependency management, and inter-feature communication, allowing for a comparative Proof of Concept that highlights the strengths and trade-offs of each architecture.**

