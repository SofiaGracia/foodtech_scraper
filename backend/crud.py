import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from db import Database  # import singleton class

def create_table():
    db = Database()
    conn = db.get_connection()
    cursor = conn.cursor()

    # SQL to create table "products"
    create_products_table = """
    CREATE TABLE IF NOT EXISTS products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        nutri_score VARCHAR(100),
        nova_score VARCHAR(100),
        green_score VARCHAR(100)
    );
    """

    cursor.execute(create_products_table)
    # Commit is only necessary when we modify data (INSERT, UPDATE, DELETE)
    conn.commit()  # Save the changes
    cursor.close()
    db.close_connection()

# Read data
def fetch_table():

    db = Database()
    conn = db.get_connection()
    cursor = conn.cursor()

    try:
        # SQL to fetch info from table products
        fetch_table_db = "SELECT * FROM products;"

        cursor.execute(fetch_table_db)
        products_info = cursor.fetchall()

    except:
        return None

    # So even if it catches the exception the connection closes    
    finally:
        cursor.close()
        db.close_connection()

    return products_info

def execute_insert(cursor, name, nutri_score, nova_score, green_score):

    insert_data = f"""INSERT INTO products (name, nutri_score, nova_score, green_score) 
        VALUES (%s, %s, %s, %s);"""

    data_product = (name, nutri_score, nova_score, green_score)

    # Insert data in DB:
    cursor.execute(insert_data, data_product)

def insert_one_product(name, nutri_score, nova_score, green_score):
    db = Database()
    conn = db.get_connection()
    cursor = conn.cursor()

    execute_insert(cursor, name, nutri_score, nova_score, green_score)
        
    conn.commit()
    cursor.close()
    db.close_connection()

# Insert data. This function receives a zip object.
def insert_products(products):
    db = Database()
    conn = db.get_connection()
    cursor = conn.cursor()

    # Create the query to insert the products
    for name, nutri_score, nova_score, green_score in products:
        execute_insert(cursor, name, nutri_score, nova_score, green_score)
        
    conn.commit()
    cursor.close()
    db.close_connection()


