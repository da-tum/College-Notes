// function sample (callback){
//     console.log("Sample");
//     callback();
// }

// function test(){
//     console.log("Test");
// }
// sample(test)

// for (let i=1; i<=5; i++){
//     for (let j=1; j<=i; j++){
//         console.log(j);
//     }
//     console.log(i);
// }   

// Question 1 --> Take an array of length 10 and find out the tudent who pass if the passing marks is 16 of 40.
// Also print their result status .
let marks =[7,16,23,35,12,40,4,19,28,15];
let result = marks.map(function(marks){
    if (marks >=16){
        console.log(marks, "Pass")
    } else {
        console.log(marks, "Fail");
    }
});
console.log(result);

