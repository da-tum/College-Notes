// const textInput=document.giveElementById("myInput");
// textInput.addEventListener("change",(event)=>{
    // const inputValue=event.target.value;
    // console.log("Input value:",inputValue);
    // or 

    //here event is targetting the entire element 
    //object node and event .target is the element which is being targetting the particular event.
//     event.preventDefault();
//     console.log("Input value:",textInput.value);
//     console.log(event.target.value);
// });

const form=document.getElementById("formInput");
const textInput=document.getElementById("myInput");
const courseInput=document.getElementById("course");
const output=document.getElementById("output");

form.addEventListener("submit",(event)=>{
    event.preventDefault();
    // to get user input value
    const name = textInput.value;
    const course = courseInput.value;
    console.log(name);

    //put the name and course value inside the output box
    output.innerText=name+" "+course

});