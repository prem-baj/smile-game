from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import requests
import answer
import users
import random
from functools import wraps
import jwt
import datetime
app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY']='004f2af45d3a4e161a7dd2d17fdae47f'

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return jsonify({'message': 'a valid token is missing'})
        try:
            data = jwt.decode(token[7:], app.config['SECRET_KEY'], algorithms=["HS256"])
            user = users.get_by_username(data['sub'])
        except:
            return jsonify({'message': 'token is invalid'})

        return f(user[0], *args, **kwargs)
    return decorator

@app.route('/register', methods=['POST'])
def signup_user(): 
    data = request.get_json() 
    hashed_password = generate_password_hash(data['password'], method='sha256')
    users.register(data['username'], hashed_password)
    return jsonify({'message': 'registered successfully'})

@app.route('/login', methods=['POST']) 
def login_user():
    data = request.get_json()
 
    user = users.get_by_username(data['username'])
    id, username, password = user
    if not user or not check_password_hash(password, data['password']):
        return jsonify({ 'message': 'Invalid credentials', 'authenticated': False }), 401
    token = jwt.encode({
        'sub': username,
        'iat':datetime.datetime.utcnow(),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
        app.config['SECRET_KEY'])
    return jsonify({ 'username': username, 'token': token.encode().decode('UTF-8') })

@app.route('/quiz')
@token_required
def generate_quiz(user_id):
    res = requests.get('https://marcconrad.com/uob/smile/api.php?out=json&base64=no').json()
    solution = res.get("solution")
    answers = [solution]
    while len(answers) < 4:
        random_num = random.randint(0, 9)
        if not random_num in answers:
            answers.append(random_num)
    
    random.shuffle(answers)

    correct_count = answer.count_correct(user_id)
    
    result = {
        "question": res.get("question"),
        "answers": answers,
        "correct_count": correct_count
    }
    answer.remove_last_if_exist(user_id)
    answer.create(solution, user_id)

    return jsonify(result)


@app.route('/quiz/answer/<solution>', methods=['POST'])
@token_required
def post_answer_solution(user_id, solution):
    _, correct_solution = answer.get_actual(user_id)
    answer.update(user_id, solution)
    return jsonify({
        "correct": correct_solution == int(solution),
    }), 201