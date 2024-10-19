# Best Practices Cheat Sheet

This cheat sheet provides a quick reference for key best practices when working with the standardized folder structure.

## General Principles

1. **Feature-Centric Organization**
   - Organize code primarily around features or business domains
   - Keep feature-specific code isolated within its feature directory

2. **Shared Resources Management**
   - Use `shared/` directory for truly common code and utilities
   - Avoid over-populating `shared/`; if in doubt, keep it feature-specific

3. **Clear Separation of Concerns**
   - Maintain clear boundaries between different features
   - Separate business logic from infrastructure concerns

4. **Consistency**
   - Follow consistent naming conventions across the project
   - Maintain similar internal structures for each feature

5. **Scalability**
   - Design with growth in mind; make it easy to add new features
   - Keep feature directories focused and avoid deep nesting

## Directory Structure Best Practices

```
project-root/
├── src/
│   ├── shared/ (shrd)
│   │   ├── utils/
│   │   ├── services/
│   │   └── models/
│   ├── features/
│   │   └── [feature-name]/
│   │       ├── components/
│   │       ├── services/
│   │       └── models/
│   └── main/
├── tests/
│   ├── unit/
│   └── integration/
└── [config files]
```

- Keep `shared/` flat; avoid creating deep subdirectories
- Mirror the `src/` structure in `tests/` for easy navigation
- Place configuration files at the root level

## Coding Best Practices

1. **Imports**
   - Use absolute imports from `src/` root
   - Avoid circular dependencies between features

2. **Naming Conventions**
   - Use clear, descriptive names for directories and files
   - Prefix shared utilities with `use` for hooks or `is` for boolean checks

3. **Code Organization**
   - Keep files focused and small (< 300 lines as a general rule)
   - Use index files to simplify imports from feature directories

4. **Testing**
   - Write unit tests for all business logic
   - Place tests next to the code they're testing
   - Use integration tests to verify feature interactions

5. **Documentation**
   - Include a README.md in each feature directory explaining its purpose
   - Use JSDoc or similar for documenting functions and classes

## Version Control Best Practices

1. **Commits**
   - Make small, focused commits
   - Use conventional commit messages (e.g., "feat:", "fix:", "refactor:")

2. **Branching**
   - Use feature branches for new features or major changes
   - Keep feature branches short-lived and up-to-date with main

3. **Pull Requests**
   - Review for adherence to the folder structure and coding standards
   - Ensure new features follow the established patterns

## Refactoring and Maintenance

1. **Regular Reviews**
   - Periodically review `shared/` for unnecessary code
   - Look for opportunities to extract common code from features

2. **Performance**
   - Profile and optimize critical paths within features
   - Be cautious of over-optimization; maintain readability

3. **Deprecation**
   - Clearly mark deprecated code and plan for removal
   - Use feature flags for gradual rollout and easy rollback

## Collaboration

1. **Knowledge Sharing**
   - Conduct regular code reviews to spread knowledge
   - Document architectural decisions and rationales

2. **Onboarding**
   - Maintain up-to-date documentation on the folder structure
   - Create onboarding guides for new team members

By following these best practices, you'll maintain a clean, scalable, and maintainable codebase that aligns with the principles of the standardized folder structure.
