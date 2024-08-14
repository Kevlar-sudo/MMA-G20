import sqlite3
from typing import Optional, List
from tkinter import *
from tkinter import messagebox
from geopy.geocoders import Nominatim
from geopy.distance import geodesic



#Button commands should call the function UserManager class and functions in the UserManager class should call UI functions to display info and inputs/command from user.

class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Dating App Name")
        self.canvas = Canvas(height=512, width=512)
        self.commandcanvas = Canvas(height = 128, width = 512)
        self.logo_png = PhotoImage(file="logo.png")
        self.label = Label(self.window, text="Welcome to (Dating App Name)", font=('Arial', 16))
        self.label.grid(row=0, column=0)

    def menu_page(self):
        self.label.destroy()
        self.label = Label(self.window, text="Welcome to (Dating App Name)", font=('Arial', 16))
        self.label.grid(row=0, column=0)

        self.canvas.delete("all")
        self.canvas.create_image(256, 256, image=self.logo_png)
        self.canvas.grid(row=1, column=0)

        self.commandcanvas.delete("all")

        self.new_button = Button(self.window, text="New User", font=('Arial', 16), command=self.register_page)
        self.commandcanvas.create_window(100,30,window=self.new_button)

        self.existing_button = Button(self.window, text="Existing User", font=('Arial', 16), command=self.log_in_page)
        self.commandcanvas.create_window(400,30,window=self.existing_button)

        self.commandcanvas.grid(row=2, column=0)
        '''
        self.compare_button = Button(self.window, text="Compare Users", font=('Arial', 16), command=self.compare_users)
        self.compare_button.grid(row=3, column=1)'''

    def register_page(self):
        self.label.destroy()
        self.label = Label(self.window, text="Please Enter Your Info to Register", font=('Arial', 16))
        self.label.grid(row=0, column=0)

        self.canvas.delete("all")
        #Create user info entry boxes
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

        #remove buttons from menu page
        self.commandcanvas.delete("all")

        self.create_user = Button(self.window, text="Complete My Profile", font=('Arial', 16),
                                  command=self.check_profile)
        self.commandcanvas.create_window(400,30,window=self.create_user)

        #create new create_user button, check if all entry boxes are filled

    def log_in_page(self):
        self.label.destroy()
        self.label = Label(self.window, text="Log In to Your Account", font=('Arial', 16))
        self.label.grid(row=0, column=0)

        #Create user log in entry boxes
        self.canvas.delete("all")
        self.name_entry = Entry(self.window, font=('Arial', 16), width=24)
        self.id_entry = Entry(self.window, font=('Arial', 16), width=8)

        self.canvas.create_window(300, 200, window=self.name_entry)
        self.canvas.create_window(204, 150, window=self.id_entry)

        self.canvas.create_text(100, 200, text="Name", font=('Arial', 16))
        self.canvas.create_text(100, 150, text="User ID", font=('Arial', 16))

        #Remove buttons from menu page
        self.commandcanvas.delete("all")

        #log in as existing user, check if the user exist
        self.user_log_in = Button(self.window, text="Log In", font=('Arial', 16), command = self.check_log_in)
        self.commandcanvas.create_window(400,30,window=self.user_log_in)


    def check_profile(self):
        user_name = self.name_entry.get()
        user_age = self.age_entry.get()
        user_gender = self.gender.get()
        user_location = self.location_entry.get()
        user_interests = self.interests_entry.get()

        user_profile = [user_name, user_age, user_gender, user_location, user_interests]
        complete = True
        for info in user_profile:
            if len(info) == 0:
                complete = False
                break
        if not complete:
            messagebox.showinfo(title="Oops", message="Please make sure you fill all the boxes")
        elif user_age.isnumeric() == False:
            messagebox.showinfo(title="Oops", message="Age should be a number")
        else:
            #pass the profile to the update_profile function in the UserProfile Class
            manager.add_user(None, user_name, int(user_age), user_gender, user_location, user_interests.split(','))

    def check_log_in(self):
        user_name = self.name_entry.get()
        user_id = self.id_entry.get()

        if len(user_id) == 0 or len(user_name) == 0:
            messagebox.showinfo(title="Oops", message="Please make sure you fill all the boxes")
        elif user_id.isnumeric() == False:
            messagebox.showinfo(title="Oops", message="ID should be a number")
        else:
            user_result = manager.user_exists(int(user_id), user_name)
            print(user_result)
            if user_result== False:
                messagebox.showinfo(title="Oops", message="User does not exist")
            else:
                self.profile_page(user_result)




    def profile_page(self, current_user):
        self.label.destroy()
        self.label = Label(self.window, text=f"{current_user.name}, Welcome Back!", font=('Arial', 16))
        self.label.grid(row=0, column=0)

        #clear the canvas to show the user profile details
        self.canvas.delete("all")

        self.canvas.create_text(100, 100, text="User ID", font=('Arial', 16))
        self.canvas.create_text(100, 150, text="Name", font=('Arial', 16))
        self.canvas.create_text(100, 200, text="Age", font=('Arial', 16))
        self.canvas.create_text(100, 250, text="Gender", font=('Arial', 16))
        self.canvas.create_text(100, 300, text="Location", font=('Arial', 16))
        self.canvas.create_text(100, 350, text="Interests", font=('Arial', 16))

        self.canvas.create_text(300, 100, text=current_user.user_id, font=('Arial', 16))
        self.canvas.create_text(300, 150, text=current_user.name, font=('Arial', 16))
        self.canvas.create_text(300, 200, text=current_user.age, font=('Arial', 16))
        self.canvas.create_text(300, 250, text=current_user.gender, font=('Arial', 16))
        self.canvas.create_text(300, 300, text=current_user.location, font=('Arial', 16))
        self.canvas.create_text(300, 350, text=','.join(current_user.interests), font=('Arial', 16))

        # Remove buttons from previous page
        self.commandcanvas.delete("all")

        # show user options
        self.user_log_out = Button(self.window, text="Log Out", font=('Arial', 16), command=self.menu_page)
        self.commandcanvas.create_window(90, 30, window=self.user_log_out)

        self.user_browse = Button(self.window, text="Start Browsing", font=('Arial', 16))
        self.commandcanvas.create_window(230, 30, window=self.user_browse)

        self.user_update = Button(self.window, text="Update Profile", font=('Arial', 16))
        self.commandcanvas.create_window(400, 30, window=self.user_update)

        self.user_liked = Button(self.window, text="Liked User", font=('Arial', 16))
        self.commandcanvas.create_window(90, 80, window=self.user_liked)

        self.user_disliked = Button(self.window, text="Disliked User", font=('Arial', 16))
        self.commandcanvas.create_window(230, 80, window=self.user_disliked)

        self.user_matched = Button(self.window, text="Matched User", font=('Arial', 16))
        self.commandcanvas.create_window(400, 80, window=self.user_matched)


    def compare_users(self):
        user_id1 = int(self.id_entry.get())
        self.compare_id_entry = Entry(self.window, font=('Arial', 16), width=8)
        self.compare_id_entry.grid(row=3, column=2)

        compare_button = Button(self.window, text="Get Compatibility", font=('Arial', 16),
                                command=lambda: manager.compare_users(user_id1, int(self.compare_id_entry.get())))
        compare_button.grid(row=3, column=3)


