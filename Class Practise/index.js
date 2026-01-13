function sample (callback){
    console.log("Sample");
    callback();
}

function test(){
    console.log("Test");
}
sample(test)
