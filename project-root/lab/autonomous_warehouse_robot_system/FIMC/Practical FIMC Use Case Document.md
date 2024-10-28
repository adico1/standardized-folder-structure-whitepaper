### **Practical FIMC Use Case Document**

---

#### **Purpose:**

**This document showcases FIMC (Feature-based, Dependency-driven Folder Structure with Modules and Composition) in action through a real-world application example, the Autonomous Warehouse Robot Control System. It illustrates FIMC’s strengths in modularity, extensibility, and simplicity.**

---

### **System Description: Autonomous Warehouse Robot Control System**

**The Autonomous Warehouse Robot Control System is a simulated system managing multiple autonomous robots in a warehouse setting. Each robot performs tasks such as navigating aisles, picking up items, sorting, and avoiding obstacles. The system is designed to coordinate these tasks using FIMC principles, prioritizing modularity, independence, and clear dependency management.**

#### **System Requirements:**

* **Central Control: A module for coordinating the robots, tracking status, assigning tasks, and managing safety protocols.**
* **Robots: Independent units that execute assigned tasks using various sensors and controls, each specializing in a different function (e.g., picking, sorting, inspection).**
* **Sensors: Real-time feedback mechanisms allowing robots to interact with the environment, including sensors for proximity, weight, and visual input.**
* **Tasks: Define individual jobs for robots, such as picking items, sorting items, and avoiding obstacles.**
* **Safety Protocols: Modules to manage collision avoidance, log errors, and ensure safe operation in a high-density environment.**

---

### **Feature Breakdown**

**Each feature is structured independently, with its own set of modules and dependencies, ensuring modular autonomy and a clear structure.**

#### **1\. Central Control (Feature: `control`)**

* **Purpose: Manages overall coordination of the robots, monitors robot states, assigns tasks, and enforces safety protocols.**
* **Modules:**
  * **`control_center.py`: Main control unit for managing task assignments and tracking robot status.**
  * **`safety_protocols.py`: Manages error handling and safety measures (e.g., collision avoidance).**

#### **2\. Robots (Feature: `robots`)**

* **Purpose: Each robot has unique functionalities and operates independently, executing tasks assigned by the control center.**
* **Modules:**
  * **`picking_robot.py`: Manages logic specific to picking tasks, such as navigating aisles and picking up items.**
  * **`sorting_robot.py`: Handles tasks related to sorting items based on specified criteria.**
  * **`inspection_robot.py`: Conducts inspection tasks, such as scanning and verifying item information.**
* **Shared Module:**
  * **`shared/robot_utils.py`: Contains utility functions relevant to robot features, such as movement controls, task prioritization, and sensor integration.**

#### **3\. Sensors (Feature: `sensors`)**

* **Purpose: Each sensor module provides real-time data to the robots, enabling them to respond to the environment.**
* **Modules:**
  * **`proximity_sensor.py`: Tracks obstacles or other robots nearby to prevent collisions.**
  * **`weight_sensor.py`: Measures the weight of items picked or moved by robots.**
  * **`camera_sensor.py`: Provides visual data for item recognition or aisle navigation.**
* **Shared Module:**
  * **`shared/sensor_utils.py`: Contains utility functions for sensor data processing, filtering, and integration.**

#### **4\. Tasks (Feature: `tasks`)**

* **Purpose: Define tasks that can be dynamically assigned to robots, ensuring each robot executes tasks independently.**
* **Modules:**
  * **`pick_item_task.py`: Logic for picking and moving items.**
  * **`sort_item_task.py`: Logic for sorting items based on categories or weight.**
  * **`avoid_obstacle_task.py`: Logic for obstacle avoidance, using sensor data for real-time navigation.**

---

### **Implementation Examples**

**This section provides FIMC-specific code snippets and explanations to illustrate how modules interact without inheritance, relying instead on function composition, dependency injection, and modular autonomy.**

#### **1\. Central Control Module (`control_center.py`)**

**The `control_center.py` module manages task assignments and robot coordination using dependency injection to interact with other modules.**

```
# control_center.py
from tasks.pick_item_task import execute_pick_task
from tasks.avoid_obstacle_task import avoid_obstacle
from robots.shared.robot_utils import update_robot_status
from sensors.shared.sensor_utils import check_for_obstacles

def assign_task(robot, task):
    if task == "pick_item":
        execute_pick_task(robot)
    elif task == "avoid_obstacle":
        avoid_obstacle(robot)
    update_robot_status(robot)

def monitor_safety(robot, sensor_data):
    if check_for_obstacles(sensor_data):
        avoid_obstacle(robot)
    # Add more safety measures as needed
```

