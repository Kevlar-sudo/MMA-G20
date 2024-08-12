import sqlite3
import os

def setup_database():

    db_file = 'users.db'
    
    # If DB exists - delete it upon setup:
    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"Deleted existing database file: {db_file}")
    
    # Create a connection to the SQLite database
    conn = sqlite3.connect(db_file)
    print(f"Created database file: {db_file}")

    # Create a cursor object
    cursor = conn.cursor()

    # Create a table for storing user information
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            gender TEXT,
            location TEXT,
            interests TEXT,
            liked_users TEXT,
            disliked_users TEXT,
            matches TEXT
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()
    print(f"Database setup completed and connection closed.")

# Run the function to set up the database
setup_database()


  