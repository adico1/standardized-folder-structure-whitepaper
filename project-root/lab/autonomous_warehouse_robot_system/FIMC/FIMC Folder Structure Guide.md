**FIMC Folder Structure Guide**

---

### **Purpose**

This document provides a comprehensive guide to the **Feature-based, Dependency-driven Folder Structure with Modules and Composition (FIMC)** folder organization. By structuring code around independent features and leveraging shared utilities and explicit dependencies, FIMC enhances modularity, simplicity, and maintainability. This guide illustrates the recommended folder structure, with specific examples of the **general layout**, **feature-specific organization**, and **shared utilities** within a system.

---

### **General Folder Layout**

The FIMC folder structure is organized primarily into **features** that reflect core functionalities of the application, along with a **common** directory for non-feature-specific shared code and a **shared** subfolder within each feature to contain feature-specific utilities.

```
project_root/
│
├── common/                              # Global shared utilities across the application
│   ├── config_loader.py                 # Configuration loading utilities
│   ├── logger.py                        # Logging utility shared across features
│   └── utils.py                         # General-purpose helper functions
│
├── features/                            # Directory containing all main features of the system
│   ├── robots/                          # Main feature for robot-related functionality
│   │   ├── picking_robot.py             # Module for picking robot behavior
│   │   ├── sorting_robot.py             # Module for sorting robot behavior
│   │   ├── inspection_robot.py          # Module for inspection robot behavior
│   │   └── shared/                      # Shared code specific to robots
│   │       └── robot_utils.py           # Utility functions used by robot modules
│   │
│   ├── sensors/                         # Main feature for handling sensor-related functionality
│   │   ├── proximity_sensor.py          # Module for proximity sensor behavior
│   │   ├── weight_sensor.py             # Module for weight sensor behavior
│   │   ├── camera_sensor.py             # Module for camera sensor behavior
│   │   └── shared/                      # Shared code specific to sensors
│   │       └── sensor_utils.py          # Utility functions used by sensor modules
│   │
│   ├── tasks/                           # Main feature for task-related functionality
│   │   ├── pick_item_task.py            # Module for item picking tasks
│   │   ├── sort_item_task.py            # Module for item sorting tasks
│   │   └── avoid_obstacle_task.py       # Module for obstacle avoidance tasks
│   │
│   ├── control/                         # Main feature for central control and coordination
│   │   ├── control_center.py            # Manages robot coordination and task assignment
│   │   └── safety_protocols.py          # Handles safety protocols and error management
│   │
│   └── shared/                          # Cross-feature shared utilities for communication
│       └── event_dispatcher.py          # Event handling and communication utility
```

### **Feature-Specific Structure**

Within the **features** directory, each folder represents a distinct functionality of the system. Here’s how the **main features** are structured, along with an example of the sub-modules and utilities they may contain.

#### **Robots**

The `robots` folder contains modules specific to robot functionalities. Each robot type (e.g., `picking_robot`, `sorting_robot`) is implemented as a self-contained module, which makes each robot type independent and testable. A `shared` folder within `robots` includes utility functions used only by the robot modules.

* `picking_robot.py`: Implements behavior specific to a picking robot, such as item retrieval.
* `sorting_robot.py`: Implements behavior for a sorting robot, including sorting and stacking logic.
* `inspection_robot.py`: Implements behavior for a robot focused on inspecting items for quality control.
* `shared/robot_utils.py`: Contains helper functions used across different robot modules, such as common movement functions or communication protocols.

#### **Sensors**

The `sensors` folder manages modules related to various sensor types. Each sensor type (e.g., `proximity_sensor`, `weight_sensor`) is a standalone module that manages sensor-specific logic. The `shared` subfolder within `sensors` contains utilities only relevant to sensors.

* `proximity_sensor.py`: Manages proximity sensing logic, sending data to the control center or specific robots.
* `weight_sensor.py`: Handles weight measurements, used to assess item characteristics.
* `camera_sensor.py`: Manages image capture and processing.
* `shared/sensor_utils.py`: Helper functions for sensor modules, such as data parsing or validation methods.

#### **Tasks**

The `tasks` folder defines modules for specific tasks, such as picking an item, sorting items, or avoiding obstacles. Each task module is independent and can be reused across different contexts without relying on shared classes.

