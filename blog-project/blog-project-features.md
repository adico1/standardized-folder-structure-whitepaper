# Feature Implementation

1. User Authentication Feature (src/features/auth/):

   ```typescript
   // src/features/auth/auth.controller.ts
   import { Request, Response } from 'express';
   import bcrypt from 'bcrypt';
   import User from '../../shared/models/user.model';
   import { generateToken } from '../../shared/utils/auth.util';

   export const register = async (req: Request, res: Response) => {
     try {
       const { username, email, password } = req.body;
       const hashedPassword = await bcrypt.hash(password, 10);
       const user = new User({ username, email, password: hashedPassword });
       await user.save();
       res.status(201).json({ message: 'User registered successfully' });
     } catch (error) {
       res.status(500).json({ message: 'Error registering user' });
     }
   };

   export const login = async (req: Request, res: Response) => {
     try {
       const { email, password } = req.body;
       const user = await User.findOne({ email });
       if (!user || !(await bcrypt.compare(password, user.password))) {
         return res.status(401).json({ message: 'Invalid credentials' });
       }
       const token = generateToken(user);
       res.json({ token });
     } catch (error) {
       res.status(500).json({ message: 'Error logging in' });
     }
   };

   // src/features/auth/auth.routes.ts
   import express from 'express';
   import * as authController from './auth.controller';

   const router = express.Router();

   router.post('/register', authController.register);
   router.post('/login', authController.login);

   export default router;
   ```

2. Post Management Feature (src/features/posts/):

   ```typescript
   // src/features/posts/post.controller.ts
   import { Request, Response } from 'express';
   import Post from '../../shared/models/post.model';

   export const createPost = async (req: Request, res: Response) => {
     try {
       const { title, content } = req.body;
       const post = new Post({ title, content, author: (req as any).userId });
       await post.save();
       res.status(201).json(post);
     } catch (error) {
       res.status(500).json({ message: 'Error creating post' });
     }
   };

   export const getPosts = async (req: Request, res: Response) => {
     try {
       const posts = await Post.find().populate('author', 'username');
       res.json(posts);
     } catch (error) {
       res.status(500).json({ message: 'Error fetching posts' });
     }
   };

   // src/features/posts/post.routes.ts
   import express from 'express';
   import * as postController from './post.controller';
   import { authMiddleware } from '../../shared/middleware/auth.middleware';

   const router = express.Router();

   router.post('/', authMiddleware, postController.createPost);
   router.get('/', postController.getPosts);

   export default router;
   ```
