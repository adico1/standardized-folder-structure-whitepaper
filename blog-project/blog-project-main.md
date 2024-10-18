# Main Application Implementation

1. Create the main application file (src/main/app.ts):

   ```typescript
   import express from 'express';
   import mongoose from 'mongoose';
   import dotenv from 'dotenv';
   import authRoutes from '../features/auth/auth.routes';
   import postRoutes from '../features/posts/post.routes';

   dotenv.config();

   const app = express();
   const PORT = process.env.PORT || 3000;

   app.use(express.json());

   // Connect to MongoDB
   mongoose.connect(process.env.MONGODB_URI!)
     .then(() => console.log('Connected to MongoDB'))
     .catch((err) => console.error('MongoDB connection error:', err));

   // Routes
   app.use('/api/auth', authRoutes);
   app.use('/api/posts', postRoutes);

   app.listen(PORT, () => {
     console.log(`Server is running on port ${PORT}`);
   });

   export default app;
   ```

2. Update package.json scripts:

   ```json
   "scripts": {
     "start": "node dist/main/app.js",
     "dev": "ts-node-dev src/main/app.ts",
     "build": "tsc"
   }
   ```
