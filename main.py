import sqlite3
from typing import Optional, List

"""GUI Library"""
from tkinter import *
from tkinter import messagebox

class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Dating App Name")


    def menu_label(self):
        self.label = Label(self.window, text="Welcome to (Dating App Name)", font=('Arial', 16))
        self.label.grid(row=0, column=0, columnspan=3)

    def menu_canvas(self):
        self.canvas = Canvas(height=512, width=512)
        logo_png = PhotoImage(file="logo.png")
        self.image_id = self.canvas.create_image(256, 256, image=logo_png)
        self.canvas.grid(row=1, column=0, columnspan=3)

    def menu_buttons(self):
        self.new_bottom = Button(self.window, text="New User", font=('Arial', 16), command=self.create_new)
        self.new_bottom.grid(row=2, column=0)

        self.existing_bottom = Button(self.window, text="Existing User", font=('Arial', 16), command=self.log_in)
        self.existing_bottom.grid(row=2, column=2)

    def register_label(self):
        self.label = Label(self.window, text="Please Enter Your Info to Register", font=('Arial', 16))
        self.label.grid(row=0, column=0, columnspan=3)

    def register_canvas(self):
        self.canvas.delete("all")
        '''create user info entry boxes'''
        self.name_entry = Entry(self.window, font=('Arial', 16), width=24)
        self.age_entry = Entry(self.window, font=('Arial', 16), width=8)
        self.gender = StringVar(self.window)
        self.gender_entry = OptionMenu(self.window, self.gender, "M", "F")
        self.location_entry = Entry(self.window, font=('Arial', 16), width=24)
        self.interests_entry = Entry(self.window, font=('Arial', 16), width=36)

        self.canvas.create_window(300, 100, window=self.name_entry)
        self.canvas.create_window(204, 150, window=self.age_entry)
        self.canvas.create_window(172, 200, window=self.gender_entry)
        self.canvas.create_window(300, 250, window=self.location_entry)
        self.canvas.create_window(256, 350, window=self.interests_entry)
        self.canvas.create_text(100, 100, text="Name", font=('Arial', 16))
        self.canvas.create_text(100, 150, text="Age", font=('Arial', 16))
        self.canvas.create_text(100, 200, text="Gender", font=('Arial', 16))
        self.canvas.create_text(100, 250, text="Location", font=('Arial', 16))
        self.canvas.create_text(256, 300, text="Interests (Please separate your interests by comma)",
                                font=('Arial', 16))

    def register_buttons(self):
        '''remove logo and buttons from menu page'''
        self.new_bottom.grid_forget()
        self.existing_bottom.grid_forget()

        '''create new create_user button, check if all entry boxes are filled'''
        self.create_user = Button(self.window, text="Complete My Profile", font=('Arial', 16),
                                  command=self.check_profile)
        self.create_user.grid(row=2, column=2)

    def log_in_label(self):
        self.label = Label(self.window, text="Log In to Your Account", font=('Arial', 16))
        self.label.grid(row=0, column=0, columnspan=3)

    def log_in_canvas(self):
        self.canvas.delete("all")
        '''create user log in entry boxes'''
        self.name_entry = Entry(self.window, font=('Arial', 16), width=24)
        self.id_entry = Entry(self.window, font=('Arial', 16), width=8)

        self.canvas.create_window(300, 200, window=self.name_entry)
        self.canvas.create_window(204, 150, window=self.id_entry)

        self.canvas.create_text(100, 200, text="Name", font=('Arial', 16))
        self.canvas.create_text(100, 150, text="User ID", font=('Arial', 16))


    def log_in_buttons(self):
        '''remove logo and buttons from menu page'''
        self.new_bottom.grid_forget()
        self.existing_bottom.grid_forget()

        '''log in as existing user, check if the user exist'''
        self.create_user = Button(self.window, text="Log In", font=('Arial', 16))
        self.create_user.grid(row=2, column=2)

    def create_new(self):
        self.register_label()
        self.register_canvas()
        self.register_buttons()

    def log_in(self):
        self.log_in_label()
        self.log_in_canvas()
        self.log_in_buttons()

    def check_profile(self):
        user_name = self.name_entry.get()
        user_age = self.age_entry.get()
        user_gender = self.gender.get()
        user_location = self.location_entry.get()
        user_interests = self.interests_entry.get()


        user_profile = [user_name,user_age,user_gender,user_location,user_interests]
        complete = True
        for info in user_profile:
            if len(info) == 0:
                complete = False
                break
        if not complete:
            messagebox.showinfo(title="Oops", message="Please make sure you fill all the boxes")
        else:
            #self.user_label()
            self.profile_canvas(user_profile)
            #self.user_button()
            """pass the profile to the update_profile function in the UserProfile Class"""
            manager.add_user(user_profile)

    def profile_canvas(self, profile):

        """clear the canvas to show the user profile details"""
        self.canvas.delete("all")

        self.canvas.create_text(100, 100, text="Name", font=('Arial', 16))
        self.canvas.create_text(100, 150, text="Age", font=('Arial', 16))
        self.canvas.create_text(100, 200, text="Gender", font=('Arial', 16))
        self.canvas.create_text(100, 250, text="Location", font=('Arial', 16))
        self.canvas.create_text(100, 300, text="Interests", font=('Arial', 16))

        user_name = profile[0]
        user_age = profile[1]
        user_gender = profile[2]
        user_location = profile[3]
        user_interests = profile[4]
        print(user_name,user_age,user_gender,user_location,user_interests)

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

""" # Add sample users
    manager.initialize_users()
    """

UI = GUI()

UI.menu_label()
UI.menu_canvas()
UI.menu_buttons()

UI.window.mainloop()