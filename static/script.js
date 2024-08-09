document.getElementById('start-game-btn').addEventListener('click', function() {
    startGame();
});

function startGame() {
    fetch('https://my-mindforge-backend.herokuapp.com/start_game', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('question').innerText = data.question;
        document.getElementById('options').innerHTML = ''; // Clear previous options

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
    });
}

function submitAnswer(userAnswer) {
    fetch('/check_answer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_answer: userAnswer })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = data.result;

        if (data.show_explain_button) {
            document.getElementById('explain-btn').style.display = 'inline-block';
            document.getElementById('next-question-btn').style.display = 'inline-block';
        } else {
            document.getElementById('next-question-btn').style.display = 'inline-block';
        }
    });
}

document.getElementById('hint1-btn').addEventListener('click', function() {
    getHint(1);
});

document.getElementById('hint2-btn').addEventListener('click', function() {
    getHint(2);
});

function getHint(level) {
    fetch('/get_hint', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ hint_level: level })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('hint').innerText = data.hint;
    });
}

document.getElementById('explain-btn').addEventListener('click', function() {
    getExplanation();
});

function getExplanation() {
    fetch('/get_explanation', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('explanation').innerText = data.explanation;
    });
}

document.getElementById('next-question-btn').addEventListener('click', function() {
    startGame(); // Simply starts a new game (question)
});
