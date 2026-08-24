# Web Dev Study Notes: RESTful API Principles & Express.js Middleware Architecture

## 1. RESTful API Design Principles

REpresentational State Transfer (REST) is an architectural style for building scalable web services.

### Core Constraints

1. **Client-Server Separation:** UI concerns are isolated from data storage concerns.
2. **Statelessness:** Every HTTP request contains all necessary context; server stores no client session state between requests.
3. **Cacheability:** Responses must explicitly indicate cacheability to prevent client stale-data errors.
4. **Uniform Interface:** Standard HTTP Verbs (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) and standard HTTP status codes (`200 OK`, `201 Created`, `400 Bad Request`, `401 Unauthorized`, `404 Not Found`, `500 Internal Error`).

---

## 2. Express.js Middleware Pipeline Architecture

Middleware functions have access to the Request object (`req`), Response object (`res`), and the `next` function.

### Layered Pipeline Pattern

```
Incoming Request
      │
      ▼
┌───────────────────────────────┐
│ Global Logger / CORS          │
└──────────────┬────────────────┘
               │ next()
               ▼
┌───────────────────────────────┐
│ Authentication Middleware     │
└──────────────┬────────────────┘
               │ next()
               ▼
┌───────────────────────────────┐
│ Route Controller Logic        │
└──────────────┬────────────────┘
               │ res.json() or next(err)
               ▼
┌───────────────────────────────┐
│ Central Error Handler         │
└───────────────────────────────┘
```

### Modular Express Architecture Example

```typescript
import express, { Request, Response, NextFunction } from 'express';

const app = express();
app.use(express.json());

// 1. Logging Middleware
app.use((req: Request, _res: Response, next: NextFunction) => {
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);
  next();
});

// 2. Controller Handler
app.get('/api/v1/resource', (req: Request, res: Response) => {
  res.status(200).json({ success: true, data: [] });
});

// 3. Centralized Error-Handling Middleware (4 parameters)
app.use((err: Error, _req: Request, res: Response, _next: NextFunction) => {
  console.error('[Error Middleware]:', err.stack);
  res.status(500).json({
    success: false,
    message: err.message || 'Internal Server Error',
  });
});
```
