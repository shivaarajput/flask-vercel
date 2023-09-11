import random
import json
from flask import Flask
from datetime import datetime

app = Flask(__name__)

def get_ques():
    with open('quesTest.json', 'r') as file:
        ques = json.load(file)
    return ques

@app.route('/', methods=['GET'])
def get_random_ques():
    capital = get_ques()
    random_cap = random.choice(list(capital.keys()))
    current_datetime = datetime.now()
    current_date = current_datetime.date()
    current_time = current_datetime.strftime("%H:%M:%S")

    return f"Each time you scroll you see a new content here!!<br><hr><br>Developer : Shiva :)<br><br>Current Time : {current_time}<br><br>Current Date : {current_date}<br><br>What is the capital of {random_cap} ? : The capital of {random_cap} is {capital[random_cap]}."

if __name__ == '__main__':
    app.run(debug=True)
