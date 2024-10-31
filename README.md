# **CORE: Comprehensive, Organized Repository for Engineering**

**Welcome to CORE, a structured, dependency-driven framework for building scalable, maintainable software across projects of any size. CORE provides a Unified Modular Structure (UMS) with a standardized modular folder system (DDFS), designed to enhance both individual productivity and team collaboration.**

---

## **Why CORE?**

**In software, the term "core" is often used vaguely to indicate essential components, leading to inconsistent organization across codebases. CORE reclaims "core" as a well-defined, foundational structure that supports clarity, scalability, and consistency in software projects.**

**UMS (Unified Modular Structure) is at the heart of CORE, built on principles of modularity, simplicity, and readability. It naturally integrates with any framework or architecture, placing DDFS (Dependency-Driven Folder Structure) at the center to organize code into logical, modular components that make it easy to scale and maintain. The Standard Way, an accompanying philosophy, guides developers to produce code that’s clean and predictable by setting practical standards of "work done" in code—balancing the ideals of perfection with the realities of development timelines.**

**Learn more about the philosophy and naming of CORE in [Why CORE?](https://github.com/adico1/standardized-folder-structure-whitepaper/blob/core-foundations/why-core.md).**

---

## **Glossary of Terms**

**CORE: A foundational framework that provides standardized structure, organization, and scalability, combining UMS, DDFS, and The Standard Way for a cohesive development experience.**

**UMS (Unified Modular Structure): The backbone of CORE, emphasizing modular design that breaks down software into independent components without class-based hierarchies. UMS achieves organization and encapsulation through folder structure and functional modules, supporting clear boundaries and adaptable code.**

**DDFS (Dependency-Driven Folder Structure): A key part of UMS, DDFS organizes code by logical modules, minimizing dependencies and creating clear flows of functionality. DDFS reduces redundancy and supports scalable development for projects ranging from simple apps to large systems.**

**The Standard Way (The DAO of Software Engineering): Inspired by craftsmanship, The Standard Way establishes a clear standard for what constitutes "work done" in code. This approach doesn’t aim for perfection at all costs; instead, it balances quality with practical speed by defining which aspects of code are essential for completion. Dependability, Adaptability, and Organization are the guiding principles, ensuring code remains clean, modular, and easy to read, with floating instructions (loose or unstructured code) organized into clear, concise functions.**

---

## **How CORE Works**

**CORE uses the Unified Modular Structure (UMS) as its guiding architecture, organizing code into modular components without class-based dependency hierarchies. Here’s a sample structure that illustrates how CORE organizes code, configurations, and dependencies:**

```
project-root/
├── src/
│   ├── main/
│   ├── features/
│   │   ├── feature1/
│   │   │   ├── index.js           # Exposes public functions only
│   │   │   ├── feature1-service/
│   │   │   ├── feature1-util/
│   │   │   └── shared/
│   │   └── feature2/
│   ├── common/
│   │   ├── helpers/
│   │   ├── dependencies/
│   │   └── shared-libs/
├── config/
│   ├── development/
│   └── production/
├── tests/
│   ├── unit-tests/
│   └── integration-tests/
└── deploy/
    ├── docker/
    ├── kubernetes/
    └── deployment-scripts/
```

### **Structure Overview:**

* **src/ contains main modules, features, and common libraries. Each feature module (e.g., `feature1`, `feature2`) includes encapsulated functionality.**  
* **config/ holds environment-specific settings, split into development and production.**  
* **tests/ is designated for unit and integration tests, with flexibility for feature-based test co-location if needed.**  
* **deploy/ stores deployment configurations and scripts, supporting Docker, Kubernetes, and other environments.**

**CORE’s structure is flexible enough for team customization. Teams can modify folder organization to fit project needs (e.g., relocating tests), with onboarding guides to clarify any deviations from the CORE standard.**

---

## **Real-World Example: CORE in Action**

**Before (Monolithic):**
```
robotics-warehouse/
├── src/
│   ├── application/                  # High-level tasks and orchestration
│   │   ├── TaskManager.psl           # Coordinates warehouse tasks
│   │   ├── RobotOrchestrator.psl     # Manages robot interactions, dispatches tasks
│   │   ├── interfaces/
│   │   │   ├── TaskInterface.psl     # Interface for different warehouse tasks
│   │   │   └── OrchestratorInterface.psl
│   │   └── controllers/
│   │       ├── WarehouseController.psl # Manages high-level warehouse commands
│   │       └── ErrorHandler.psl       # Global error handling
│   ├── core/                          # Core utilities, reusable code, interfaces
│   │   ├── interfaces/
│   │   │   ├── SensorInterface.psl    # Interface for different sensors
│   │   │   ├── MotorInterface.psl     # Interface for robot motors
│   │   │   └── ConfigInterface.psl    # Interface for configuration management
│   │   ├── utils/
│   │   │   ├── Logger.psl             # Logging utility for system-wide logging
│   │   │   ├── ConfigLoader.psl       # Manages configuration files
│   │   │   └── ConnectionManager.psl  # Manages network connections
│   ├── domain/                        # Domain layer representing key domain entities
│   │   ├── entities/
│   │   │   ├── Robot.psl              # Robot entity, encapsulates robot state
│   │   │   ├── Sensor.psl             # Sensor entity, tracks sensor states
│   │   │   └── Motor.psl              # Motor entity, tracks motor states
│   │   ├── factories/
│   │   │   ├── RobotFactory.psl       # Factory to create Robot instances
│   │   │   └── SensorFactory.psl      # Factory to create Sensor instances
│   │   └── repositories/
│   │       ├── RobotRepository.psl    # Repository for managing robot data
│   │       ├── SensorRepository.psl   # Repository for sensor data
│   │       └── TaskRepository.psl     # Repository for task-related data
│   ├── infrastructure/                # Low-level infrastructure and communication
│   │   ├── comms/
│   │   │   ├── RobotComm.psl          # Communication layer for robot commands
│   │   │   ├── SensorComm.psl         # Communication with sensors
│   │   │   └── TaskQueue.psl          # Manages task queuing
│   │   ├── database/
│   │   │   ├── DatabaseConnector.psl  # Manages DB connection and transactions
│   │   │   └── ORM.psl                # Object-relational mapping layer
│   │   └── messaging/
│   │       ├── MessageBroker.psl      # Manages message queue system
│   │       └── EventPublisher.psl     # Publishes events for real-time notifications
│   ├── service/                       # Core business logic for operations
│   │   ├── RobotService.psl           # Manages robot-specific operations
│   │   ├── SensorService.psl          # Manages sensor-related operations
│   │   ├── TaskService.psl            # Handles task-related operations
│   │   ├── MonitoringService.psl      # Monitors robot and sensor performance
│   │   ├── interfaces/
│   │   │   ├── ServiceInterface.psl   # General interface for services
│   │   │   └── MonitoringInterface.psl
│   └── ui/                            # UI layer for control dashboard
│       ├── Dashboard.psl              # Main dashboard UI
│       ├── RobotMonitor.psl           # UI for monitoring robots
│       ├── TaskViewer.psl             # UI for viewing and managing tasks
│       └── SensorMonitor.psl          # UI for monitoring sensor data
├── config/
│   ├── application.yml                # Main application configuration
│   ├── database.yml                   # Database configuration
│   ├── messaging.yml                  # Message broker configuration
│   └── sensors.yml                    # Configuration for sensor parameters
├── tests/                             # Testing structure
│   ├── unit/
│   │   ├── RobotServiceTest.psl       # Unit tests for RobotService
│   │   ├── TaskManagerTest.psl        # Unit tests for TaskManager
│   │   └── SensorCommTest.psl         # Unit tests for SensorComm
│   ├── integration/
│   │   ├── TaskIntegrationTest.psl    # Integration tests for task flows
│   │   └── RobotIntegrationTest.psl   # Integration tests for robot flows
│   └── e2e/
│       ├── FullWarehouseFlowTest.psl  # End-to-end test for warehouse operations
│       └── ErrorHandlingTest.psl      # Tests error handling and recovery
└── deploy/
    ├── docker-compose.yml             # Docker setup for deployment
    ├── kubernetes/
    │   ├── warehouse-deployment.yml   # Kubernetes deployment config for the app
    │   └── services.yml               # Kubernetes services configuration
    └── scripts/
        ├── init-db.psl                # Script to initialize database schema
        ├── deploy-robots.psl          # Deployment script for robot systems
        └── cleanup.psl                # Script for cleaning up deployment
```

**After (CORE Structure):**
```
robotics-warehouse/
├── src/
│   ├── main/                            # Entry point and system configuration
│   │   ├── App.psl                      # Main application entry point
│   │   └── Config.psl                   # Application-level configuration
│   ├── features/                        # Organized by core features
│   │   ├── warehouse-control/           # Warehouse control feature
│   │   │   ├── controllers/
│   │   │   │   └── WarehouseController.psl # Manages warehouse-level operations
│   │   │   ├── services/
│   │   │   │   └── ErrorHandler.psl        # Error handling for warehouse control
│   │   │   ├── ui/
│   │   │   │   └── WarehouseDashboard.psl  # UI for warehouse operations
│   │   │   └── interfaces/
│   │   │       └── WarehouseInterface.psl  # Interface for external access
│   │   ├── task-management/              # Task management feature
│   │   │   ├── TaskManager.psl           # Task delegation logic
│   │   │   ├── interfaces/
│   │   │   │   └── TaskInterface.psl     # Interface for task management
│   │   │   └── repositories/
│   │   │       └── TaskRepository.psl    # Task data handling
│   │   ├── robot-orchestration/          # Robot-specific orchestration
│   │   │   ├── RobotOrchestrator.psl     # Manages individual robot activities
│   │   │   ├── interfaces/
│   │   │   │   └── OrchestratorInterface.psl # Interface for robot orchestrator
│   │   │   ├── controllers/
│   │   │   │   └── RobotController.psl      # Robot command handling
│   │   │   ├── factories/
│   │   │   │   └── RobotFactory.psl         # Creates robot instances
│   │   │   └── repositories/
│   │   │       └── RobotRepository.psl      # Robot data storage
│   │   ├── monitoring/                    # Real-time monitoring and reporting
│   │   │   ├── services/
│   │   │   │   └── MonitoringService.psl     # Central monitoring logic
│   │   │   ├── ui/
│   │   │   │   └── MonitoringDashboard.psl   # Dashboard for real-time updates
│   │   │   └── interfaces/
│   │   │       └── MonitoringInterface.psl   # Interface for monitoring services
│   │   └── sensor-management/             # Manages sensor interactions
│   │       ├── SensorManager.psl          # Core sensor management logic
│   │       ├── interfaces/
│   │       │   └── SensorInterface.psl    # Interface for sensors
│   │       ├── factories/
│   │       │   └── SensorFactory.psl      # Creates sensor instances
│   │       └── repositories/
│   │           └── SensorRepository.psl   # Sensor data storage
│   ├── common/                           # Minimal shared code (only reusable, non-feature-specific)
│   │   ├── utils/
│   │   │   ├── Logger.psl                # Global logging utility
│   │   │   ├── ConfigLoader.psl          # Configuration loader
│   │   │   └── ConnectionManager.psl     # Connection handling
│   │   └── messaging/
│   │       ├── MessageBroker.psl         # Manages message queue system
│   │       └── EventPublisher.psl        # Publishes events for real-time notifications
├── config/                               # Configuration files
│   ├── application.yml                   # Main application configuration
│   ├── database.yml                      # Database configuration
│   ├── messaging.yml                     # Message broker configuration
│   └── sensors.yml                       # Configuration for sensor parameters
├── tests/                                # Organized by feature
│   ├── warehouse-control/
│   │   ├── UnitTests.psl                 # Unit tests for warehouse control
│   │   └── IntegrationTests.psl          # Integration tests for warehouse feature
│   ├── task-management/
│   │   ├── TaskManagerTest.psl           # Unit tests for TaskManager
│   │   └── TaskIntegrationTest.psl       # Integration tests for task flow
│   ├── robot-orchestration/
│   │   ├── RobotOrchestratorTest.psl     # Unit tests for RobotOrchestrator
│   │   └── RobotIntegrationTest.psl      # Integration tests for robot control
│   ├── monitoring/
│   │   ├── MonitoringServiceTest.psl     # Unit tests for MonitoringService
│   │   └── MonitoringIntegrationTest.psl # Integration tests for monitoring flow
│   └── sensor-management/
│       ├── SensorManagerTest.psl         # Unit tests for SensorManager
│       └── SensorIntegrationTest.psl     # Integration tests for sensor interactions
└── deploy/                               # Deployment configurations and scripts
    ├── docker-compose.yml                # Docker setup for deployment
    ├── kubernetes/
    │   ├── warehouse-deployment.yml      # Kubernetes deployment config
    │   └── services.yml                  # Kubernetes services configuration
    └── scripts/
        ├── init-db.psl                   # Script to initialize database schema
        ├── deploy-robots.psl             # Deployment script for robots
        └── cleanup.psl                   # Script for cleaning up deployment

```

**Using CORE, project organization becomes intuitive, dependencies are clear, and scalability is embedded by design. Each module’s role is evident, and encapsulation is achieved naturally without complex class hierarchies.**

---

## **The Standard Way: Craftsmanship through Standards**

**The Standard Way takes inspiration from craftsmanship, not in pursuit of perfection but in pursuit of standards. Like creating a functional, well-built chair, The Standard Way defines clear, achievable criteria for "work done" in code. In software, “done” isn’t just functional code—it’s code that is structured, intentional, and meets agreed-upon standards for quality and maintainability.**

**The Standard Way guides developers to:**

* **Organize "floating instructions" into functions that communicate their purpose clearly.**  
* **Create clean function boundaries that make code easy to read and maintain.**  
* **Prioritize balance between high standards and practical timelines, so that quality is achievable without unnecessary complexity.**

**This approach ensures that software development remains efficient and that code quality meets a shared standard, making it both professional and practical.**

---

## **Getting Started with CORE**

1. [**Quick-Start Guide**](https://github.com/adico1/standardized-folder-structure-whitepaper/blob/feat/CORE/quick-start-guide.md)**: Set up your project with CORE’s foundational structure.**  
2. [**White Paper**](https://github.com/adico1/standardized-folder-structure-whitepaper/blob/feat/CORE/white-paper.md)**: Dive deeper into CORE’s guiding principles and architecture.**  
3. [**Migration Guide**](https://github.com/adico1/standardized-folder-structure-whitepaper/blob/feat/CORE/migration-guide.md)**: Transition your existing projects seamlessly to CORE.**

---

## **Why CORE?**

**As software evolves, the limitations of Object-Oriented Programming (OOP) have become more apparent. Modern development trends favor modularity and functional composition, and CORE recognizes the value of structure based on modules and folder organization over complex class hierarchies. For a deeper perspective on this shift, read the article ["Putting the Axe on OOP"](https://adico.tech/blog/2024/10/31/putting-the-axe-on-oop/).**

**CORE embraces the natural progression toward modularity, clear organization, and functional composition. It offers a universal standard adaptable across languages, frameworks, platforms, operating systems, and cloud environments—making it a foundational guide for modern, scalable software development.**

---

## Contributing

We welcome contributions from the community to enhance CORE and its components! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on supporting CORE and expanding its ecosystem.

CORE is an open-source framework, and together, we aim to establish industry-wide standards for clarity, structure, and maintainability in software development.
