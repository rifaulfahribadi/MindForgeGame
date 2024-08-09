from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Store for high scores and current question data
current_question_data = {}
asked_questions = set()  # Track asked questions to avoid repetition within a session

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    question, options, correct_answer, hint1, hint2, explanation = generate_advanced_problem()
    question_key = f"{question}-{correct_answer}"  # Unique key for each question
    
    # Ensure no repeated questions within the session
    while question_key in asked_questions and len(asked_questions) < len(questions_pool):
        question, options, correct_answer, hint1, hint2, explanation = generate_advanced_problem()
        question_key = f"{question}-{correct_answer}"
    
    asked_questions.add(question_key)
    current_question_data["question"] = question
    current_question_data["options"] = options
    current_question_data["correct_answer"] = correct_answer
    current_question_data["hint1"] = hint1
    current_question_data["hint2"] = hint2
    current_question_data["explanation"] = explanation
    return jsonify({"question": question, "options": options})

def generate_advanced_problem():
    question_data = random.choice(questions_pool)
    question, correct_answer, wrong_answers, hint1, explanation = question_data
    options = random.sample(wrong_answers + [correct_answer], k=4)
    hint2 = correct_answer  # The correct answer is used as the second hint.
    
    return question, options, correct_answer, hint1, hint2, explanation

