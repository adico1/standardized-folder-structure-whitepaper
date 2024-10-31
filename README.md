# CORE: A Standardized Framework for Software Development

**CORE** is a comprehensive framework designed to standardize software development through principles of **modularity, encapsulation, and consistent coding practices**. CORE aims to create a unified structure that fosters readability, scalability, and maintainability across all aspects of software projects, empowering teams to write clear, structured, and resilient code.

CORE is built around two key components:
1. **EMF (Encapsulated Modular Framework)**: A structural guide for organizing code into self-contained, modular units with well-defined boundaries, single-direction dependencies, and encapsulated logic.
2. **TSW (The Standard Way)**: A set of coding best practices that ensures consistency, readability, and abstraction across codebases. TSW provides standards for function clarity, naming conventions, and abstraction of low-level instructions.

Together, these components define **CORE as a complete framework** that developers can use to achieve high-quality, standardized software design.

---

## Key Components of CORE

### 1. EMF (Encapsulated Modular Framework)
The **Encapsulated Modular Framework (EMF)** provides a structural foundation for organizing code into modules with clear boundaries and responsibilities. EMF emphasizes:

- **Modularity**: Each feature or functionality is encapsulated within self-contained modules.
- **Single-Directional Dependencies**: Dependencies flow in a single direction from high-level to low-level modules, avoiding circular dependencies.
- **Public/Private Interface Control**: Modules expose only essential functions through controlled interfaces (e.g., `index.o` files), keeping internal logic hidden.
- **Configuration Management**: Build configurations are managed at the project root, while application-level configurations are encapsulated at the feature level or centralized in `src/main`.

### 2. TSW (The Standard Way)
**The Standard Way (TSW)** defines best practices for writing clear, maintainable code that aligns with the principles of EMF. Key elements of TSW include:

- **Abstraction of Low-Level Instructions**: Low-level operations should be abstracted into functions to improve readability and reusability.
- **Function Readability and Marking**: Functions should be self-explanatory, with clear naming. Stateful functions and async functions should be prefixed for clarity.
- **Standardized Naming and Style**: Consistent naming conventions, formatting, and comments ensure cohesive code across the entire codebase.
- **Private Function Testing**: Unit testing can access both private and public functions to support robust, complete testing practices.

---

## Getting Started

1. **Read the [introduction](docs/introduction.md)** to understand CORE’s principles and how it fosters modular, maintainable, and consistent software design.
2. **Explore [EMF guidelines](docs/EMF_guidelines.md)** to learn about structuring your project with modularity and encapsulation at its core.
3. **Follow [TSW guidelines](docs/TSW_guidelines.md)** to implement best coding practices in line with CORE’s standards.

For detailed examples, check out the [examples](docs/examples/) folder.

---

## Contributing

We welcome contributions from the community to enhance CORE and its components! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on supporting CORE and expanding its ecosystem.

CORE is an open-source framework, and together, we aim to establish industry-wide standards for clarity, structure, and maintainability in software development.
