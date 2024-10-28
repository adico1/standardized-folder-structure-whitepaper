## **Design Patterns and Principles for OOP and FIMC Architectures**

### **Objective**

**This document provides a detailed guide on implementing design patterns and architectural principles for both Object-Oriented Programming (OOP) and Feature-based Dependency-Driven Folder Structure with Modules and Composition (FIMC). Each architecture will handle core features in an autonomous warehouse system, including Navigation, Task Assignment, Obstacle Detection, and Communication.**

### **OOP Design Patterns and Principles**

**OOP architecture leverages class-based inheritance, encapsulation, and polymorphism. The design ensures features are represented as objects with a hierarchical relationship, making it easy to manage robot types, sensors, and tasks through shared functionality.**

#### **1\. Inheritance for Shared Features**

**In OOP, inheritance enables the creation of a class hierarchy where common functionalities are encapsulated in base classes, allowing derived classes to extend or override behaviors.**

* **Robot Class Hierarchy:**
  * **Base Class: `Robot`**
    * **Attributes: `id`, `position`, `status`**
    * **Methods: `move`, `update_status`**
  * **Derived Classes:**
    * **`PickerRobot`, `TransportRobot` – Each robot type extends `Robot` with specific task-related functionalities (e.g., `pick` for `PickerRobot`).**

```
class Robot:
    def __init__(self, robot_id, position):
        self.robot_id = robot_id
        self.position = position
        self.status = "idle"

    def move(self, target_position):
        # Movement logic
        pass

class PickerRobot(Robot):
    def pick_task(self, item):
        # Picking task logic
        pass
```

#### **2\. Polymorphism for Task Handling and Sensors**

**Polymorphism allows different robots or sensors to respond to the same function call differently based on their type. This simplifies task handling and sensor-based obstacle detection.**

* **Task Polymorphism:**
  * **Task types (e.g., `PickTask`, `DeliverTask`) inherit from a `Task` base class and implement their specific logic.**
* **Sensor Polymorphism:**
  * **Sensors like `InfraredSensor` and `UltrasonicSensor` inherit from `ObstacleSensor`, enabling `detect_obstacle()` to behave differently for each type.**

```
class Task:
    def execute(self, robot):
        raise NotImplementedError("Subclasses must implement execute method")

class PickTask(Task):
    def execute(self, robot):
        # Picking task-specific execution
        pass
```

#### **3\. Encapsulation in Class-Based Structures**

**Encapsulation keeps each robot’s state and behaviors private to its class, allowing controlled access through methods. This ensures each robot's data, such as `status` and `position`, is secure and accessible only through designated methods.**

#### **4\. Centralized Task Management and Communication**

**In OOP, a TaskManager can centrally assign tasks to robots, while communication occurs directly between classes using references and method calls.**

* **TaskManager Class:**
  * **Manages task assignment, monitoring, and reassignment.**
* **Direct Method Calls:**
  * **Robots call each other’s methods to communicate status changes, e.g., `robot.update_status()`.**

---

### **FIMC Design Patterns and Principles**

**FIMC focuses on modular independence and loose coupling, using composition, dependency injection, and interface-driven design. Each feature operates independently, interacting with others through well-defined interfaces and event-driven communication.**

#### **1\. Composition Over Inheritance**

**Instead of inheritance, FIMC uses composition by grouping functionalities into independent modules. Each module can receive its dependencies through injection, promoting reusability without creating hierarchical structures.**

* **Feature-Based Modules:**
  * **Modules like `Navigation`, `TaskAssignment`, `ObstacleDetection` are developed as standalone components with dependencies injected at runtime.**
* **Example of Composition:**
  * **A `Robot` feature might compose `Navigation` and `ObstacleDetection` modules, with each module injected based on the robot’s requirements.**

```
class Navigation:
    def __init__(self, obstacle_detector):
        self.obstacle_detector = obstacle_detector

    def move_to(self, position):
        if not self.obstacle_detector.is_obstacle_in_path(position):
            # Navigation logic
            pass
```

#### **2\. Dependency Injection for Flexibility and Testing**

**Dependency injection is central to FIMC, enabling each module to receive only the dependencies it needs. This decouples modules, making them easier to test, maintain, and swap out as needed.**

* **Injected Dependencies:**
  * **A `Navigation` module might receive an `ObstacleDetection` module through injection rather than direct instantiation, supporting modular independence and testability.**

```
class TaskAssignment:
    def __init__(self, event_dispatcher):
        self.event_dispatcher = event_dispatcher

    def assign_task(self, robot_id, task):
        self.event_dispatcher.broadcast("task_assigned", robot_id, task)

```

#### **3\. Interface-Driven Design for Loose Coupling**

**Instead of inheritance, FIMC relies on interfaces and contracts to specify module behaviors, enabling different implementations to be swapped in without modifying the overall system.**

* **Interfaces for Communication:**
  * **A `NavigationInterface` might specify methods like `move_to()`, allowing any navigation module adhering to this interface to be injected as a dependency.**

**Example:**
```
class NavigationInterface:
    def move_to(self, position):
        raise NotImplementedError("Subclasses must implement move_to")

```

#### **4\. Event-Driven Communication for Inter-Module Interaction**

**FIMC employs event-driven communication instead of direct method calls, allowing modules to remain loosely coupled. An Event Dispatcher handles events like “task\_assigned” or “obstacle\_detected,” routing them to relevant modules.**

* **Event Dispatcher:**
  * **Acts as a centralized module that receives events and notifies interested modules, enabling asynchronous communication.**

```
class EventDispatcher:
    def __init__(self):
        self.listeners = {}

    def register_listener(self, event_type, listener):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)

    def broadcast(self, event_type, *args):
        for listener in self.listeners.get(event_type, []):
            listener(*args)

```

---

### **Comparison Summary**

| Aspect | OOP | FIMC |
| ----- | ----- | ----- |
| **Primary Pattern** | **Inheritance, Polymorphism** | **Composition, Dependency Injection** |
| **Encapsulation** | **Class-based** | **Module-based** |
| **Inter-Feature Communication** | **Centralized TaskManager** | **Event-Driven via Dispatcher** |
| **Modularity** | **Class hierarchies, shared base classes** | **Independent, dependency-injected modules** |
| **Testing Flexibility** | **Harder to isolate due to inheritance links** | **High, due to dependency injection** |

### **Guidelines for Implementing Each Architecture**

* **OOP:**
  * **Use class hierarchies to encapsulate shared behaviors.**
  * **Apply polymorphism for task-specific robot behaviors.**
  * **Use a centralized manager (e.g., `TaskManager`) to handle task assignments and updates.**
* **FIMC:**
  * **Structure each feature as an autonomous module, with dependencies injected where needed.**
  * **Use an event-driven dispatcher to manage inter-feature communication.**
  * **Implement interfaces or contracts instead of base classes for flexibility.**

**This document provides a foundation for implementing the PoC in both architectures, ensuring consistency and balanced design across OOP and FIMC approaches. Each pattern has been selected to showcase the strengths of both architectures in managing the core functionalities of an autonomous warehouse robot control system.**

