import mysql.connector
import os

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._connect()
        return cls._instance

    def _connect(self):
        """Create the connection to MySQL using environment variables or default values"""
        self.conn = mysql.connector.connect(
            host=os.environ.get("DB_HOST", "127.0.0.1"),
            user=os.environ.get("DB_USER", "fooduser"),
            password=os.environ.get("DB_PASSWORD", "password123"),
            database=os.environ.get("DB_NAME", "foodtech"),
            port=os.environ.get("PORT", "3307")
        )

    def get_connection(self):
        """Return the active connection"""
        if not self.conn.is_connected():
            self._connect()
        return self.conn

    def close_connection(self):
        """Close the connection and restart the instance"""
        if self.conn.is_connected():
            self.conn.close()
        Database._instance = None


# Ús recomanat:

# db = Database()                  # Obtenir instància singleton
# conn = db.get_connection()       # Obtenir connexió
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM products")
# results = cursor.fetchall()
# db.close_connection()            # Tancar connexió quan acabis