class UserProfile:
    def __init__(self, user_id: int, name: str, age: int, gender: str, location: str, interests: List[str]) -> None:
        self.user_id = user_id
        self.name = name
        self.age = age
        self.gender = gender
        self.location = location
        self.interests = interests
        self.geolocator = Nominatim(user_agent="dating_app")

    def get_location_coordinates(self, location: str):
        location_data = self.geolocator.geocode(location)
        if location_data:
            return (location_data.latitude, location_data.longitude)
        else:
            return None

    def calculate_distance(self, other_user: 'UserProfile') -> Optional[float]:
        self_coords = self.get_location_coordinates(self.location)
        other_coords = other_user.get_location_coordinates(other_user.location)
        if self_coords and other_coords:
            return geodesic(self_coords, other_coords).kilometers
        else:
            return None

    def calculate_compatibility(self, other_user: 'UserProfile') -> Optional[float]:
        distance = self.calculate_distance(other_user)
        if distance is not None:
            max_distance = 5000  # Define a max distance to normalize the score
            compatibility_score = max(0, (max_distance - distance) / max_distance) * 100
            return round(compatibility_score, 2)
        else:
            return None

    def save_to_db(self, conn: sqlite3.Connection) -> None:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (name, age, gender, location, interests)
            VALUES (?, ?, ?, ?, ?)
        """, (self.name, self.age, self.gender, self.location, ','.join(self.interests)))
        self.user_id = cursor.lastrowid
        conn.commit()

    def update_profile(self, conn: sqlite3.Connection, name: Optional[str] = None, age: Optional[int] = None, 
                       gender: Optional[str] = None, location: Optional[str] = None, 
                       interests: Optional[List[str]] = None) -> None:
        cursor = conn.cursor()
        #Retrieve the current values if not provided
        cursor.execute("SELECT name, age, gender, location, interests FROM users WHERE user_id = ?", (self.user_id,))
        current_values = cursor.fetchone()
        if current_values:
            current_name, current_age, current_gender, current_location, current_interests = current_values
            self.name = name if name is not None else current_name
            self.age = age if age is not None else current_age
            self.gender = gender if gender is not None else current_gender
            self.location = location if location is not None else current_location
            self.interests = interests if interests is not None else current_interests.split(',')

            #Update the database
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
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
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

    def add_user(self, user_id: Optional[int], name: str, age: int, gender: str, location: str, interests: List[str]) -> None:
        user = UserProfile(user_id, name, age, gender, location, interests)
        user.save_to_db(self.conn)
        print(f"User {user.user_id} added successfully!")
        UI.profile_page(user)

    def user_exists(self, user_id: int, user_name: str):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        row1 = cursor.fetchone()
        if not row1:
            return False
        else:
            if row1[1] != user_name:
                return False
            else:
                user1 = UserProfile(row1[0], row1[1], row1[2], row1[3], row1[4], row1[5].split(','))
                return user1

    def like_user(self, current_user_id: int, liked_user_id: int) -> None:
        cursor = self.conn.cursor()
        cursor.execute("SELECT liked_users FROM users WHERE user_id = ?", (current_user_id,))
        liked_users = cursor.fetchone()[0]
        
        if liked_users:
            liked_users_list = liked_users.split(',')
        else:
            liked_users_list = []
        
        if str(liked_user_id) not in liked_users_list:
            liked_users_list.append(str(liked_user_id))
            cursor.execute("""
                UPDATE users 
                SET liked_users = ?
                WHERE user_id = ?
            """, (','.join(liked_users_list), current_user_id))
            self.conn.commit()
            print(f"User {current_user_id} liked user {liked_user_id}")
        else:
            print(f"User {current_user_id} has already liked user {liked_user_id}")

    def dislike_user(self, current_user_id: int, disliked_user_id: int) -> None:
        cursor = self.conn.cursor()
        cursor.execute("SELECT disliked_users FROM users WHERE user_id = ?", (current_user_id,))
        disliked_users = cursor.fetchone()[0]
        
        if disliked_users:
            disliked_users_list = disliked_users.split(',')
        else:
            disliked_users_list = []

        if str(disliked_user_id) not in disliked_users_list:
            disliked_users_list.append(str(disliked_user_id))
            cursor.execute("""
                UPDATE users 
                SET disliked_users = ?
                WHERE user_id = ?
            """, (','.join(disliked_users_list), current_user_id))
            self.conn.commit()
            print(f"User {current_user_id} disliked user {disliked_user_id}")
        else:
            print(f"User {current_user_id} has already disliked user {disliked_user_id}")


    def compare_users(self, user_id1: int, user_id2: int) -> None:
        if self.user_exists(user_id1) and self.user_exists(user_id2):
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id1,))
            row1 = cursor.fetchone()
            user1 = UserProfile(row1[0], row1[1], row1[2], row1[3], row1[4], row1[5].split(','))

            cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id2,))
            row2 = cursor.fetchone()
            user2 = UserProfile(row2[0], row2[1], row2[2], row2[3], row2[4], row2[5].split(','))

            compatibility_score = user1.calculate_compatibility(user2)
            if compatibility_score is not None:
                print(f"The compatibility score between User {user1.name} and User {user2.name} is: {compatibility_score}%")
            else:
                print("Unable to calculate compatibility score due to missing location data.")
        else:
            print("One or both user IDs do not exist.")

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

if __name__ == "__main__":
    manager = UserManager("users.db")

    '''
    # Add test users (You can comment these out later)
    manager.add_user(None, "Alice", 30, "F", "New York", ["reading", "coding"])
    manager.add_user(None, "Bob", 25, "M", "Los Angeles", ["hiking", "gaming"])
    manager.add_user(None, "Charlie", 28, "M", "Chicago", ["music", "sports", "traveling"])
    '''


    UI = GUI()
    UI.menu_page()

    UI.window.mainloop()

