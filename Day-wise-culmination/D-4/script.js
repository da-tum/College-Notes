// A1
// let arr=[1,2,3,4,5];
// let revArr=[];
// while (arr.length>0){
//     revArr.push(arr.pop());
// }
// console.log(revArr);

// A2
// let arr= [-1,-2,3,4,-5,6];
// let posArr=[];
// while (arr.length>0){
//     let val=arr.pop();
//     if (val>0){
//         posArr.push(val);
//     }   
// }
// console.log(posArr);

// or 

// for (let i=arr.length-1;i>=0;i--){
//     if (arr[i]>0){
//         posArr.push(arr[i]);
//     }
// }
// console.log(posArr);

// A3
// let arr=[1,2,3,2,1];
// let originalArr=[...arr];
// let isPalindrome=true;
// while (arr.length>0){
//     if (arr.pop()!==originalArr.shift()){
//         isPalindrome=false;
//         break;
//     }           
// }
// console.log(isPalindrome);


// or 

let arr=[1,2,3,2,1];
let originalArr=[];
let reversedArr=[];
for (let i=0;i<arr.length;i++){
    originalArr.push(arr[i]);
    reversedArr.unshift(arr[i]);
}
let isPalindrome=true;
for (let i=0;i<originalArr.length;i++){
    if (originalArr[i]!==reversedArr[i]){
        isPalindrome=false;
        break;
    }
}
console.log(isPalindrome);

// A4