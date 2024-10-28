# **Autonomous Warehouse Robot Control System \- Requirements Document**

## **Project Overview**

The Autonomous Warehouse Robot Control System is a simulated application designed to control multiple autonomous robots operating in a warehouse environment. Each robot must navigate the warehouse, detect and pick up items, avoid obstacles, and communicate with a central control unit for efficient task management. The goal is to evaluate two architectural approaches, **Object-Oriented Programming (OOP)** and **feature-based, dependency-driven modular architecture**, by implementing and comparing them in a controlled setting.

This document details the core requirements, functional modules, and performance criteria essential for both architectures.

---

## **System Objectives**

1. **Modularity and Extensibility**: The system must support adding new robot types, sensors, or tasks without significant refactoring.
2. **Real-Time Responsiveness**: The system must handle dynamic task assignments and obstacle avoidance in real time, adapting to warehouse changes as they occur.
3. **Safety and Reliability**: Robust error handling and safety protocols are essential to ensure safe navigation and reliable task completion.
4. **Developer Productivity and Cognitive Load**: The system should be implemented with minimal cognitive load for developers, aiming for easy-to-understand, maintainable code.

---

## **Functional Requirements**

### **1\. Central Control Unit (CCU)**

The Central Control Unit (CCU) is the main module responsible for overall warehouse management, task assignment, and robot coordination.

#### **Functional Specifications:**

* **Robot Coordination**: Track each robot’s location, status, and task progress.
* **Task Assignment**: Assign tasks to robots based on task priority and robot availability.
* **Safety Monitoring**: Track and respond to any reported errors or safety issues from robots and sensors.
* **Event-Driven Communication**: Maintain event-driven communication for task allocation, task completion, and emergency alerts.
* **Logging**: Maintain a log of events, tasks, and errors for monitoring and debugging purposes.

#### **Design Requirements:**

* **OOP**: Implement the CCU as a Singleton class, managing robot and sensor state using the Observer pattern.
* **Feature-Based**: Implement the CCU as a module within the `features/control` directory, using in-module event handling for communication and state tracking.

### **2\. Robots**

Robots are autonomous units responsible for carrying out assigned tasks (e.g., picking, sorting, inspection) and navigating the warehouse.

#### **Types of Robots:**

* **Picking Robot**: Designed to locate and pick up items from shelves.
* **Sorting Robot**: Responsible for sorting items based on specified criteria.
* **Inspection Robot**: Performs inspection tasks, verifying item conditions.

#### **Functional Specifications:**

* **Task Execution**: Execute assigned tasks based on configuration parameters, including speed, range, and task priority.
* **Obstacle Avoidance**: Detect and avoid obstacles using sensor data.
* **Status Reporting**: Report task completion, errors, and current status to the CCU.
* **Sensor Integration**: Interact with various sensors to receive data (e.g., proximity, weight, camera).

#### **Design Requirements:**

* **OOP**: Implement `Robot` as a base class with shared methods for movement, task execution, and sensor integration. Each robot type (Picking, Sorting, Inspection) is a subclass of `Robot`.
* **Feature-Based**: Implement each robot type (e.g., picking\_robot.py, sorting\_robot.py, inspection\_robot.py) as an independent module in `features/robots`. Use composition and dependency injection for task and sensor interactions.

### **3\. Sensors**

Sensors provide real-time feedback to robots, enabling obstacle detection, item identification, and task verification.

#### **Types of Sensors:**

* **Proximity Sensor**: Detects nearby obstacles to support obstacle avoidance.
* **Weight Sensor**: Measures item weight for sorting and verification tasks.
* **Camera Sensor**: Captures images or video for inspection tasks.

#### **Functional Specifications:**

* **Data Collection**: Capture sensor data based on configuration parameters (e.g., range, frequency).
* **Error Reporting**: Detect and report sensor malfunctions to the CCU.
* **Real-Time Feedback**: Provide immediate feedback to robots for obstacle avoidance and task confirmation.

#### **Design Requirements:**

* **OOP**: Implement `Sensor` as an abstract base class with methods for data collection and reporting. Each sensor type (Proximity, Weight, Camera) is a subclass.
* **Feature-Based**: Implement each sensor type as an independent module (e.g., proximity\_sensor.py, weight\_sensor.py, camera\_sensor.py) in `features/sensors`.

### **4\. Tasks**

Tasks represent the specific actions robots perform in the warehouse. Each task module defines the logic and conditions for successful completion.

#### **Types of Tasks:**

* **Pick Item Task**: Directs a robot to locate and pick up a specified item.
* **Sort Item Task**: Instructs a robot to sort items based on predefined criteria.
* **Avoid Obstacle Task**: Commands a robot to navigate around detected obstacles.

#### **Functional Specifications:**

* **Task Initialization**: Set task-specific parameters (e.g., priority, item ID).
* **Dependency Injection**: Manage dependencies, such as sensor inputs and control commands, through dependency injection.
* **Task Completion Reporting**: Notify the CCU upon task completion.

#### **Design Requirements:**

