const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());

const questions = [
    {
        question: "What is 2 + 2?",
        options: ["3", "4", "5"],
        correctAnswer: "4",
        hintLevel1: "It's an even number.",
        hintLevel2: "It's more than 3.",
        explanation: "2 + 2 equals 4."
    },
];

let currentQuestionIndex = 0;

app.post('/start_game', (req, res) => {
    const data = questions[currentQuestionIndex];
    res.json(data);
});

app.post('/check_answer', (req, res) => {
    const userAnswer = req.body.user_answer;
    const data = questions[currentQuestionIndex];
    const result = userAnswer === data.correctAnswer ? "Correct!" : "Incorrect!";
    res.json({ result, show_explain_button: result === "Correct!" });
});

app.post('/get_hint', (req, res) => {
    const level = req.body.hint_level;
    const data = questions[currentQuestionIndex];
    const hint = level === 1 ? data.hintLevel1 : data.hintLevel2;
    res.json({ hint });
});

app.post('/get_explanation', (req, res) => {
    const data = questions[currentQuestionIndex];
    res.json({ explanation: data.explanation });
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
