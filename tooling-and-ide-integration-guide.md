# Tooling and IDE Integration Guide

This guide provides instructions on how to configure popular Integrated Development Environments (IDEs) and development tools to work optimally with the proposed standardized folder structure.

## Visual Studio Code

1. **Workspace Settings**:
   Create a `.vscode/settings.json` file in your project root:

   ```json
   {
     "files.exclude": {
       "**/node_modules": true,
       "**/dist": true
     },
     "search.exclude": {
       "**/node_modules": true,
       "**/dist": true
     },
     "files.associations": {
       "*.js": "javascript",
       "*.jsx": "javascriptreact",
       "*.ts": "typescript",
       "*.tsx": "typescriptreact"
     }
   }
   ```

2. **Extensions**:
   - Install "Project Manager" extension for easy navigation between features.
   - Use "Todo Tree" extension to track TODOs across the project.

3. **Custom Explorer Groups**:
   Add to `.vscode/settings.json`:

   ```json
   {
     "explorer.experimental.fileNesting.enabled": true,
     "explorer.experimental.fileNesting.expand": false,
     "explorer.experimental.fileNesting.patterns": {
       "*.ts": "${capture}.test.ts,${capture}.spec.ts",
       "*.js": "${capture}.test.js,${capture}.spec.js"
     }
   }
   ```

## JetBrains IDEs (IntelliJ IDEA, WebStorm, PyCharm)

1. **Project Structure**:
   - Right-click on `src` folder > Mark Directory as > Sources Root
   - Right-click on `tests` folder > Mark Directory as > Test Sources Root

2. **Custom Scopes**:
   - Go to Settings/Preferences > Scopes
   - Create scopes for each feature and shared resources

3. **File Templates**:
   - Go to Settings/Preferences > Editor > File and Code Templates
   - Create templates for feature-specific files (e.g., services, controllers)

4. **Live Templates**:
   - Go to Settings/Preferences > Editor > Live Templates
   - Create snippets for common patterns in your structure

## Eclipse

1. **Project Explorer View**:
   - Right-click on the project > Properties > Resource > Resource Filters
   - Add filters to exclude `node_modules` and `dist` folders

2. **Working Sets**:
   - Create working sets for each feature and shared resources

3. **Code Templates**:
   - Go to Window > Preferences > [Language] > Code Style > Code Templates
   - Create templates for feature-specific files

## Git Configuration

1. **Gitignore**:
   Add to your `.gitignore` file:

   ```
   node_modules/
   dist/
   *.log
   .env
   ```

2. **Git Attributes**:
   Create a `.gitattributes` file:

   ```
   * text=auto eol=lf
   *.{cmd,[cC][mM][dD]} text eol=crlf
   *.{bat,[bB][aA][tT]} text eol=crlf
   ```

## ESLint Configuration

For JavaScript/TypeScript projects, create an `.eslintrc.js` file:

```javascript
module.exports = {
  root: true,
  parser: '@typescript-eslint/parser',
  plugins: ['@typescript-eslint'],
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
  ],
  rules: {
    // Add custom rules here
  },
};
```

## Prettier Configuration

Create a `.prettierrc` file:

```json
{
  "singleQuote": true,
  "trailingComma": "es5",
  "printWidth": 100
}
```

## VS Code Tasks

Create a `.vscode/tasks.json` file for common tasks:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "type": "npm",
      "script": "test",
      "group": "test",
      "problemMatcher": ["$tsc"]
    },
    {
      "type": "npm",
      "script": "build",
      "group": "build",
      "problemMatcher": ["$tsc"]
    }
  ]
}
```

## Docker Integration

If using Docker, create a `.dockerignore` file:

```
node_modules
npm-debug.log
Dockerfile
.dockerignore
.git
.gitignore
README.md
```

These configurations will help ensure that your development environment is optimized for the proposed folder structure, improving productivity and maintaining consistency across your team.
