import random
import json
from flask import Flask, jsonify

app = Flask(__name__)

def get_quotes():
    with open('quesTest.json', 'r') as file:
        quotes = json.load(file)
    return quotes

@app.route('/', methods=['GET'])
def get_random_quote():
    capital = get_quotes()
    random_cap = random.choice(list(capital.keys()))
    return jsonify({f"What is the capital of {random_cap} ?": f"The capital of {random_cap} is {capital[random_cap]}."})

if __name__ == '__main__':
    app.run(debug=True)
