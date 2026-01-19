let arr=[1,2,3,4,5];
while (arr.length>0){
    arr.push(arr.pop());
}
console.log(arr);