* `pick_item_task.py`: Defines the logic for an item picking task, coordinating with robots and sensors.
* `sort_item_task.py`: Manages sorting tasks for organization within the warehouse.
* `avoid_obstacle_task.py`: Handles logic for obstacle avoidance, typically used with sensor data.

#### **Control**

The `control` folder manages modules for coordination and control, specifically for orchestrating robot activities and enforcing safety protocols. This feature is often the primary point for issuing commands, receiving feedback, and ensuring system safety.

* `control_center.py`: The main coordination module, responsible for assigning tasks to robots and managing their statuses.
* `safety_protocols.py`: Handles safety-related protocols and error tracking to ensure smooth operation in a high-density environment.

### **Shared and Common Modules**

FIMC’s structure uses both **feature-specific shared folders** and a **global common directory** for shared utilities, providing a flexible way to share code without creating tight coupling.

#### **Common Folder**

The `common` folder contains global utilities or helpers that are used across multiple features. These utilities are generally stateless and do not need to know specific feature details. Examples include logging, configuration loading, and general-purpose helper functions.

* **`config_loader.py`**: Provides functionality to load configurations across all features. This is often a centralized configuration loader that different features can import directly without dependency injection.
* **`logger.py`**: A shared logging utility to ensure consistent logging standards across features.
* **`utils.py`**: Contains general-purpose helper functions that may be needed in multiple parts of the application (e.g., data formatting, error handling).

#### **Feature-Specific Shared Folders**

Within each main feature, a `shared` subfolder provides utilities that are specific to that feature but not required by other features. This helps keep feature dependencies isolated, reducing the risk of cross-feature coupling and keeping the codebase modular.

* **Example in `robots/shared/robot_utils.py`**: Contains utilities like navigation algorithms or motor control functions that are only relevant to robot modules.
* **Example in `sensors/shared/sensor_utils.py`**: Holds sensor-specific helper functions, such as data validation or calibration functions, that do not apply to other parts of the system.

### **Example FIMC Folder Structure**

Below is a sample folder structure for a FIMC-based application, showing the purpose of each main directory and module within the system.

```
project_root/
│
├── common/                                # Shared, non-feature-specific utilities
│   ├── config_loader.py                   # Configuration loading utility
│   ├── logger.py                          # Logging utility
│   └── utils.py                           # General-purpose helpers
│
├── features/
│   ├── robots/                            # Robot-specific modules and utilities
│   │   ├── picking_robot.py               # Picking robot module
│   │   ├── sorting_robot.py               # Sorting robot module
│   │   ├── inspection_robot.py            # Inspection robot module
│   │   └── shared/                        # Shared utilities specific to robots
│   │       └── robot_utils.py             # Helper functions for robot modules
│   │
│   ├── sensors/                           # Sensor-specific modules and utilities
│   │   ├── proximity_sensor.py            # Proximity sensor module
│   │   ├── weight_sensor.py               # Weight sensor module
│   │   ├── camera_sensor.py               # Camera sensor module
│   │   └── shared/                        # Shared utilities specific to sensors
│   │       └── sensor_utils.py            # Helper functions for sensor modules
│   │
│   ├── tasks/                             # Task-specific modules and utilities
│   │   ├── pick_item_task.py              # Pick item task module
│   │   ├── sort_item_task.py              # Sort item task module
│   │   └── avoid_obstacle_task.py         # Obstacle avoidance task module
│   │
│   ├── control/                           # Central control and safety modules
│   │   ├── control_center.py              # Main control module for coordination
│   │   └── safety_protocols.py            # Safety and error management protocols
│   │
│   └── shared/                            # Cross-feature shared utilities
│       └── event_dispatcher.py            # Manages event handling and inter-module communication

```

### **Summary**

The FIMC folder structure organizes code around feature-based modules to maximize modularity and maintainability. Each **feature** (like `robots`, `sensors`, and `tasks`) has its own directory with all the necessary modules and utilities, isolating functionality and dependencies. **Shared modules** within each feature and the global **common directory** allow for flexible, controlled code reuse without tight coupling, supporting FIMC’s goal of building independent, self-contained, and easily testable components.

