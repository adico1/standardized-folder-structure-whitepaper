# Event-Driven Architecture with White Paper Folder Structure

```
event-driven-project/
├── src/
│   ├── shared/ (shrd)
│   │   ├── events/
│   │   │   ├── base-event.ts
│   │   │   └── event-bus.ts
│   │   ├── commands/
│   │   │   └── base-command.ts
│   │   └── infrastructure/
│   │       └── message-broker.ts
│   ├── features/
│   │   ├── user-management/
│   │   │   ├── domain/
│   │   │   │   └── user.entity.ts
│   │   │   ├── events/
│   │   │   │   ├── user-created.event.ts
│   │   │   │   └── user-updated.event.ts
│   │   │   ├── commands/
│   │   │   │   ├── create-user.command.ts
│   │   │   │   └── update-user.command.ts
│   │   │   ├── handlers/
│   │   │   │   ├── user-command.handler.ts
│   │   │   │   └── user-event.handler.ts
│   │   │   └── services/
│   │   │       └── user.service.ts
│   │   └── order-processing/
│   │       ├── domain/
│   │       │   └── order.entity.ts
│   │       ├── events/
│   │       │   ├── order-created.event.ts
│   │       │   └── order-shipped.event.ts
│   │       ├── commands/
│   │       │   ├── create-order.command.ts
│   │       │   └── ship-order.command.ts
│   │       ├── handlers/
│   │       │   ├── order-command.handler.ts
│   │       │   └── order-event.handler.ts
│   │       └── services/
│   │           └── order.service.ts
│   └── main/
│       └── app.ts
├── tests/
│   ├── unit/
│   └── integration/
└── package.json

This structure incorporates event-driven principles while maintaining feature-centric organization:

1. **Shared Events and Commands**: Common event and command base classes in the `shared` folder.
2. **Feature-specific Events and Commands**: Each feature has its own events and commands.
3. **Handlers**: Each feature has command and event handlers.
4. **Services**: Business logic is encapsulated in services within each feature.

The `shared` folder contains the event bus and message broker infrastructure, which are used across all features.
