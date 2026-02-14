const heading = document.getElementById('Culmination');
heading.style.color = 'blue';
heading.style.textAlign = 'center';
heading.style.fontFamily = 'Arial, sans-serif';
heading.style.backgroundColor = '#000';

console.log(heading.textContent);

heading.textContent = 'Day 8 - JavaScript DOM Manipulation';

const paragraphs= document.getElementById('para');
console.log(para)
for (let i=0 ; i<para.length ; i++){
    para[i].style.fontSize = '18px';
    para[i].style.backgroundColor = 'cyan';
}

// querySelectorAll example
const paraElements = document.querySelectorAll('#para');
paraElements.forEach((p) => {
    p.style.margin = '10px 0';
    p.style.padding = '10px';
    p.style.border = '1px solid #000';
});