* **OOP**: Implement `Task` as an abstract class, with `PickItemTask`, `SortItemTask`, and `AvoidObstacleTask` as subclasses.
* **Feature-Based**: Implement each task as an independent module in `features/tasks` (e.g., pick\_item\_task.py, sort\_item\_task.py, avoid\_obstacle\_task.py).

### **5\. Safety Protocols**

Safety protocols are responsible for handling collision avoidance, error tracking, and emergency states, ensuring safe robot operations within the warehouse.

#### **Functional Specifications:**

* **Collision Avoidance**: Actively prevent collisions by analyzing sensor data and adjusting robot paths.
* **Error Tracking**: Track and log errors from robots and sensors, escalating to the CCU if necessary.
* **Emergency State Logging**: Record and manage emergency states, such as system shutdowns or critical errors.

#### **Design Requirements:**

* **OOP**: Implement a `SafetyController` class, using design patterns like Observer to monitor robot states and respond to emergency conditions.
* **Feature-Based**: Implement safety protocols as a module in `features/control/safety_protocols.py`, using direct in-module handling to monitor and manage safety conditions.

---

## **Non-Functional Requirements**

### **1\. Performance and Responsiveness**

* **Requirement**: The system must support real-time responses to dynamic events, such as task allocation, obstacle detection, and error reporting.
* **Metric**: Measure response times for task assignments, sensor data processing, and error handling to evaluate real-time performance.

### **2\. Modularity and Scalability**

* **Requirement**: The system should allow easy addition of new robots, sensors, or tasks without affecting existing components.
* **Metric**: Measure time and lines of code required to add new features. Evaluate reusability of code in OOP (inheritance, interfaces) versus feature-based (modular composition).

### **3\. Safety and Reliability**

* **Requirement**: The system must handle errors gracefully, logging issues and ensuring safe operations during malfunctions or unexpected conditions.
* **Metric**: Measure error recovery times and evaluate resilience under simulated failure scenarios for both architectures.

### **4\. Developer Productivity and Cognitive Load**

* **Requirement**: Minimize cognitive load for developers by organizing code logically, ensuring ease of understanding and extension.
* **Metric**: Track implementation time as the primary measure of cognitive load when adding new features.

---

## **Benchmarking and Testing**

### **1\. Extensibility and Cognitive Load Testing**

* **Objective**: Evaluate the ease of adding new components to each architecture.
* **Test Cases**:
  * Add `ScanningRobot`, `TemperatureSensor`, and `InspectItemTask`.
  * Measure time taken and LOC for each addition as a direct measure of extensibility and cognitive load.

### **2\. Real-Time Responsiveness Testing**

* **Objective**: Measure the system’s ability to handle real-time interactions, such as dynamic task assignment and obstacle detection.
* **Test Cases**:
  * Simulate multiple robots receiving tasks and encountering obstacles.
  * Track response times for task allocation, sensor feedback, and obstacle avoidance.

### **3\. Safety and Error Handling Testing**

* **Objective**: Test the system’s resilience and error management capabilities.
* **Test Cases**:
  * Simulate sensor malfunctions, robot malfunctions, and emergency conditions.
  * Record error recovery times and evaluate reliability under each scenario.

### **4\. Code Reusability and Maintenance Testing**

* **Objective**: Assess the amount of reusable versus duplicated code, particularly for similar features.
* **Test Cases**:
  * Evaluate LOC for similar components (e.g., adding a new robot or sensor type).
  * Analyze reusability in OOP’s inheritance model versus the feature-based modular setup.

### **5\. Modularity Testing**

* **Objective**: Verify each module’s independence and ability to operate without unintended dependencies.
* **Test Cases**:
  * Run tests where each module is tested in isolation (e.g., testing individual sensors or tasks).
  * Evaluate modular boundaries and assess whether each module operates as a self-contained unit.

---

## **Summary of Requirements**

| Feature | Description | Design Requirements |
| ----- | ----- | ----- |
| **Central Control Unit (CCU)** | Manages robot coordination, task assignment, and safety protocols. | Singleton in OOP, independent module in feature-based |
| **Robots** | Autonomous units that execute tasks and avoid obstacles. | Subclasses in OOP, independent modules in feature-based |
| **Sensors** | Real-time data providers (e.g., proximity, weight, camera) for robots. | Subclasses in OOP, independent modules in feature-based |
| **Tasks** | Define specific robot actions, such as picking, sorting, and avoiding obstacles. | Abstract classes in OOP, independent modules in feature-based |
| **Safety Protocols** | Handle collision avoidance, error tracking, and emergency logging. | Central controller in OOP, independent handling in feature-based |
| **Performance Metrics** | Real-time responsiveness, modularity, safety, reusability, and developer productivity | Evaluated through benchmarks and testing |

---

This requirements document ensures that both **OOP and feature-based architectures** meet identical core functionalities, providing a basis for objective benchmarking. Each component’s requirements, functional behaviors, and metrics are designed to illustrate strengths and limitations, allowing for a comprehensive evaluation of modular autonomy, cognitive simplicity, and suitability for real-time, safety-critical applications.

