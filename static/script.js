const questions = [
    {
        question: "What is 2 + 2?",
        options: ["3", "4", "5"],
        correctAnswer: "4",
        hintLevel1: "It's an even number.",
        hintLevel2: "It's more than 3."
    },
    // Tambahkan lebih banyak pertanyaan sesuai kebutuhan
];

let currentQuestionIndex = 0;

function startGame() {
    const data = questions[currentQuestionIndex];
    document.getElementById('question').innerText = data.question;
    document.getElementById('options').innerHTML = '';

    data.options.forEach(option => {
        const button = document.createElement('button');
        button.className = 'option-btn';
        button.innerText = option;
        button.addEventListener('click', function() {
            submitAnswer(option);
        });
        document.getElementById('options').appendChild(button);
    });

    document.getElementById('question-container').style.display = 'block';
    document.getElementById('result').innerText = '';
    document.getElementById('hint').innerText = '';
    document.getElementById('explanation').innerText = '';
    document.getElementById('explain-btn').style.display = 'none';
    document.getElementById('next-question-btn').style.display = 'none';
}

function submitAnswer(userAnswer) {
    const data = questions[currentQuestionIndex];
    const resultText = userAnswer === data.correctAnswer ? "Correct!" : "Incorrect!";
    document.getElementById('result').innerText = resultText;

    if (resultText === "Correct!") {
        document.getElementById('explain-btn').style.display = 'inline-block';
        document.getElementById('next-question-btn').style.display = 'inline-block';
    } else {
        document.getElementById('next-question-btn').style.display = 'inline-block';
    }
}

function getHint(level) {
    const data = questions[currentQuestionIndex];
    const hint = level === 1 ? data.hintLevel1 : data.hintLevel2;
    document.getElementById('hint').innerText = hint;
}

document.getElementById('start-game-btn').addEventListener('click', startGame);
document.getElementById('hint1-btn').addEventListener('click', function() {
    getHint(1);
});
document.getElementById('hint2-btn').addEventListener('click', function() {
    getHint(2);
});
document.getElementById('next-question-btn').addEventListener('click', function() {
    currentQuestionIndex++;
    if (currentQuestionIndex < questions.length) {
        startGame();
    } else {
        alert("You've completed all questions!");
    }
});
