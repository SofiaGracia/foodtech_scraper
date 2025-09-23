import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))
from get_products import get_products as gp

from backend.crud import *

# Checks if the table exists, if it doesn't, create the table
def check_table_exists():
    table_data = fetch_table()
    if table_data == None:
        create_table()
    
def get_table_info():

    table_data = fetch_table()

    # Scrape the web and insert info in the table
    if len(table_data) < 50:
        products_to_insert = gp()
        insert_products(products_to_insert)

    # Return the info inserted
    return fetch_table()
        