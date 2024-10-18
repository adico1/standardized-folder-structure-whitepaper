# Hexagonal Architecture with White Paper Folder Structure

```
hexagonal-project/
├── src/
│   ├── shared/ (shrd)
│   │   ├── domain/
│   │   │   └── value-objects/
│   │   │       └── money.ts
│   │   ├── application/
│   │   │   └── ports/
│   │   │       ├── repository.interface.ts
│   │   │       └── notification.interface.ts
│   │   └── infrastructure/
│   │       └── adapters/
│   │           ├── database-adapter.ts
│   │           └── email-adapter.ts
│   ├── features/
│   │   ├── user-management/
│   │   │   ├── domain/
│   │   │   │   ├── user.entity.ts
│   │   │   │   └── user-repository.interface.ts
│   │   │   ├── application/
│   │   │   │   ├── ports/
│   │   │   │   │   └── user-service.interface.ts
│   │   │   │   └── use-cases/
│   │   │   │       ├── create-user.use-case.ts
│   │   │   │       └── get-user.use-case.ts
│   │   │   └── infrastructure/
│   │   │       ├── adapters/
│   │   │       │   └── user-repository.adapter.ts
│   │   │       └── controllers/
│   │   │           └── user.controller.ts
│   │   └── order-processing/
│   │       ├── domain/
│   │       │   ├── order.entity.ts
│   │       │   └── order-repository.interface.ts
│   │       ├── application/
│   │       │   ├── ports/
│   │       │   │   └── order-service.interface.ts
│   │       │   └── use-cases/
│   │       │       ├── create-order.use-case.ts
│   │       │       └── process-payment.use-case.ts
│   │       └── infrastructure/
│   │           ├── adapters/
│   │           │   ├── order-repository.adapter.ts
│   │           │   └── payment-gateway.adapter.ts
│   │           └── controllers/
│   │               └── order.controller.ts
│   └── main/
│       └── app.ts
├── tests/
│   ├── unit/
│   └── integration/
└── package.json

This structure maintains the feature-centric organization and shared resources while incorporating the key elements of Hexagonal Architecture:

1. **Domain**: Contains business logic and entities.
2. **Application**: Houses use cases and defines ports (interfaces).
3. **Infrastructure**: Implements adapters and controllers.

The `shared` folder contains common elements used across features, while each feature has its own hexagonal structure.
