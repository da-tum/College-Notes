# Web Development IIINotes

## 06-08-2026

### 1. API & REST Architecture

#### What is an API?

- **API (Application Programming Interface)**: A software intermediary that allows two applications to talk to each other. In web development, we primarily deal with **REST APIs**.
- **REST API (Representational State Transfer)**: A convention based on HTTP by which we can perform CRUD operations over the internet.
- **Hypertext**: Any text or media containing links to other text/media available on the web.

#### what is node ?

  It is a runtime module for JS.

#### CRUD Operations & HTTP Methods Mapping

CRUD represents the 4 basic functions of persistent storage and how they map to HTTP request methods:

| Operation | Action / Purpose | HTTP Method | Details / Scope |
| :--- | :--- | :--- | :--- |
| **C** - Create | Create new resource / entry | `POST` | Submits payload data to create a new entry on the server |
| **R** - Read | Retrieve / Fetch data | `GET` | Requests data from a specified resource |
| **U** - Update (Full) | Complete resource overwrite | `PUT` | Full update; replaces target resource entirely |
| **U** - Update (Partial) | Modify specific fields | `PATCH` | Partial update; modifies only specified fields |
| **D** - Delete | Delete resource / action | `DELETE` | Removes the specified resource |

#### Data Exchange Format & Endpoints

- **Data Exchange**: When making API endpoints, data transfer and receiving is handled in **JSON (JavaScript Object Notation)** format.
- **HTTP Request Architecture** consists of 4 main parts:
  1. **Methods**: Tells the server what action to perform (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`).
  2. **URL (Endpoint)**: The target web address/path where the request is sent.
  3. **Header**: Extra metadata/information about the request (e.g., `Content-Type: application/json`, Auth tokens).
  4. **Body** *(Optional)*: Contains the actual data payload sent to the server.

---

### 2. Node.js Ecosystem & Package Management

#### Node.js Core Architecture

- **libuv**: Node.js is built on top of **libuv**, a multi-platform C library that powers the event loop and asynchronous I/O operations.

#### NPM (Node Package Manager)

- **NPM**: Utility tool to manage adding, updating, or removing external code packages and libraries.
- **npmjs.com**: The official public registry where Node packages and libraries can be discovered.

#### Steps for Node Project Creation (`npm init`)

1. Open terminal and run: `npm init`
2. Fill out prompts:
   - **Name**: Project name
   - **Version**: Initial version *(auto-filled)*
   - **Description**: Short description
   - **Entry point**: Main execution file *(e.g., `app.js`)*
   - **Author**: Developer name
3. Confirm with `y` or `yes`.
4. A `package.json` file is created, which can also be modified manually later.

#### Package Types & Installation Flags

- **Local Packages**: Installed into a specific project directory (`node_modules/`).
- **Global Packages**: Installed system-wide using the `-g` flag (e.g., `npm install -g nodemon`), making the tool available globally across the command line.

#### Example `package.json`

```json
{
  "name": "myapp",
  "version": "1.0.0",
  "description": "this is my app",
  "license": "ISC",
  "author": "Harsh Dev Jha",
  "type": "commonjs",
  "main": "app.js",
  "scripts": {
    "dev": "nodemon app.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  }
}
```

> **Note**: `nodemon` (Node Monitor) is a library installed via `npm install -g nodemon` that monitors your project directory and automatically restarts the Node.js application whenever file changes are detected.

---

### 3. Node.js Modularization & Module System

#### What is a Module?

- **Module**: A isolated, reusable piece of code.
- **Modularization**: The practice of splitting codebase into separate, dedicated files/modules for better organization, maintainability, and reusability.

#### Types of Modules in Node.js

1. **Self / Internal / Local Modules**:
   - Custom modules created by the developer locally within the project.
   - Example: Local utility files imported via `require('./myModule')`.

2. **Core Modules**:
   - Native built-in modules provided by Node.js in its own ecosystem.
   - Must be explicitly imported using `require()` before use.
   - Examples: `fs` (File System), `http`, `path`, `os`, `events`, `crypto`.

3. **External / Third-Party Modules**:
   - Community packages installed from `npmjs.com` via `npm install`.
   - Examples: `express`, `nodemon`, `cors`, `dotenv`.

#### CommonJS Module Import & Export Syntax

Node.js uses CommonJS syntax by default:

- **Importing Modules**: Use the `require()` function.

  ```javascript
  const fs = require('fs'); // Core module
  const express = require('express'); // External module
  const myModule = require('./myModule'); // Local module
  ```

- **Exporting Modules**: Use `module.exports`.

  ```javascript
  // myModule.js
  const add = (a, b) => a + b;
  
  module.exports = { add };
  ```

## 07-08-2026

### Modularization (Continued)

  It is the practice of splitting the codebase into separate, dedicated files/modules for better organization, maintainability, and reusability.
    1. Internal/Self Moduled- Splitting it into modules by self
      ./myModule
    2. Core Modules - Node predefined modules.
      fs, http.path.os.crypto.dns.url
    3. External / Third-Party Modules - NPM Modules. - The dependencies that we use.
      Mongoose,Express etc.

#### Core Modules

  Modulename   Module Usecase
  fs           File System
  http         HTTP requests/responses
  path         Path manipulation
  os           Operating System operations
  dns          DNS resolution

  events       Event-driven programming
  crypto       Cryptographic functions
  url          URL parsing and manipulation
  querystring  Parsing query strings
  zlib         Data compression/decompression
