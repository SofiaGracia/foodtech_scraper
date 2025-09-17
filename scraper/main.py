#
import sys
import os
from get_products import get_products as gp

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.crud import *

def db():

    # Check if table exists if not create it 
    table_data = fetch_table()
    if table_data == None:
        create_tables()
        table_data = []

    # If the table exists but has no data ...
    if len(table_data) == 0:
        # ... scrape the web and insert info in the table
        products_to_insert = gp()
        insert_products(products_to_insert)

    # Now we have some data in the db's table, so let's show it nicely
    print('we have data')
        

if __name__ == "__main__":
    db()