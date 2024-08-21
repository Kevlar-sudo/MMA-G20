# MMA RSM8431Y - Matching U App Documentation - Group20 
### Contributors: Kevin Abdo, Yuze Li, Kevin Liu, Ruohan Wang, Emily Zhong
### Instructor: Prof. Arik Senderovich
### Course: RSM8431 Introduction to Computer Science with Python 

## Description
Matching U apps aim to build a bridge for adults, who want to explore and start their love journeys. Matching U focuses on helping users find the best partner based on three main considerations: age, location, and interests. When new users open the Matching U app, they can easily start by entering personal information and preferences such as age, gender, and interest to create their own profile. Then, with the unique user ID and name, they can log in to the Matching U app. Next, there are several actions that the user can take, including editing and viewing their own profile, viewing other users' profiles, liking and disliking other users, deleting their own profile, and logging out. The matching U app will use the algorithm to recommend potential matches to the current users

 
 ## Usage
 ### Data Structure: UserProfile class 
The User Profile class is created to show each user's profile in the system, combined with the following attributes:
- user_id (int): A unique identifier for the user, auto-assigned by the database. 
- name (str): The name of the user.
- age (int): The user's age.
- gender (str): The user's gender, typically represented as "M" or "F".
- location (str): The city, where the user lives.
- interests (list of str): A list of the user's interests, like "yoga, swimming", "reading", "cooking", etc.
- liked_users (list of int): A list of user IDs that this user has liked.
- disliked_users (list of int): A list of user IDs that this user has disliked.
- matched_users (list of int): A list of user IDs that have been mutually matched with this user.

 
### Database Integration:

SQLite database is created by the function *create_table* to store user profiles and their actions. 

The system uses the SQLite database for persistent storage of user data and interactions. Python's built-in SQLite3library is used to perform all database operations, including creating, reading, updating, and deleting (CRUD) user profiles and their associated data. After the creation of the database, we perform **CRUD** operations:


- C:
*save_to_db*: create user profiles in the database.


- R:
*user_exists*: extract users' profiles and actions in the database.


- U: 
  - *like_user*: Updates the list of users that the current user has liked. If both users like each other, they are added to each other's match lists.
  - *_add_to_matches*: Updates the list of matched users when two users mutually like each other. The matched user ID is added to the current user's match list and saved in the database.
  - *dislike_user*: Updates the list of users that the current user has disliked. This ensures that the disliked user is not shown again in recommendations.
  - *update_user*: Updates the current user's profile information in the database. This includes modifying attributes such as the user's name, age, gender, location, and interests. The updated information is saved back to the SQLite database, ensuring that any changes the user makes to their profile are reflected in future interactions and queries.

- D:
*delete_user*: delete the current user and remove the current user’s follow-up effects.

 
 ## Feature









 
 
 ## Tools
### Pandas DataFrame:
The user data will be loaded in the Pandas Dataframe temporarily when doing some complicated operations like computing the compatibility scores between users. The DataFrame allows for vectorized operations and quick comparisons, with columns representing user attributes (age, gender, interests) and interaction data (liked, disliked, and matched users).

### Dictionaries and Lists:
- Dictionaries are applied to store user information and present results in most cases, for example, it allow us to fetch user profiles or find interest similarities. 
- Lists are applied to store liked, disliked, and matched user IDs in the user profiles. 








 
 ## Contact Information
 
 
 
