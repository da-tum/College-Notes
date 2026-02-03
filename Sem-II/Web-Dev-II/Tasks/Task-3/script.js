const task3 = document.getElementsByClassName("task");
console.log(task2);

for (let i=0 ; i<task2.length ; i++){
    if(i%2==0){
        task3[i].style.color="red";
        task3[i].style.fontSize="20px"; 
    }
    task3[i].style.color="green";
    task3[i].style.fontSize="25px";
}
console.log(task3.length);


document.querySelector("Task-3").style.backgroundColor="lightblue";
document.querySelector("Task-3").style.padding="20px";
document.querySelector("Task-3").style.borderRadius="30px";



const content=document.getElementById("task");
cont task3= task3.querySelectorAll("p");
for(let i=0;i<task3.length;i++){
    task3[i].style.fontFamily="Arial, sans-serif";
}
content.style.border="2px solid black";