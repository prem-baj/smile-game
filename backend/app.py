from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import random
import psycopg2

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = psycopg2.connect(
        host='localhost',
        database='smile-game',
        user="",
        password=""
    )
    return conn


@app.route('/get_quiz')
def get_random_quiz():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("select version()")
    data = cur.fetchone()
    print("Connection established to: ",data)
    print(cur)
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
    return jsonify(result)


@app.route('/post_answer/', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return '', 204