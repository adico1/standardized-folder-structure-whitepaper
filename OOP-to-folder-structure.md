# The Shift from OOP to Procedural: Embracing a Standardized Universal Folder Structure

In the ever-evolving landscape of software development, paradigms and methodologies continuously adapt to meet the demands of modern applications. While object-oriented programming (OOP) has long been a dominant force, a growing trend towards procedural programming with a standardized folder structure is emerging. This article explores the reasons behind this shift and the benefits of adopting a procedural approach with a universal folder structure.

## The Limitations of OOP

Object-oriented programming has been a staple in software development for decades, offering benefits such as encapsulation, inheritance, and polymorphism. However, as applications grow in complexity, several limitations of OOP have become apparent:

1. **Complexity and Overhead**: OOP can introduce unnecessary complexity, especially in large codebases where deep inheritance hierarchies and extensive use of polymorphism can make the code difficult to understand and maintain.

2. **Tight Coupling**: The interdependencies between classes can lead to tight coupling, making it challenging to modify or extend individual components without affecting others.

3. **Performance Concerns**: The abstraction layers in OOP can introduce performance overhead, which may not be suitable for performance-critical applications.

4. **Over-Architecture**: OOP often leads to over-architecting solutions, where the focus on inheritance and abstraction can result in overly complex designs that are hard to manage.

## The Rise of Procedural Programming

In response to these limitations, many developers are turning to procedural programming, which emphasizes simplicity and directness. Procedural programming focuses on writing clear, straightforward code that is easy to read and maintain. This approach is complemented by a standardized universal folder structure that promotes modularity and reusability.

### Key Benefits of Procedural Programming

1. **Simplicity**: Procedural code is often more straightforward, with a clear flow of execution that is easy to follow. This simplicity reduces the cognitive load on developers and makes the codebase more accessible.

2. **Modularity**: By organizing code into distinct modules, procedural programming encourages separation of concerns. Each module encapsulates specific functionality, promoting reusability and simplifying maintenance.

3. **Performance**: Procedural code can be more performant, as it avoids the overhead associated with object creation and method dispatch in OOP.

4. **Composition Over Inheritance**: Procedural programming naturally favors composition over inheritance. This principle allows for more flexible and maintainable code by combining simple functions and modules rather than relying on complex inheritance hierarchies.

## Comparisson between OOP and universal folder structure

### Diagram Presenting the native strength of OOP
<img width="751" alt="image" src="https://github.com/user-attachments/assets/3a15f6b9-ce6c-4f90-90b8-3059341893e6">

### Diagram Presenting the native strength of OOP using the universal folder structure and procedural code
<img width="979" alt="image" src="https://github.com/user-attachments/assets/e08aa5ac-4251-4d86-962e-62aeb2932848">

## The Standardized Universal Folder Structure

A key aspect of the procedural paradigm is the adoption of a standardized folder structure that organizes code into logical components. This structure enhances clarity and maintainability, making it easier for developers to navigate and understand the codebase.

### Example Folder Structure

```

src/
  server/                  # Server application
    connection_handler/
      connection_handler.s
      connection_handler_macro.s
      messages.s
    socket/
      setup_socket.s
      setup_socket_macro.s
    shared/
      constants.s
    error_handler/
      error_handler.s
      messages.s
  studio/                  # Studio application
    common/                # Common utilities or resources
    features/
      shared/              # Shared components across features
        field/             # Shared field components
          field.s
        primitive_field/   # Shared primitive field components
          primitive_field.s
        layout_field/      # Shared layout field components
          layout_field.s
      canvas/              # Canvas feature
        canvas.s
      fields/              # Specific field features
        text_field/        # Text field feature
          text_field.s
        column/            # Column field feature
          column.s
  main.s
  shared/
    macros.s
```

### Advantages of the Universal Folder Structure

1. **Clear Separation of Concerns**: The folder structure clearly delineates different components and features, making it easy to locate and modify specific parts of the codebase.

2. **Reusability**: Shared components are organized in a way that promotes reuse across different features or applications, reducing duplication and enhancing consistency.

3. **Scalability**: As the project grows, the standardized structure provides a scalable framework that can accommodate new features and components without becoming unwieldy.

4. **Encapsulation through Structure**: Encapsulation is achieved through careful folder structure management, which is more flexible than code-based encapsulation.

5. **Solving Reusability with Composition**: While OOP uses inheritance to solve reusability, procedural programming uses composition, which avoids the pitfalls of over-abstraction and over-architecture.

## Conclusion

The shift from OOP to procedural programming with a standardized universal folder structure represents a significant evolution in software development. By embracing simplicity, modularity, and performance, developers can create maintainable and scalable applications that meet the demands of modern software. This approach not only addresses the limitations of OOP but also provides a clear path forward for building robust and efficient systems. By preferring composition over inheritance, procedural programming offers a more flexible and maintainable way to achieve reusability and encapsulation.