**In this example:**

* **Dependency Injection: Functions from other modules (`execute_pick_task`, `avoid_obstacle`, etc.) are injected into the `control_center` rather than relying on a base class.**
* **Event-Driven Safety Monitoring: The `monitor_safety` function checks sensor data for obstacles and initiates avoidance if necessary, illustrating how FIMC manages real-time events.**

#### **2\. Picking Robot Module (`picking_robot.py`)**

**The `picking_robot.py` module is responsible for executing picking tasks, relying on `robot_utils` for movement control.**

```
# picking_robot.py
from robots.shared.robot_utils import move_to_location, pick_item

def execute_picking_task(location):
    move_to_location(location)
    pick_item()
    print("Item picked successfully")
```

**In this example:**

* **Modular Composition: The picking robot composes its functionality from functions in `robot_utils`, maintaining independence and simplifying testing.**
* **No Inheritance: The robot behavior is customized through function calls rather than inheritance, making it easy to modify or replace individual behaviors without affecting the entire system.**

#### **3\. Proximity Sensor Module (`proximity_sensor.py`)**

**The `proximity_sensor.py` module detects nearby obstacles, alerting the robot or control center to avoid collisions.**

```
# proximity_sensor.py
from sensors.shared.sensor_utils import get_proximity_data

def detect_obstacle():
    distance = get_proximity_data()
    return distance < 10  # Arbitrary threshold for obstacle detection
```

**In this example:**

* **Independent Functionality: The module is self-contained, relying on shared sensor utilities for its core functionality.**
* **Modular Interactions: The control center or robot modules can invoke `detect_obstacle` as needed, showing how sensor functionality remains isolated but accessible.**

#### **4\. Pick Item Task Module (`pick_item_task.py`)**

**The `pick_item_task.py` module defines the specific steps for executing a picking task, allowing robots to complete this task independently.**

```
# pick_item_task.py
from robots.picking_robot import execute_picking_task

def execute_pick_task(robot):
    location = determine_pick_location(robot)
    execute_picking_task(location)
```

**In this example:**

* **Function-Based Task Execution: The task is executed by calling the relevant robot function (`execute_picking_task`) without needing a shared base class.**
* **Inter-module Dependency Injection: The task depends on functions from the robot module, showcasing dependency injection for flexibility.**

---

### **Metrics and Benchmarking**

**To evaluate the FIMC structure, we measure modularity, extensibility, error handling, and compare it to a similar OOP system.**

#### **1\. Modularity**

* **Metric: Measure lines of code (LOC) per feature and track how isolated each feature is in terms of dependencies.**
* **Expected Result: FIMC should result in well-contained, independent modules, with clear, minimal dependencies on other features.**

#### **2\. Extensibility**

* **Metric: Time required to add a new feature (e.g., a new sensor type) and the number of changes needed in other parts of the system.**
* **Expected Result: FIMC should allow new modules to be added independently without affecting other modules, demonstrating high extensibility.**

#### **3\. Error Handling and Safety**

* **Metric: Test error handling capabilities, including the ability to gracefully handle sensor failures or robot malfunctions.**
* **Expected Result: FIMC’s modularity should allow for isolated error handling within each module, with fallback mechanisms like the `safety_protocols.py` in the control module managing broader safety concerns.**

#### **4\. Real-Time Performance**

* **Metric: Measure response times for task allocation, obstacle detection, and task completion.**
* **Expected Result: FIMC should achieve competitive response times by keeping modules autonomous, limiting dependency on centralized processing.**

#### **5\. Cognitive Load and Complexity**

* **Metric: Track time developers spend adding or modifying features and their ease of understanding the structure.**
* **Expected Result: FIMC’s feature-based organization should minimize cognitive load, as developers only need to focus on individual feature modules rather than navigating an inheritance hierarchy.**

---

### **Conclusion**

**This example of the Autonomous Warehouse Robot Control System demonstrates how FIMC can be used to structure complex applications modularly, emphasizing simplicity, testability, and extensibility. By managing dependencies through injection and event-driven updates, FIMC allows for flexible, adaptable systems without the need for inheritance hierarchies typical in OOP. The outlined metrics provide a basis for comparing FIMC’s efficiency, modularity, and maintainability against an OOP approach.**

