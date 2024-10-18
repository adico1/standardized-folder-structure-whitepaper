# Domain-Driven Design with White Paper Folder Structure

```
ddd-project/
├── src/
│   ├── shared/ (shrd)
│   │   ├── domain/
│   │   │   ├── value-objects/
│   │   │   │   └── money.ts
│   │   │   └── events/
│   │   │       └── domain-event.ts
│   │   ├── application/
│   │   │   └── interfaces/
│   │   │       └── unit-of-work.interface.ts
│   │   └── infrastructure/
│   │       ├── persistence/
│   │       │   └── base-repository.ts
│   │       └── messaging/
│   │           └── event-dispatcher.ts
│   ├── features/
│   │   ├── user-management/
│   │   │   ├── domain/
│   │   │   │   ├── user.aggregate.ts
│   │   │   │   ├── user-repository.interface.ts
│   │   │   │   └── events/
│   │   │   │       └── user-created.event.ts
│   │   │   ├── application/
│   │   │   │   ├── commands/
│   │   │   │   │   └── create-user.command.ts
│   │   │   │   └── handlers/
│   │   │   │       └── create-user.handler.ts
│   │   │   └── infrastructure/
│   │   │       ├── persistence/
│   │   │       │   └── user.repository.ts
│   │   │       └── controllers/
│   │   │           └── user.controller.ts
│   │   └── order-processing/
│   │       ├── domain/
│   │       │   ├── order.aggregate.ts
│   │       │   ├── order-repository.interface.ts
│   │       │   └── events/
│   │       │       └── order-placed.event.ts
│   │       ├── application/
│   │       │   ├── commands/
│   │       │   │   └── place-order.command.ts
│   │       │   └── handlers/
│   │       │       └── place-order.handler.ts
│   │       └── infrastructure/
│   │           ├── persistence/
│   │           │   └── order.repository.ts
│   │           └── controllers/
│   │               └── order.controller.ts
│   └── main/
│       └── app.ts
├── tests/
│   ├── unit/
│   └── integration/
└── package.json
