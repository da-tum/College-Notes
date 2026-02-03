/* --- Lab 4 Assignment --- */

// Quiz questions array
const quizQuestions = [
  { question: "What is the capital of India?", answer: "Delhi" },
  { question: "Full stack development include , Front-end and ______", answer: "BACKEND" },
  { question: "What is full form of JS?", answer: "JAVA-SCRIPT" },
  { question: "What works as layout designing in front-end?", answer: "HTML" },
  { question: "Properties are used in which language?", answer: "CSS" },
];

function runQuiz() {
  alert("Hello! Welcome to the Quick Quiz");
  let score = 0; // Score tracker

  // Iterate through questions
  for (let i = 0; i < quizQuestions.length; i++) {
    const ques = quizQuestions[i].question;
    const correctAns = quizQuestions[i].answer; // Original answer for display
    const lowerAns = correctAns.toLowerCase(); // Lowercase answer for comparison

    // Get user input
    const userAnswer = prompt(ques);

    // Handle cancel input
    if (userAnswer && userAnswer.toLowerCase().trim() == lowerAns) {
      alert("Correct Answer");
      score++;
    } else {
      // Show correct answer
      alert(`Wrong Answer. The Correct Answer is ${correctAns}`);
    }
  }

  // Show final score
  alert(
    `Quiz Over! Your final score is ${score} out of ${quizQuestions.length}`
  );
}

runQuiz();
