// function handleClick(){
//     document.getElementById("btn").textcontent="Clicked!";
// }

// function handleClick(){
//     document.getElementById("btn").textContent="Clicked!";
//     document.getElementById("heading").textContent="Heading Changed!";
//     document.getElementById("heading").style.color="tomato";

// }


// function handleClick() {
//     const span = document.createElement("span");
//     span.textContent = "This is a dynamically created span element.";

//     const image = document.createElement("img");
//     image.setAttribute("src", "https://www.pinterest.com/luisanddagmar/linkedin-background-image/");
//     image.setAttribute("alt", "Placeholder Image");

//     document.getElementById("content").appendChild(span);
//     document.getElementById("content").appendChild(image);
// }


document.getElementById("btn").addEventListener("click",()=>{
    const span = document.createElement("span");
    span.textContent = "This is a dynamically created span element.";

    const image = document.createElement("img");
    image.setAttribute("src", "https://www.pinterest.com/luisanddagmar/linkedin-background-image/");
    image.setAttribute("alt", "Placeholder Image");

    document.getElementById("content").appendChild(span);
    document.getElementById("content").appendChild(image);
})

