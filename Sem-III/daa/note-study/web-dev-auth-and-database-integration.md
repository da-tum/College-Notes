# Web Dev Study Notes: Database Integration, JWT Authentication & Security

## 1. Database Integration Models (ORM vs Query Builders)

| Approach | Technology Example | Pros | Cons |
|---|---|---|---|
| **Raw Drivers** | `pg`, `mongodb` driver | Maximum execution speed & query control | Manual SQL string concatenation, injection risk |
| **Query Builders** | `Knex.js`, `Kysely` | Programmatic SQL building, type safety | Low abstraction over raw tables |
| **Object-Relational Mappers (ORM)** | `Prisma`, `TypeORM`, `Mongoose` | High productivity, migration management, relational graph fetching | Potential N+1 query overhead if unoptimized |

---

## 2. JWT Authentication & Password Security Flow

JSON Web Tokens (JWT) enable stateless user authentication.

### Token Architecture

A JWT consists of three base64-url encoded parts separated by dots (`.`):
$$\text{Header} . \text{Payload} . \text{Signature}$$

- **Header:** Specifies algorithm (`HS256`, `RS256`) and token type (`JWT`).
- **Payload:** User claims (`sub`, `username`, `role`, `iat`, `exp`).
- **Signature:** Created by hashing $\text{Header} + \text{Payload}$ with a server secret key.

```
Client                             Server
  │                                  │
  ├────── POST /api/auth/login ─────►│ (Validate password with bcrypt)
  │       (credentials)              │
  │                                  │
  │◄───── 200 OK + JWT Token ────────┤ (Sign token with SECRET_KEY)
  │       (stored in HTTP-Only cookie)│
  │                                  │
  ├────── GET /api/protected ───────►│ (Verify token signature & expiration)
  │       Header: Bearer <token>     │
  │                                  │
  │◄───── 200 OK + Data ─────────────┤
```

---

## 3. Best Practices in Web Security

1. **Password Hashing:** Always salt and hash passwords using **bcrypt** or **argon2** (never store plaintext or simple MD5/SHA256 hashes).
2. **XSS & CSRF Prevention:** Store access tokens in `HttpOnly`, `SameSite=Strict`, `Secure` cookies to prevent client-side JavaScript theft.
3. **CORS Hardening:** Restrict cross-origin resource sharing to trusted domain origins.
