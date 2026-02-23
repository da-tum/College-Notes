// // Async JS
// console.log("Script started");

// // Simulating an asynchronous operation using setTimeout
// // setTimeout(() => {
// //     console.log("Asynchronous operation completed");
// // }, 2000);

// function myfunction() {
//     setTimeout(() => {
//         console.log("Button clicked and asynchronous operation completed");
//         return "Operation Result";
//     }, 2000);
// }

// myfunction(()=>{});
// console.log("Script ended");

console.log("Script started");

function login(uname,password,callback) {
    setTimeout(() => {
        callback({uname:uname,isLoggedIn:true, Message: "Login Successfull"});
    }, 2000);
}

function getVideoList(uname, callback) {
    setTimeout(() => {
        callback([{title:"Video1"},{title: "Video2"},{title:"Video3"}]);
    }, 2000);
}

function getVideoDetails(video, callback) {
    setTimeout(() => {
        callback({title: video.title, duration: "2 hours", description: "This is a video about JavaScript"});
    }, 2000);
}

login("JohnDoe", "password123", (login) => {
    console.log(login);
    getVideoList(login.uname, (videoList) => {
        console.log(videoList);

        getVideoDetails(videoList[0], (videoDetails) => {
            console.log(videoDetails);
        });
    });
});
console.log("Script ended");