# db/database.py
import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='house_app'
        )
        print("Connexion à MySQL réussie")
        return connection
    except Error as e:
        print(f"Erreur de connexion à MySQL: {e}")
        return None

def verify_user(connection, username, password):
    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        return user
    except Error as e:
        print(f"Erreur lors de la vérification de l'utilisateur: {e}")
        return None
    finally:
        if cursor:
            cursor.close()


# db/database.py
def create_user(connection, username, password, email=None, full_name=None):
    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO users (username, password, email, full_name)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (username, password, email, full_name))
        connection.commit()
        return True
    except Error as e:
        print(f"Erreur création utilisateur: {e}")
        return False
    finally:
        if cursor:
            cursor.close()


