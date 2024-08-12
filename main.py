from typing import Optional

class UserProfile:
    def __init__(self, user_id: int, name: str, age: int, gender: str, location: str, interests: list[str]) -> None:
        """
        Initialize a user profile. 
        """
        self.user_id = user_id
        self.name = name
        self.age = age
        self.gender = gender
        self.location = location
        self.interests = interests

    def update_profile(self, name: str, age: int, gender: str, location: str, interests: list[str]) -> None:
        """
        Update the user profile with the provided details. All details must be provided.
        """
        self.name = name
        self.age = age
        self.gender = gender
        self.location = location
        self.interests = interests
        print(f"User {self.user_id} updated successfully!")

    def view_profile(self) -> None:
        """
        Print the user profile details. 
        """
        print(f"ID: {self.user_id}, Name: {self.name}, Age: {self.age}, "
              f"Gender: {self.gender}, Location: {self.location}, "
              f"Interests: {', '.join(self.interests)}")

class UserManager:
    def __init__(self) -> None:
        self.users = {
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

    def add_user(self, user_id: int, name: str, age: int, gender: str, location: str, interests: list[str]) -> None:
        """
        Add a new user profile.
        """
        if user_id in self.users:
            print(f"User ID {user_id} already exists.")
        else:
            self.users[user_id] = UserProfile(user_id, name, age, gender, location, interests)
            print(f"User {user_id} added successfully!")

    # Pick one of the following methods to update the user profile
    # Need to input all details to update the profile, even if only one detail is changed
    def update_user(self, user_id: int, name: str, age: int, gender: str, location: str, interests: list[str]) -> None:
        """
        Update an existing user profile.
        """
        if user_id in self.users:
            self.users[user_id].update_profile(name, age, gender, location, interests)
        else:
            print(f"User ID {user_id} does not exist.")

    # Only need to input the details that need to be updated
    def update_user(self, user_id: int, name: Optional[str] = None, age: Optional[int] = None, gender: Optional[str] = None, 
    location: Optional[str] = None, interests: Optional[list[str]] = None) -> None:
        """
        Update an existing user profile. Only provided details will be updated.
        """
        if user_id in self.users:
            user = self.users[user_id]
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
            print(f"User {user_id} updated successfully!")
        else:
            print(f"User ID {user_id} does not exist.")    

    def view_user(self, user_id: int) -> None:
        """
        View an existing user profile.
        """
        if user_id in self.users:
            self.users[user_id].view_profile()
        else:
            print(f"User ID {user_id} does not exist.")