# Mobile App Development Structure

```
mobile-app/
├── src/
│   ├── shared/ (shrd)
│   │   ├── models/
│   │   │   └── user.ts
│   │   ├── utils/
│   │   │   └── formatting.ts
│   │   └── services/
│   │       └── api.service.ts
│   ├── features/
│   │   ├── authentication/
│   │   │   ├── screens/
│   │   │   │   ├── LoginScreen.tsx
│   │   │   │   └── RegisterScreen.tsx
│   │   │   └── services/
│   │   │       └── auth.service.ts
│   │   ├── profile/
│   │   │   ├── screens/
│   │   │   │   └── ProfileScreen.tsx
│   │   │   └── services/
│   │   │       └── profile.service.ts
│   │   └── messaging/
│   │       ├── screens/
│   │       │   └── ChatScreen.tsx
│   │       └── services/
│   │           └── chat.service.ts
│   └── App.tsx
├── ios/
│   └── // iOS-specific files
├── android/
│   └── // Android-specific files
├── tests/
│   ├── unit/
│   └── integration/
└── package.json

This structure applies the white-paper's principles to a React Native mobile app, showing how to organize shared code and platform-specific implementations.
