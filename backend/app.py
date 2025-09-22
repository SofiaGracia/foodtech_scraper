from flask import Flask, jsonify, request
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from scraper.run_scraper import get_table_info, check_table_exists
from crud import insert_one_product as iop
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to My API"

@app.route('/data', methods=['GET','POST'])
def manage_request():

    try:
        # First of all, check if the table exists
        check_table_exists()

        if request.method == 'GET':
            # return all the info in the database
            dbresult = get_table_info()
            return jsonify({'DBResult': dbresult}), 200
    
        if request.method == 'POST':

            data = request.get_json()

            if not data:
                return jsonify({'Error': 'Request body must be JSON'}), 400
            
            required_keys = ['product_name', 'nutri_score', 'nova_score', 'green_score']
            for key in required_keys:
                if key not in data:
                    return jsonify({'Error': f'Missing field: {key}'}), 400

            # Extract the data from the body of the request
            product_name = data['product_name']
            nutri_score = data['nutri_score']
            nova_score = data['nova_score']
            green_score = data['green_score']

            # insert the data in the db
            iop(product_name, nutri_score, nova_score, green_score)
            # return a response
            return jsonify({'Message':'Product added', 'data':data}), 201

    except mysql.connector.Error as e:
        return jsonify({'Error': f'Database error: {str(e)}'}), 500

    except Exception as e:
        return jsonify({'Error': f'Unexpected error: {str(e)}'}), 500

    # TODO (After other things) Manage errors

if __name__ == "__main__":
    app.run(debug=False) # Put to True to restart if we make changes