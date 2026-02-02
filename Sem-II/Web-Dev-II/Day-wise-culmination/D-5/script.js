let str = "hello world";
let sliced_str = str.slice(-5);
console.log(sliced_str);

let arr = [0,1,2,3,4];
let sliced_arr = arr.slice(-2);
console.log(sliced_arr);

let sentence = "the quick brown fox jumps over the lazy dog"
let ind = sentence.indexOf("the");
console.log(ind);

let sent = "tu meri me tera me tera tu meri";
let split_sent = sent.split("r");
console.log(split_sent);
console.log(`Number of r: ${split_sent.length-1}`);