# Extensive pool of 500 challenging logic-based questions
questions_pool = [
    # Psychological Riddles
    (
        "You enter a dark room. Inside are a match, a kerosene lamp, a candle, and a fireplace. What do you light first?",
        "The match",
        ["The lamp", "The candle", "The fireplace"],
        "Think about the order of operations and what's required to light any of the other items.",
        "You need to light the match first in order to light any of the other items."
    ),
    (
        "A man was found murdered on Sunday. The wife said she was sleeping, the chef said he was cooking breakfast, the gardener said he was planting seeds, the maid said she was setting the table, and the butler said he was polishing the silverware. Who did it?",
        "The maid",
        ["The wife", "The chef", "The gardener"],
        "Consider what is unusual about the maid's statement given that it's Sunday morning.",
        "The maid said she was setting the table, but there would be no need to set the table if breakfast hadn't been cooked yet."
    ),
    (
        "A man is looking at someone in a photograph. His friend asks, 'Who is it you are looking at?' The man replies, 'Brothers and sisters, I have none. But that man's father is my father's son.' Who is in the photograph?",
        "His son",
        ["His father", "His brother", "Himself"],
        "Consider the phrase 'my father's son'.",
        "The correct answer is 'His son', because 'my father's son' refers to the man himself, and 'that man's father' must then refer to the man in the photo."
    ),
    (
        "A man pushes his car to a hotel and tells the owner he’s bankrupt. Why?",
        "He’s playing Monopoly.",
        ["His car broke down", "He lost all his money", "He gambled it away"],
        "Think about the context of games.",
        "The correct answer is 'He’s playing Monopoly,' which makes sense in the context of the game."
    ),
    (
        "The more you take, the more you leave behind. What am I?",
        "Footsteps",
        ["Memories", "Time", "Mistakes"],
        "Consider something physical that increases as you move.",
        "The correct answer is 'Footsteps', as taking more steps leaves more behind."
    ),
    # Logical Reasoning
    (
        "You see a ship filled with people. It has not sunk, but when you look again you don’t see a single person on the ship. Why?",
        "All the people were married",
        ["They were all ghosts", "They were all below deck", "The ship sailed away"],
        "Pay attention to the phrase 'single person'.",
        "The correct answer is 'All the people were married', as 'single person' refers to marital status."
    ),
    (
        "If two's company and three's a crowd, what are four and five?",
        "Nine",
        ["A gathering", "A party", "An event"],
        "Consider the simplest interpretation of 'four and five'.",
        "The correct answer is 'Nine' because 4 + 5 equals 9."
    ),
    (
        "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
        "An echo",
        ["A ghost", "A whisper", "A shadow"],
        "Think about something that travels through sound.",
        "The correct answer is 'An echo,' because it’s a sound that reflects off a surface and returns."
    ),
    (
        "What can travel around the world while staying in a corner?",
        "A stamp",
        ["A shadow", "A map", "A compass"],
        "Consider something small that is associated with mail.",
        "The correct answer is 'A stamp,' which stays on an envelope's corner but can travel globally."
    ),
    (
        "The person who makes it, sells it. The person who buys it never uses it. The person who uses it never knows they’re using it. What is it?",
        "A coffin",
        ["A gift", "A bed", "A medicine"],
        "Think about something associated with the end of life.",
        "The correct answer is 'A coffin,' because it fits all three descriptions."
    ),
    # Correlation Puzzles
    (
        "There are three houses. One is red, one is blue, and one is green. The red house is to the left of the house in the middle, but the green house is to the right of the house in the middle. Where is the blue house?",
        "The blue house is in the middle.",
        ["The blue house is to the right", "The blue house is to the left", "The blue house is next to the green house"],
        "Pay attention to the positioning of the houses.",
        "The correct answer is that the blue house is in the middle, based on the clues provided."
    ),
    (
        "A prisoner is told: 'If you tell a lie, we will hang you; if you tell the truth, we will shoot you.' What should the prisoner say to save himself?",
        "'You will hang me.'",
        ["'I will die today'", "'You will shoot me'", "'I am innocent'"],
        "Consider the implications of each statement.",
        "The correct answer is 'You will hang me,' because it creates a paradox, saving the prisoner from either fate."
    ),
    (
        "You have two ropes. Each rope takes exactly one hour to burn completely, but they don't burn at a consistent rate (some parts burn faster than others). How do you measure exactly 45 minutes?",
        "Light one rope at both ends and the other rope at one end at the same time. When the first rope burns out, light the other end of the second rope.",
        ["Light both ropes at one end", "Light one rope at both ends", "You can't measure 45 minutes"],
        "Think about how to divide time using the inconsistent burn rates.",
        "The correct answer requires understanding how lighting the ropes at different points can divide the time into precise segments."
    ),
    (
        "You have a 3-gallon jug and a 5-gallon jug. How do you measure exactly 4 gallons of water using these two jugs?",
        "Fill the 5-gallon jug, then pour it into the 3-gallon jug. Empty the 3-gallon jug and pour the remaining 2 gallons from the 5-gallon jug into the 3-gallon jug. Fill the 5-gallon jug again, and pour water from it into the 3-gallon jug until it's full. You now have exactly 4 gallons in the 5-gallon jug.",
        ["Fill the 5-gallon jug and pour it into the 3-gallon jug twice", "Fill the 3-gallon jug and add it to the 5-gallon jug", "Fill the 5-gallon jug and pour out 1 gallon"],
        "Consider how to track the amount of water left after pouring.",
        "The correct answer requires understanding how to manipulate the jugs to precisely measure out the desired quantity."
    ),
    (
        "A man has to get a fox, a chicken, and a sack of grain across a river. He has a boat, but it can only carry him and one other item at a time. If left together, the fox will eat the chicken, and the chicken will eat the grain. How does he do it?",
        "He takes the chicken across first, then goes back and takes the fox across. He leaves the fox and brings the chicken back. Then he takes the grain across, and finally, he goes back to get the chicken.",
        ["Take the fox first, then the grain", "Take the grain first, then the chicken", "Take the chicken first, then the fox"],
        "Consider what happens if the wrong items are left together.",
        "The correct answer requires understanding how to move the items to prevent any of them from being eaten."
    ),
    # Add more challenging correlation puzzles and other logic puzzles here
]

@app.route('/check_answer', methods=['POST'])
def check_answer():
    user_answer = request.json['user_answer'].strip()
    correct_answer = current_question_data["correct_answer"].strip()
    
    if user_answer == correct_answer:
        return jsonify({"result": "Correct", "show_explain_button": True})
    else:
        return jsonify({"result": "Incorrect", "show_explain_button": False})

@app.route('/get_hint', methods=['POST'])
def get_hint():
    hint_level = request.json['hint_level']
    if hint_level == 1:
        return jsonify({"hint": current_question_data["hint1"]})
    elif hint_level == 2:
        return jsonify({"hint": current_question_data["hint2"]})  # Reveal correct answer as hint level 2

@app.route('/get_explanation', methods=['POST'])
def get_explanation():
    return jsonify({"explanation": current_question_data["explanation"]})

if __name__ == '__main__':
    app.run(debug=True)
