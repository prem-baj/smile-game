from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from decorators import token_required
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import requests
import answer
import users
import random
app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY']='004f2af45d3a4e161a7dd2d17fdae47f'

@app.route('/register', methods=['POST'])
def signup_user(): 
    data = request.get_json() 
    hashed_password = generate_password_hash(data['password'], method='sha256')
    users.register(data['name'], hashed_password)
    return jsonify({'message': 'registered successfully'})

@app.route('/quiz')
def generate_quiz():
    res = requests.get('https://marcconrad.com/uob/smile/api.php?out=json&base64=no').json()
    solution = res.get("solution")
    answers = [solution]
    while len(answers) < 4:
        random_num = random.randint(0, 9)
        if not random_num == solution:
            answers.append(random_num)
    
    random.shuffle(answers)
    
    result = {
        "question": res.get("question"),
        "answers": answers
    }
    # answer.create(solution)
    answer.remove_last_if_exist()
    answer.create(solution)

    return jsonify(result)


@app.route('/quiz/answer/<solution>', methods=['POST'])
def post_answer_solution(solution):
    _, correct_solution = answer.get_actual()
    answer.update(solution)
    return jsonify({"correct": correct_solution == int(solution)}), 201