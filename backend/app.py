# main.py
from flask import Flask, jsonify
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from scraper.run_scraper import db

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to My API"

@app.route('/data', methods=['GET'])
def get():
    dbresult = db()
    return jsonify({'DBResult': dbresult})

if __name__ == "__main__":
    app.run(debug=False) # Put to True to restart if we make changes