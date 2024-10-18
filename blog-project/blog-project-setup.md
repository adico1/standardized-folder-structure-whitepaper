# Blog Project Setup

1. Initialize a new Node.js project:
   ```
   mkdir blog-project
   cd blog-project
   npm init -y
   ```

2. Install necessary dependencies:
   ```
   npm install express mongoose bcrypt jsonwebtoken dotenv
   npm install --save-dev typescript @types/express @types/mongoose @types/bcrypt @types/jsonwebtoken
   ```

3. Create the initial folder structure:
   ```
   blog-project/
   ├── src/
   │   ├── shared/ (shrd)
   │   ├── features/
   │   └── main/
   ├── tests/
   │   ├── unit/
   │   └── integration/
   ├── package.json
   └── tsconfig.json
   ```

4. Configure TypeScript (tsconfig.json):
   ```json
   {
     "compilerOptions": {
       "target": "es6",
       "module": "commonjs",
       "outDir": "./dist",
       "rootDir": "./src",
       "strict": true,
       "esModuleInterop": true
     },
     "include": ["src/**/*"],
     "exclude": ["node_modules", "**/*.spec.ts"]
   }
   ```

5. Create a .env file for environment variables:
   ```
   PORT=3000
   MONGODB_URI=mongodb://localhost:27017/blog_db
   JWT_SECRET=your_secret_key
   ```
