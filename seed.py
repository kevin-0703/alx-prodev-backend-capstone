#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error
import csv
import uuid
import requests
import io


def connect_db():
    """Connect to MySQL server (without specifying database)."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="alxprodevadmin",        
            password="alxprodev"     
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def create_database(connection):
    """Create ALX_prodev database if it does not exist."""
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
        print("Database ALX_prodev created successfully (if not existed)")
    except Error as e:
        print(f"Error creating database: {e}")


def connect_to_prodev():
    """Connect directly to ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="alxprodevadmin",        # change to your MySQL username
            password="alxprodev",    # change to your MySQL password
            database="ALX_prodev"
        )
        return connection
    except Error as e:
        print(f"Error connecting to ALX_prodev: {e}")
        return None


def create_table(connection):
    """Create user_data table with required fields."""
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL NOT NULL,
                INDEX (user_id)
            );
        """)
        connection.commit()
        print("Table user_data created successfully")
    except Error as e:
        print(f"Error creating table: {e}")


def insert_data(connection, csv_url):
    """Insert CSV data from a remote URL into user_data table if not already exists."""
    try:
        cursor = connection.cursor()

        # Fetch CSV from the remote URL
        response = requests.get(csv_url)
        response.raise_for_status()  # raise exception if failed

        # Convert response content into a file-like object
        csv_file = io.StringIO(response.text)
        reader = csv.DictReader(csv_file)

        inserted = 0
        skipped = 0

        for row in reader:
            user_id = str(uuid.uuid4())
            name = row["name"]
            email = row["email"]
            age = row["age"]

            # Check if email already exists (avoid duplicates)
            cursor.execute("SELECT * FROM user_data WHERE email = %s", (email,))
            if not cursor.fetchone():
                cursor.execute("""
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                """, (user_id, name, email, age))
                inserted += 1
            else:
                skipped += 1

        connection.commit()
        print(f"Data inserted successfully from remote CSV ({inserted} new, {skipped} skipped)")
    except Exception as e:
        print(f"Error inserting data: {e}")
