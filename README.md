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



### Data Structure: User Profile Management
In the user profile, users’ information, including individual user ID, name, age, gender, located city, interest, and other information, including a list of liked users, a list of disliked users, and a list of matched users will be stored and updated as well. Current user’s information will be stored in the database through SQLite connection.

- *add_user*: A new user profile will be added through to store the new user’s information in the database. 
- *user_exists*: To view an existing user profile, a given user id will be searched and will return the searching user’s a list of different information, otherwise, it will return a warning message.
- *update_user*: Users can edit their profile information. The user’s existing profile will be extracted from the database, and the updated information, such as name, age, gender, location, and interests, will replace the old data. The changes will then be saved back to the database.
- *delete_user*: A user profile will be removed. This function deletes the user’s profile from the database, and all references to the user in other users’ liked, disliked, and matched lists will be cleared as well.

### User Interaction
- *liked_user*: The other user ID will be checked or added to the list of current users’ “liked_user” if the list does not contain the other user ID. Moreover, if both users like each other, then each user will be added to the other’s like list and both return TRUE, otherwise, return False for the user who dislikes.
- *dislike_user*: If the other user ID is not in the matching list, then the new dislike user ID will be added to the list and then updated to the database. 
- *_add_to_matches*: If the matched user ID is not in the matching list, then the new matched user ID will be added to the list and then updated to the database. 
- *compare_users*: If both users' existence is validated, then two user profiles will be created, and further calculated the compatibility scores between the two users. If one or both users do not exist, then an error message will be printed.
- *recommend_user*: After extracting users from the data frame, an eligible user list will be created, but excluding the current user, liked user, and disliked user. Then, the user with the highest compatibility score will be selected as a candidate matching user. Otherwise, a “False” message will the returned. 





  

 




 
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
 
 
 
