const task2 = document.getElementsByClassName("task");
console.log(task2);

for (let i=0 ; i<task2.length ; i++){
    task2[i].style.color="red";
    task2[i].style.fontSize="20px"; 
}
console.log(task2.length);