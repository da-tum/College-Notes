# JavaScript Notes: From Basic to Advanced

This document provides a comprehensive overview of JavaScript concepts, progressing from basic fundamentals to advanced topics. It's designed for learners moving from beginner to expert level.

## Table of Contents
1. [Basic Concepts](#basic-concepts)
2. [Intermediate Concepts](#intermediate-concepts)
3. [Advanced Concepts](#advanced-concepts)

## Basic Concepts

### 1. Variables and Data Types
JavaScript has three ways to declare variables: `var`, `let`, and `const`.

- `var`: Function-scoped, can be redeclared and updated.
- `let`: Block-scoped, can be updated but not redeclared.
- `const`: Block-scoped, cannot be updated or redeclared.

**Data Types:**
- Primitive: string, number, boolean, undefined, null, symbol, bigint
- Reference: object, array, function

```javascript
let name = "John"; // string
const age = 25; // number
var isStudent = true; // boolean
let score; // undefined
const person = null; // null
```

### 2. Operators
- Arithmetic: +, -, *, /, %, **
- Comparison: ==, ===, !=, !==, <, >, <=, >=
- Logical: &&, ||, !
- Assignment: =, +=, -=, *=, /=, %=

### 3. Control Structures
#### If-Else Statements
```javascript
if (condition) {
    // code
} else if (anotherCondition) {
    // code
} else {
    // code
}
```

#### Switch Statement
```javascript
switch (expression) {
    case value1:
        // code
        break;
    case value2:
        // code
        break;
    default:
        // code
}
```

#### Loops
- For loop: `for (let i = 0; i < 5; i++) { }`
- While loop: `while (condition) { }`
- Do-while loop: `do { } while (condition);`
- For-in loop: for iterating over object properties
- For-of loop: for iterating over iterable objects

### 4. Functions
Functions are first-class citizens in JavaScript.

```javascript
// Function declaration
function greet(name) {
    return `Hello, ${name}!`;
}

// Function expression
const greet = function(name) {
    return `Hello, ${name}!`;
};

// Arrow function (ES6+)
const greet = (name) => `Hello, ${name}!`;
```

## Intermediate Concepts

### 1. Objects and Arrays
#### Objects
```javascript
const person = {
    name: "John",
    age: 30,
    greet: function() {
        console.log(`Hello, I'm ${this.name}`);
    }
};
```

#### Arrays
```javascript
const fruits = ["apple", "banana", "orange"];
fruits.push("grape"); // Add to end
fruits.pop(); // Remove from end
fruits.shift(); // Remove from beginning
fruits.unshift("mango"); // Add to beginning
```

### 2. DOM Manipulation
JavaScript can interact with HTML elements.

```javascript
// Selecting elements
const element = document.getElementById("myId");
const elements = document.querySelectorAll(".myClass");

// Modifying elements
element.textContent = "New text";
element.style.color = "red";

// Event listeners
element.addEventListener("click", function() {
    console.log("Element clicked!");
});
```

### 3. Asynchronous JavaScript
#### Callbacks
```javascript
function fetchData(callback) {
    setTimeout(() => {
        callback("Data received");
    }, 1000);
}

fetchData((data) => {
    console.log(data);
});
```

#### Promises
```javascript
const myPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve("Data received");
    }, 1000);
});

myPromise.then((data) => {
    console.log(data);
}).catch((error) => {
    console.error(error);
});
```

#### Async/Await (ES8)
```javascript
async function fetchData() {
    try {
        const response = await fetch("https://api.example.com/data");
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error(error);
    }
}
```

### 4. ES6+ Features
- Template literals: `Hello, ${name}!`
- Destructuring: `const {name, age} = person;`
- Spread operator: `const newArray = [...oldArray];`
- Default parameters: `function greet(name = "World") { }`
- Modules: `import` and `export`

## Advanced Concepts

### 1. Closures
A closure is a function that has access to its own scope, the outer function's scope, and the global scope.

```javascript
function outerFunction() {
    let outerVariable = "I'm outer!";
    
    function innerFunction() {
        console.log(outerVariable); // Can access outerVariable
    }
    
    return innerFunction;
}

const closure = outerFunction();
closure(); // Logs: "I'm outer!"
```

### 2. Prototypes and Inheritance
JavaScript uses prototypal inheritance.

```javascript
function Person(name, age) {
    this.name = name;
    this.age = age;
}

Person.prototype.greet = function() {
    console.log(`Hello, I'm ${this.name}`);
};

const john = new Person("John", 30);
john.greet();
```

### 3. Classes (ES6)
Syntactic sugar over prototypes.

```javascript
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    
    greet() {
        console.log(`Hello, I'm ${this.name}`);
    }
    
    static createPerson(name, age) {
        return new Person(name, age);
    }
}

const john = new Person("John", 30);
john.greet();
```

### 4. Advanced Array Methods
- `map()`: Transform each element
- `filter()`: Filter elements based on condition
- `reduce()`: Reduce array to single value
- `find()`: Find first element matching condition
- `some()`: Check if at least one element matches
- `every()`: Check if all elements match

### 5. Error Handling
```javascript
try {
    // Code that might throw an error
    throw new Error("Something went wrong");
} catch (error) {
    console.error(error.message);
} finally {
    // Code that always runs
    console.log("Cleanup");
}
```

### 6. Memory Management
- Garbage collection in JavaScript
- Memory leaks: circular references, global variables
- WeakMap and WeakSet for memory-efficient storage

### 7. Performance Optimization
- Debouncing and throttling
- Memoization
- Virtual DOM (in frameworks like React)
- Code splitting and lazy loading

### 8. Design Patterns
- Module pattern
- Observer pattern
- Singleton pattern
- Factory pattern

### 9. Web APIs
- Fetch API for HTTP requests
- LocalStorage and SessionStorage
- WebSockets for real-time communication
- Service Workers for offline functionality

### 10. Modern JavaScript Ecosystem
- Transpilers: Babel
- Bundlers: Webpack, Rollup
- Package managers: npm, yarn
- Frameworks: React, Vue, Angular
- Testing: Jest, Mocha
- Linting: ESLint

This covers the core concepts from basic to advanced JavaScript. Practice regularly and build projects to solidify your understanding. Remember, JavaScript is constantly evolving, so stay updated with the latest ECMAScript specifications.
