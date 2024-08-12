import sqlite3
from typing import Optional, List

class UserProfile:
    def __init__(self, user_id: int, name: str, age: int, gender: str, location: str, interests: List[str]) -> None:
        self.user_id = user_id
        self.name = name
        self.age = age
        self.gender = gender
        self.location = location
        self.interests = interests

    def save_to_db(self, conn: sqlite3.Connection) -> None:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (user_id, name, age, gender, location, interests)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (self.user_id, self.name, self.age, self.gender, self.location, ','.join(self.interests)))
        conn.commit()

    def update_profile(self, conn: sqlite3.Connection, name: Optional[str] = None, age: Optional[int] = None, 
                       gender: Optional[str] = None, location: Optional[str] = None, 
                       interests: Optional[List[str]] = None) -> None:
        cursor = conn.cursor()
        
        # Retrieve current values if not provided
        cursor.execute("SELECT name, age, gender, location, interests FROM users WHERE user_id = ?", (self.user_id,))
        current_values = cursor.fetchone()
        if current_values:
            current_name, current_age, current_gender, current_location, current_interests = current_values
            self.name = name if name is not None else current_name
            self.age = age if age is not None else current_age
            self.gender = gender if gender is not None else current_gender
            self.location = location if location is not None else current_location
            self.interests = interests if interests is not None else current_interests.split(',')

            # Update the database
            cursor.execute("""
                UPDATE users
                SET name = ?, age = ?, gender = ?, location = ?, interests = ?
                WHERE user_id = ?
            """, (self.name, self.age, self.gender, self.location, ','.join(self.interests), self.user_id))
            conn.commit()
            print(f"User {self.user_id} updated successfully!")
        else:
            print(f"User {self.user_id} not found!")

    def view_profile(self) -> None:
        print(f"ID: {self.user_id}, Name: {self.name}, Age: {self.age}, "
              f"Gender: {self.gender}, Location: {self.location}, "
              f"Interests: {', '.join(self.interests)}")
        
class UserManager:
    def __init__(self, db_path: str) -> None:
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self) -> None:
        cursor = self.conn.cursor()
        cursor.execute("""
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
        """)
        self.conn.commit()

    def add_user(self, user_id: int, name: str, age: int, gender: str, location: str, interests: List[str]) -> None:
        if self.user_exists(user_id):
            print(f"User ID {user_id} already exists.")
        else:
            user = UserProfile(user_id, name, age, gender, location, interests)
            user.save_to_db(self.conn)
            print(f"User {user_id} added successfully!")

    def user_exists(self, user_id: int) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("SELECT 1 FROM users WHERE user_id = ?", (user_id,))
        return cursor.fetchone() is not None

    def update_user(self, user_id: int, name: Optional[str] = None, age: Optional[int] = None, gender: Optional[str] = None, 
                    location: Optional[str] = None, interests: Optional[List[str]] = None) -> None:
        if self.user_exists(user_id):
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
            row = cursor.fetchone()
            user = UserProfile(row[0], row[1], row[2], row[3], row[4], row[5].split(','))
            if name is not None:
                user.name = name
            if age is not None:
                user.age = age
            if gender is not None:
                user.gender = gender
            if location is not None:
                user.location = location
            if interests is not None:
                user.interests = interests
            user.update_profile(self.conn, user.name, user.age, user.gender, user.location, user.interests)
        else:
            print(f"User ID {user_id} does not exist.")

    def view_user(self, user_id: int) -> None:
        if self.user_exists(user_id):
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
            row = cursor.fetchone()
            user = UserProfile(row[0], row[1], row[2], row[3], row[4], row[5].split(','))
            user.view_profile()
        else:
            print(f"User ID {user_id} does not exist.")

    def delete_user(self, user_id: int) -> None:
        if self.user_exists(user_id):
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
            self.conn.commit()
            print(f"User {user_id} deleted successfully!")
        else:
            print(f"User ID {user_id} does not exist.")

    def view_all_users(self) -> None:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            user = UserProfile(row[0], row[1], row[2], row[3], row[4], row[5].split(','))
            user.view_profile()

    def initialize_users(self) -> None:
        predefined_users = {
            1: UserProfile(1, "Alice", 30, "Female", "New York", ["reading", "coding"]),
            2: UserProfile(2, "Bob", 25, "Male", "San Francisco", ["hiking", "gaming"]),
            3: UserProfile(3, "Charlie", 28, "Male", "Los Angeles", ["music", "sports", "traveling"]),
            4: UserProfile(4, "Diana", 22, "Female", "Chicago", ["art", "traveling"]),
            5: UserProfile(5, "Eve", 35, "Female", "Houston", ["cooking", "gardening"]),
            6: UserProfile(6, "Frank", 27, "Male", "Phoenix", ["photography", "cycling", "fishing"]),
            7: UserProfile(7, "Grace", 24, "Female", "Philadelphia", ["writing", "yoga"]),
            8: UserProfile(8, "Hank", 32, "Male", "San Antonio", ["fishing", "hiking"]),
            9: UserProfile(9, "Ivy", 29, "Female", "San Diego", ["dancing", "painting"]),
            10: UserProfile(10, "Jack", 26, "Male", "Dallas", ["gaming"]),
            11: UserProfile(11, "Karen", 31, "Female", "San Jose", ["reading", "swimming"]),  
            12: UserProfile(12, "Leo", 23, "Male", "Austin", ["running", "music"]),
            13: UserProfile(13, "Mona", 34, "Female", "Jacksonville", ["traveling", "photography"]),
            14: UserProfile(14, "Nate", 28, "Male", "Fort Worth", ["sports", "gaming", "hiking", "reading"]),
            15: UserProfile(15, "Olivia", 27, "Female", "Columbus", ["yoga", "cooking"])
        }
        for user in predefined_users.values():
            manager.add_user(user.user_id, user.name, user.age, user.gender, user.location, user.interests)

if __name__ == "__main__":
    manager = UserManager("users.db")
    
    # Add sample users
    manager.initialize_users()
