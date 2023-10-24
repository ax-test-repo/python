import os
import sqlite3

from config import BASE_DIR


db_path = os.path.join(BASE_DIR, "sql", "pet_store.db")

def create_db():
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        query = """
            CREATE TABLE IF NOT EXISTS users (
        id INT NOT NULL,
        username VARCHAR(30) NOT NULL,
        first_name VARCHAR(30) NOT NULL,
        last_name VARCHAR(30) NOT NULL,
        email VARCHAR(100) NOT NULL,
        password VARCHAR(30) NOT NULL,
        phone VARCHAR(20) NOT NULL,
        PRIMARY KEY (id)
        );
        """
        cursor.execute(query)
        connection.commit()

def get_user_name(id):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    query ="""SELECT username
            FROM users
            WHERE id = ?"""
    cursor.execute(query, (id,))
    user_name = cursor.fetchone()[0]
    connection.close()
    return user_name

def create_valid_user():
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        query = """INSERT INTO users
                (id, username, first_name, last_name, email, password, phone)
                VALUES(1, 'valid_user', 'first_valid_user', 'last_valid_user', 'email@valid.user', 'password_valid_user', '89123344440404');"""
        cursor.execute(query)
        connection.commit()

def delete_valid_user():
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        query ="""DELETE FROM users WHERE id=1;"""
        cursor.execute(query)
        connection.commit()
