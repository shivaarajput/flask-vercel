import random
import json
from flask import Flask
from datetime import datetime

app = Flask(__name__)

def get_quotes():
    with open('quesTest.json', 'r') as file:
        quotes = json.load(file)
    return quotes

@app.route('/')
def get_random_quote():
    capital = get_quotes()
    random_cap = random.choice(list(capital.keys()))
    current_datetime = datetime.now()
    current_date = current_datetime.date()
    current_time = current_datetime.time()

    return f"""
    \{
    Developer : Shiva :),
    
    Current Time : {current_time},
    
    Current Date : {current_date},
    
    What is the capital of {random_cap} ? : The capital of {random_cap} is {capital[random_cap]}.
    \}
    """

if __name__ == '__main__':
    app.run(debug=True)
