# MMA RSM8431Y - Matching App Documentation - Group20 
### Contributors: Kevin Abdo, Yuze Li, Kevin Liu, Ruohan Wang, Emily Zhong
### Instructor: Prof. Arik Senderovich
### Course: RSM8431 Introduction to Computer Science with Python 

## Description
Matching U apps aim to build a bridge for adults, who want to explore and start their love journeys. Matching U focuses on helping users find the best partner based on three main considerations: age, location, and interests. When new users open the Matching U app, they can easily start by entering personal information and preferences such as age, gender, and interest to create their own profile. Then, with the unique user ID and name, they are able to log in to the Matching U app. Next, there are several actions that the user can take, including editing and viewing their profile, viewing other users' profiles, liking and disliking other users, deleting their own profile, and logging out. The matching U app will use the algorithm to recommend potential matches to the current users

 
 ## Usage
 ### Data Structure: UserProfile class 
The User Profile class is created to show each user's profile in the system, combined with following attributes:
- user_id (int): A unique identifier for the user, auto-assigned by the database. 
- name (str): The name of the user.
- age (int): The user's age.
- gender (str): The user's gender, typically represented as "M" or "F".
- location (str): The city, where the user lives.
- interests (list of str): A list of the user's interests, like "yoga, swimming", "reading", "cooking", etc.
- liked_users (list of int): A list of user IDs that this user has liked.
- disliked_users (list of int): A list of user IDs that this user has disliked.
- matched_users (list of int): A list of user IDs that have been mutually matched with this user.

 











 
 ## Feature









 
 
 ## Tools
Pandas DataFrame:
When conducting complex operations like computing compatibility scores between users or generating recommendations, user data is temporarily loaded into a Pandas DataFrame. The DataFrame allows for vectorized operations and quick comparisons, with columns representing user attributes (age, gender, interests) and interaction data (liked, disliked, and matched users).

Dictionaries and Lists:
In various parts of the application, dictionaries are used to store user information and lookup results, particularly when fetching user profiles or calculating interest similarities. Lists are also used within the user profiles to store liked, disliked, and matched user IDs.








 
 ## Contact Information
 
 
 
