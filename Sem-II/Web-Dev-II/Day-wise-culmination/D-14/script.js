

// prmises are smart organizaion of callback functions
// they are used to handle asynchronous operations in a more manageable way
// they can be in one of three states: pending, fulfilled, or rejected
// they can be chained together using .then() and .catch() methods
// they can also be created using the async/await syntax for cleaner code

// let myPromise = new Promise((res, rej) => {
//     let data = 'this is data';
//     if (data){
//         res(data);
//     } else {
//         rej('Error');
//     }
// })
// console.log(myPromise);

// myPromise.then((data) => {
//     console.log('Promise resolved with data:', data);
// }).catch((error) => {
//     console.error('Promise rejected with error:', error);
// });


let myPromise = new Promise((res, rej) => {
  let data = "hello world";
  if (data) {
    res(data);
  } else {
    rej("Error: Promise rejected");
  }
});

myPromise.then(
  (data) => {
    console.log(data);
  }, //resolved
  (error) => {
    console.log(error);
  }, // rejected
);

console.log(myPromise);