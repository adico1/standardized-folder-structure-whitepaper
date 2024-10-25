# CORE: Comprehensive, Organized Repository for Engineering

Welcome to **CORE**, a meticulously designed framework intended to elevate software engineering through organized, dependency-driven architecture. Inspired by the *Dao* of Software Engineering, CORE represents the ideal of a **standardized, modular folder structure** (also known as **Dependency-Driven Folder Structure** or DDFS) that simplifies collaboration, scales effortlessly, and aligns with modern CI/CD practices. The CORE structure fosters **predictable, comparable, and estimable software development** by creating a path towards organization, clarity, and efficiency.

![DAO Symbol - The Way of Software Engineering](./assets/dao-symbol.png)
*Embrace the Standard Way: The Dao of Software Engineering*

---

## 📜 Overview of the Repository

This repository is a practical implementation of the **CORE** approach to software structuring, emphasizing the “Standard Way” that aligns with software engineering principles for simplicity, modularity, and scalability.

Key concepts and contents include:
- **CORE Architecture**: Comprehensive and organized structure across all functional areas
- **The Standard Way (Dao of Software Engineering)**: Leading to software that is predictable, comparable, and estimable
- **DDFS / SMFS**: A modular, dependency-driven folder structure for the future of scalable software

---

## 📂 Repository Structure

### Directory Flowchart

Below is a flowchart of the CORE architecture’s folder hierarchy, illustrating key dependencies and organization. This dependency-driven structure allows for clear boundaries between modules, scalable feature management, and optimized collaboration.

\\```mermaid
flowchart TD
    A[Project Root] --> B[src]
    A --> C[config]
    A --> D[tests]
    A --> E[deploy]
    B --> B1[main]
    B --> B2[features]
    B --> B3[common]
    B2 --> B2a[feature1]
    B2 --> B2b[feature2]
    C --> C1[development]
    C --> C2[production]
    D --> D1[unit tests]
    D --> D2[integration tests]
    E --> E1[docker]
    E --> E2[kubernetes]
    E --> E3[deployment scripts]
\\```

### Folder Explanations

- **src/**: Main source code for the application, organized into:
    - `main/`: Core files for application start-up and primary execution.
    - `features/`: Modular directories for each feature (e.g., `feature1`, `feature2`), allowing isolated development and testing.
    - `common/`: Shared utilities and components used across multiple features.
- **config/**: Houses environment-specific configuration files:
    - `development/`: Configs for development environments.
    - `production/`: Configs for production environments.
- **tests/**: Contains all test files, with separate directories for:
    - `unit tests/`: Unit testing for isolated functions.
    - `integration tests/`: Testing for multi-module interactions.
- **deploy/**: Holds deployment-related resources, including:
    - `docker/`: Docker configurations.
    - `kubernetes/`: Kubernetes configurations.
    - `deployment scripts/`: Custom deployment scripts.

---

## 🌟 CORE Principles and Benefits

### 1. **The Standard Way (Dao of Software)**: Predictable, Comparable, Estimable
   * Following “The Way” (道) in software means adopting a repeatable, modular structure that fosters consistent results. The CORE approach is designed to create software that is:
      - **Predictable**: Each module’s responsibility and behavior are clearly defined.
      - **Comparable**: Modules follow uniform design, making it easy to compare functionality.
      - **Estimable**: Clear boundaries and responsibilities facilitate accurate time and cost estimates.
   * This is inspired by the Daoist principle of a balanced, natural path, leading to smooth workflows and minimal rework.

### 2. **DDFS (Dependency-Driven Folder Structure)**: Cornerstone for Future Development
   * DDFS organizes the project based on dependencies, allowing teams to isolate features, scale with confidence, and manage change effectively.
   * By isolating dependencies, the structure supports CI/CD integrations and seamless module-based collaboration, essential for distributed teams or large projects.

### 3. **Scalable and Team-Friendly**: Designed for flexibility, the CORE structure promotes clean modularization and prevents code overlap, reducing merge conflicts in team environments.

---

## 🔍 Exploring the Repository

### Quickstart Guide

1. **Understand the Structure**: Begin by reviewing the [Folder Flowchart](#folder-hierarchy-flowchart) above and folder explanations to get a sense of the architecture.
2. **Examples Directory**: Navigate to the `examples/` directory for a collection of demo applications structured with CORE.
3. **Documentation**:
    - **White Paper**: For a deeper dive, see the [white-paper.md](./white-paper.md) file, which explains the theoretical foundation of CORE and how it applies to enterprise-scale projects.
    - **Quick-Start Guide**: A simple guide on setting up the CORE structure in new or existing projects.
    - **Migration Guide**: Step-by-step guide to refactor a project into CORE, minimizing disruption and streamlining the transition.

### Repository Structure Overview

**Before-and-After Comparison**: This repository includes refactored project examples. Here’s a simplified view of the transformation from a monolithic structure to the CORE structure.

#### **Before** (Monolithic)
\\```plaintext
project-root/
├── app.js
├── config.js
├── controllers/
├── models/
├── views/
└── tests/
\\```

#### **After** (CORE Structure)
\\```plaintext
project-root/
├── src/
│   ├── main/
│   ├── features/
│   └── common/
├── config/
├── tests/
└── deploy/
\\```

---

## 🛠️ Setting Up CI/CD with CORE

Below is a sample GitHub Actions workflow that integrates testing within the CORE structure. This setup demonstrates how easily CORE aligns with CI/CD automation.

\\```yaml
# GitHub Actions Workflow
name: CI/CD Pipeline

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Install dependencies
        run: npm install

      - name: Run tests
        run: npm test --prefix tests/
\\```

---

## 📖 Additional Resources and Documentation

1. **[White Paper](./white-paper.md)**: In-depth look at CORE’s theoretical foundations and practical applications.
2. **[Quick-Start Guide](./quick-start-guide.md)**: Step-by-step instructions for implementing the CORE structure in new projects.
3. **[Migration Guide](./migration-guide.md)**: Guide for transitioning existing projects into the CORE structure.
4. **[FAQ Document](./faq-document.md)**: Answers to common questions and troubleshooting.

---

## 🌏 Join the CORE Community

Whether you’re just starting with modular development or looking to optimize an enterprise application, the CORE structure offers a pathway to efficiency and consistency. Connect with other developers on GitHub Discussions, and feel free to contribute improvements or share feedback. Embrace *The Standard Way* and help shape the future of scalable software development!

