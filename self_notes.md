# Class Notes

## 12.1.26
Redeclaring with let wll give 'SyntaxError'  
redeclaring with const afterwords will run the file until the error comes and then the 'TypeError'  
by default var is assigned.

```js
a=10;
console.log(a)
```

in case 

```js
a=10;
console.log(a)
let a;
```

will give an error that is Reference Error.that is cannot acess before initialization.

```py
Js Is synchronous that is line by line - like interpreter 
but when line by line code reaches in JS engine it is stored in a place caled "CALLED STACK", then is processed altogether that is like a COMPILER , and in such instance var goes to top of the scope.
But in case of let it doesnt go to top of the scope.

Almost Everything in JS is Object.
```

### TDZ - Temporal Dead Zone

Until a variable is properly initialized until then the variable is in a Temporal Dead Zone.

Math Functiosn in JS

OTP gen used this functions beforehand still foes but is upgraded now.

Trunk in Maths ,

In general Map function is used for rendering , iteration .
Time complexity in For loop in increased . Returns the length of Array.

Filter Reduces the subset

Reduce returns a single number

Big O - azentotic expression .
Brute Force and Optimized Approach in Problem Solving.

in console 

```js
console.log(Window)
```

then it will show all the object instantiation in the windows.

line by line assigning in js ,
also in js whenever an Object is instantiated its 
assigned a new address in memory location as a new reference . Thus different memory address , array is also and Obejct.
Thus when comparing 

```js
console.log([]==[])
or
console.log({}=={})
```

will give false.

NaN is used as a bug support in JS.

return will return only once in a function as after the return statement the code stops 
so if we call it even after the once return call the code will be unreachable for it to return anything.

## Functions

### Arrow Function

1. Treating the variable as a function.
2. Use for return statement is sustained.

### Callback Function 

Functions passed into a HIgher Order function and used as a parameter.

1. It is a asynchronous function. Can do multiple things at once.

```md
Asynchronous Function: We can move to another task before the previous one finishes its execution.
Callback Function: We can pass one function inside another function as an argument.
```

#### Callback Hell

## Methods

1. Map returns the same length of the array
2. Filter return the subset of orignal array
3. Reduce method will return only one value (like : sum of all the numbers in the array)

---
