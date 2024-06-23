"""
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
"""

from flask import Flask, jsonify
import requests
import re
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def hello_world():
    return  'App is running...'

@app.route('/scrape', methods=['GET'])
def scrape_links():
    url = 'https://ppup.ac.in/notice-board'  # Replace with your target URL

    # Fetch the webpage conten
    try:
      response = requests.get(url, proxies = {"http":"http://proxy.server:3128", "https":"https://proxy.server:3128"}
)
      response.raise_for_status()  # Ensure we notice bad response

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

    # Get the raw HTML content
    html_content = response.text

    # Fix the specific broken <a> tags
    fixed_html_content = re.sub(r'(<a href="[^"]+)"\s*<strong>', r'\1"><strong>', html_content)

    # Parse the fixed HTML
    soup = BeautifulSoup(fixed_html_content, 'lxml')

    # Find links containing a <strong> tag
    links = []
    for a_tag in soup.find_all('a'):
        if a_tag.find('strong'):
            href = a_tag.get('href')
            text = a_tag.get_text(strip=True)
            links.append({'link': href, 'text': text})
            if len(links) >= 10:
                break

    return jsonify(links)

if __name__ == '__main__':
    app.run(debug=True)
