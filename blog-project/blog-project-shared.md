# Shared Resources Implementation

1. Create shared models (src/shared/models/):

   ```typescript
   // src/shared/models/user.model.ts
   import mongoose, { Document, Schema } from 'mongoose';

   export interface IUser extends Document {
     username: string;
     email: string;
     password: string;
   }

   const UserSchema: Schema = new Schema({
     username: { type: String, required: true, unique: true },
     email: { type: String, required: true, unique: true },
     password: { type: String, required: true }
   });

   export default mongoose.model<IUser>('User', UserSchema);

   // src/shared/models/post.model.ts
   import mongoose, { Document, Schema } from 'mongoose';

   export interface IPost extends Document {
     title: string;
     content: string;
     author: mongoose.Types.ObjectId;
   }

   const PostSchema: Schema = new Schema({
     title: { type: String, required: true },
     content: { type: String, required: true },
     author: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true }
   });

   export default mongoose.model<IPost>('Post', PostSchema);
   ```

2. Create shared utilities (src/shared/utils/):

   ```typescript
   // src/shared/utils/auth.util.ts
   import jwt from 'jsonwebtoken';
   import { IUser } from '../models/user.model';

   export const generateToken = (user: IUser): string => {
     return jwt.sign({ id: user._id }, process.env.JWT_SECRET!, { expiresIn: '1d' });
   };

   export const verifyToken = (token: string): any => {
     return jwt.verify(token, process.env.JWT_SECRET!);
   };
   ```

3. Create shared middleware (src/shared/middleware/):

   ```typescript
   // src/shared/middleware/auth.middleware.ts
   import { Request, Response, NextFunction } from 'express';
   import { verifyToken } from '../utils/auth.util';

   export const authMiddleware = (req: Request, res: Response, next: NextFunction) => {
     const token = req.header('Authorization')?.replace('Bearer ', '');

     if (!token) {
       return res.status(401).json({ message: 'No token provided' });
     }

     try {
       const decoded = verifyToken(token);
       (req as any).userId = decoded.id;
       next();
     } catch (error) {
       res.status(401).json({ message: 'Invalid token' });
     }
   };