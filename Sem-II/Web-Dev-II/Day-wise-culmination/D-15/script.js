/* fetch("https://jsonplaceholder.typicode.com/todos/5")
.then((response) => {
if (!response.ok) {
    throw new Error("Network response was not ok");
    } else {
    console.log("Network response was ok");
    return response.json();}
})  
.then(data => console.log(data)); */


/* function getData(url){
    fetch(url)
.then((response) => response.json())  
.then(data => console.log(data)); 
}
getData("https://jsonplaceholder.typicode.com/todos/5"); */


async function getData(url){
let resp = await fetch (url)
// .then((response) => response.json())  
// .then(data => console.log(data)); 
let data = await resp.json()
return data;
}
getData("https://jsonplaceholder.typicode.com/todos/5")
.then(data => console.log(data));
