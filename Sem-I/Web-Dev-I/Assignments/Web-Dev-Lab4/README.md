# Lab 4: Simple JavaScript Quiz

**Name:** Harsh Dev Jha  
**Course:** B. Tech CSE Core  
**Section:** A
**Roll No:** 2501010168  
**Lab Assignment:** 4

## Description

This project is a simple JavaScript quiz game that executes entirely within the browser console. It was created as part of the Web Dev I Lab Assignment 4. The objective is to reinforce the use of JavaScript arrays, loops, conditionals, functions, and basic input/output methods without utilizing HTML DOM manipulation.

## Prerequisites
- A modern web browser (e.g., Chrome, Firefox, Safari) with JavaScript enabled.
- No additional software or dependencies required.

## Technologies Used
- **JavaScript:** Core language for quiz logic, including arrays, loops, and functions.
- **HTML:** Basic structure to load the JavaScript script in the browser.

## Features

- **Question Bank:** Stores 5 predefined questions and answers in an array of objects.
- **Interactive Input:** Uses `prompt()` to collect user answers and `alert()` to provide immediate feedback.
- **Input Validation:** Processes user input using `toLowerCase()` and `trim()` to ensure case-insensitive and whitespace-tolerant comparisons.
- **Score Tracking:** Maintains a running score throughout the quiz and displays the final result upon completion.
- **Modular Code:** Logic is encapsulated within a `runQuiz()` function for better organization.

## File Structure

* `index.html`: A basic HTML file to load the script.
- `quiz.js`: The main logic file containing the `quizQuestions` array and the `runQuiz()` function.
- `README.md`: Project documentation.

## How to Run

1. **Clone the Repository:**
    Download or clone this repository to your local machine.
2. **Open in Browser:**
    Open the `index.html` file in any modern web browser. The quiz should start automatically (or check your browser's console if configured differently).
3. **Run via Console (Alternative):**
    You can also open your browser's Developer Tools (F12), navigate to the **Console** tab, paste the code from `quiz.js`, and press **Enter** to start the quiz manually.

## Example Usage

* The game will ask: *"What is the capital of India?"*
- If you type: *"  delhi  "*
- The game validates the input (trimming spaces and converting to lowercase) and alerts: *"Correct Answer"*.
- If incorrect, it alerts the correct answer.
- At the end, it displays: *"Quiz Over! Your final score is X out of 5"*.
