# **Interactions and Communication Protocols**

### **Purpose**

**This document provides the communication and interaction requirements for implementing both Object-Oriented Programming (OOP) and Feature-based Dependency-Driven Folder Structure with Modules and Composition (FIMC) in the Autonomous Warehouse Robot Control System PoC. The goal is to define how each core feature—Navigation, Task Assignment, Obstacle Detection, and Communication—interacts within each architectural paradigm.**

---

## **1\. Centralized Task Management (OOP Approach)**

**In the OOP implementation, interactions between features are managed primarily by a centralized `TaskManager` object, which acts as a coordinator for tasks and status updates.**

### **Key Interaction Requirements**

1. **Robot Status Updates:**
   * **Robots send status updates (e.g., task completed, obstacle encountered) directly to the `TaskManager`.**
   * **The `TaskManager` class manages the state and availability of each robot.**
   * **Each `Robot` class inherits from a base `Robot` class, which defines methods for updating and reporting status to the `TaskManager`.**
2. **Task Assignment:**
   * **The `TaskManager` assigns tasks by directly updating the task properties of each robot.**
   * **Robots inherit from a base `Robot` class and override methods as needed to perform specific tasks, such as `PickTask`, `TransportTask`, or `DeliverTask`.**
3. **Obstacle Detection:**
   * **Robots equipped with sensors directly report obstacle detections to the `TaskManager`.**
   * **If an obstacle is detected, the `TaskManager` reassigns tasks or reroutes the robot as needed.**
   * **`Sensor` classes (e.g., `InfraredSensor`, `UltrasonicSensor`) inherit from a `Sensor` base class and implement `detect_obstacle` methods.**

### **OOP Interaction Flow**

1. **TaskManager initiates a task and assigns it to an available robot.**
2. **Robot updates the TaskManager when it encounters an obstacle.**
3. **TaskManager updates or reassigns tasks based on robot and sensor statuses.**

### **OOP Example Code**

```
class TaskManager:
    def assign_task(self, robot, task):
        robot.receive_task(task)

    def update_status(self, robot, status):
        # Logic to handle robot status update
        pass

class Robot:
    def __init__(self, robot_id, task_manager):
        self.robot_id = robot_id
        self.task_manager = task_manager
        self.status = "idle"

    def update_status(self, status):
        self.status = status
        self.task_manager.update_status(self, status)

class ObstacleSensor:
    def detect_obstacle(self):
        # Detect and report obstacle
        return True
```

---

## **2\. Event-Driven, Dependency-Injection-Based Communication (FIMC Approach)**

**In the FIMC implementation, each feature is a self-contained module with dependencies explicitly injected. Interactions rely on an Event Dispatcher that allows modules to communicate through events, maintaining modular independence.**

### **Key Interaction Requirements**

1. **Event Dispatcher:**
   * **Serves as the core communication channel between feature modules.**
   * **Modules broadcast events (e.g., `task_assigned`, `task_completed`, `obstacle_detected`) through the dispatcher.**
   * **Each module subscribes only to relevant events, ensuring they receive the updates they need without direct dependencies.**
2. **Dependency Injection:**
   * **Feature modules (e.g., `Navigation`, `TaskAssignment`) receive injected dependencies as parameters.**
   * **The event dispatcher is injected into each module, allowing them to publish and listen for specific events.**
3. **Modular Task Assignment:**
   * **The `TaskAssignment` module listens for robot availability updates from the dispatcher and assigns tasks accordingly.**
   * **Task progress and completion events are broadcasted to update other modules, such as `TaskAssignment` and `Communication`.**
4. **Real-Time Obstacle Handling:**
   * **The `ObstacleDetection` module broadcasts `obstacle_detected` events if an obstacle is encountered.**
   * **The `Navigation` module subscribes to this event and reacts by adjusting routes or pausing movement.**

### **FIMC Interaction Flow**

1. **TaskAssignment broadcasts a `task_assigned` event with task details and robot ID.**
2. **Navigation listens for `obstacle_detected` events and updates the robot’s path as needed.**
3. **Communication receives `task_completed` and `obstacle_encountered` events and sends updates to the central system.**

### **FIMC Example Code**

```
class EventDispatcher:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event_type, listener):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)

    def dispatch(self, event_type, data):
        for listener in self.listeners.get(event_type, []):
            listener(data)

class Navigation:
    def __init__(self, obstacle_detector, event_dispatcher):
        self.obstacle_detector = obstacle_detector
        self.event_dispatcher = event_dispatcher
        self.event_dispatcher.subscribe("obstacle_detected", self.handle_obstacle)

    def handle_obstacle(self, data):
        # Logic to handle obstacle detection
        pass

class TaskAssignment:
    def __init__(self, event_dispatcher):
        self.event_dispatcher = event_dispatcher

    def assign_task(self, robot_id, task):
        # Broadcast task assigned event
        self.event_dispatcher.dispatch("task_assigned", {"robot_id": robot_id, "task": task})
```

---

## **3\. Summary of Requirements for Each Architecture**

| Feature | OOP Approach | FIMC Approach |
| ----- | ----- | ----- |
| **Task Assignment** | **Centralized `TaskManager` for task distribution** | **`TaskAssignment` module with event dispatch** |
| **Robot Status** | **Direct updates to `TaskManager`** | **Event dispatcher broadcasts task updates** |
| **Obstacle Handling** | **Robots notify `TaskManager` for re-routing** | **`ObstacleDetection` broadcasts events** |
| **Dependency Management** | **Shared classes through inheritance** | **Dependency injection with autonomous modules** |

---

### **Conclusion**

**This document defines the interaction and communication protocols for the PoC, highlighting how each architecture handles dependencies and inter-feature communication. In the OOP approach, centralized control through a `TaskManager` and direct status updates provide straightforward interactions, while the FIMC approach leverages modular autonomy, event-driven communication, and dependency injection for scalability and flexibility.**

**These guidelines will ensure balanced PoC implementations for both OOP and FIMC, allowing for an accurate comparison of modularity, scalability, and performance.**

