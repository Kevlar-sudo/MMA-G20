# MMA RSM8431Y - Matching U App Documentation - Group20 
### Contributors: Kevin Abdo, Yuze Li, Kevin Liu, Ruohan Wang, Emily Zhong
### Instructor: Prof. Arik Senderovich
### Course: RSM8431 Introduction to Computer Science with Python 

## Section 1: How to run code 
- If the code doesn't run properly, ensure the packages needed are installed using pip or pip3.
- When registering a user make sure the city is an actual city name in the world since we are querying a real-world database. i.e. "San Francisco", "Paris", and "Tokyo" are all valid options if not the score won't be calculated properly.
- Please ensure that interests are realistic thus the contribution scores are calculated properly. 
- Please be patient when browsing other users, you might need to wait a couple seconds for the system to recommend the best fit for you.



## Section 2: Description
**Matching U** apps aim to build a bridge for adults wanting to explore and start their love journeys. Matching U focuses on helping users find the best partner based on four main considerations: age, location, interests, and gender. When new users open the Matching U app, they can easily start by entering personal information and preferences such as age, gender, and interest to create their own profile. Then, they can log in to the Matching U app with the unique user ID and name. Next, there are several actions that the user can take, including editing and viewing their own profile, viewing other users' profiles, liking and disliking other users, deleting their own profile, and logging out. The matching U app will use the algorithm to recommend potential matches to the current users.

 
## Section 3: Usage / Technical
### Data Structure: UserProfile class 
The User Profile class is created to save each user's profile in the system, combined with the following attributes:
- user_id (int): A unique identifier for the user, auto-assigned by the database. 
- name (str): The name of the user.
- age (int): The user's age.
- gender (str): The user's gender, typically represented as "M" or "F".
- location (str): The city, where the user lives.
- interests (list of str): A list of the user's interests, like "yoga, swimming", "reading", "cooking", etc.
- liked_users (list of int): A list of user IDs that this user has liked.
- disliked_users (list of int): A list of user IDs that this user has disliked.
- matched_users (list of int): A list of user IDs that have been mutually matched with this user.


### Data Structure: UserManager Class
In the user manager, users’ information, including individual user ID, name, age, gender, location city, interest, and other information, including a list of liked users, a list of disliked users, and a list of matched users will be stored and updated and sync with the database. Current user’s information will be stored in the database through SQLite connection.

- *add_user*: A new user profile will be added to store the new user’s information in the database. 
- *user_exists*: To view an existing user profile, a given user id will be searched and will return the searching user’s a list of different information, otherwise, it will return a warning message.
- *update_user*: Users can edit their profile information. The user’s profile will be extracted from the database, and the updated information, such as name, age, gender, location, and interests, will replace the old data. The changes will then be saved back to the database.
- *delete_user*: A user profile will be removed. This function deletes the user’s profile from the database, and all references to the user in other users’ liked, disliked, and matched lists will be cleared as well.


### User Interaction
- *liked_user*: The liked user ID will be checked or added to the current users’ liked list depending on whether the list contains the liked user's ID. Moreover, if both users like each other, then each user will be added to the other’s liked list.
- *dislike_user*: If the disliked user's ID is not in the current user's disliked list, their ID will be added to the list and then updated to the database. 
- *_add_to_matches*: If the matched user's ID is not in the current user's matching list, their ID will be added to the list and then updated to the database. 
- *compare_users*: If both users' IDs are valid and match their names, two users' profiles will be created. Further, the compatibility scores will be calculated between two users.
- *recommend_user*: After extracting users from the dataframe, an eligible user list will be created excluding the current user, liked user, and disliked user. Then, the user with the highest compatibility score will be suggested as the best-matching user.


 
### Database Integration:

SQLite database is created by the function *create_table* to store user profiles and their actions. 

The system uses the SQLite database for persistent storage of user data and interactions. Python's built-in SQLite3library is used to perform all database operations, including creating, reading, updating, and deleting (CRUD) user profiles and their associated data. After the creation of the database, we perform **CRUD** operations:


- **C**:
*add_user*: create user profiles in the database.


- **R**:
*user_exists*: extract users' profiles and actions in the database.


- **U**: 
  - *like_user*: Updates the list of users that the current user has liked. If both users like each other, they are added to each other's match lists.
  - *_add_to_matches*: Updates the list of matched users when two users mutually like each other. The matched user ID is added to the current user's match list and saved in the database.
  - *dislike_user*: Updates the list of users that the current user has disliked. This ensures that the disliked user is not shown again in recommendations.
  - *update_user*: Updates the current user's profile information in the database. This includes modifying attributes such as the user's name, age, gender, location, and interests. The updated information is saved back to the SQLite database, ensuring that any changes the user makes to their profile are reflected in future interactions and queries.

- **D**:
*delete_user*: delete the current user and remove the current user’s follow-up effects.

 
## Section 4: Feature
 
### User Commands:
- *create_user*: Create a new user profile with information, including name, age, gender, location, and interests in the system which will be stored in the database.
- *view_profiles*: All user profile details can be viewed in the system.
- *update_profile*: Users could update or edit details, like name, age, location, or interests based on searching each user ID.
- *delete_profile*: User profile and previous actions (liked, disliked, and matched users) will be cleared.
- *like_user*: Updates the list of matched users when two users mutually like each other. The matched user ID is added to the current user's match list and saved in the database.
- *dislike_user*: Updates the list of users that the current user has disliked. This ensures that the disliked user is not shown again in recommendations.
- *view_matches*: The user could view the profiles of mutual-liked/matched users.
- Select preferred factor for the compatibility score


## Section 5: Method/Algorithm 
### Vectorization and Data Processing:
All potential match users will be stored in a dictionary. *compute_compatibility_scores*: The compatibility score between the current user and the candidate user will be calculated based on their profiles. The compatibility score will be evaluated based on age, interest, gender, and location of these 4 components.

- *Age similarity score*: The age score will be calculated based on the average age of users that the current user liked before. The closer the age of the other users is to the average age of the current user's previously liked users, the higher the age score will be.
- *Location similarity score*: The distance between the two users will be estimated. The longer distance will result in a lower location similarity score, and the upper threshold is 4000km. An algorithm “Nominatim” is used to convert the distances between  two users’ city locations into geographic coordinates.
- *Interest similarity score*: With a tree system, we use WordNet from NLTK to categorize all interests into 4 categories, including sports, art, lifestyle, and intellectual. Each category represents one subtree, and under each subtree, the algorithm recognizes a set of synonyms that have a common meaning and outputs a partial Interest similarity score between 0 and 1. For example, two words under the same  subtree (one category) will generate a higher score than two words under two distinct subtrees. More similar interests will get a higher interest similarity score.
- *Gender score*: The gender score will be calculated based on the average outcome of what the user liked before, thus the closer to the previously average gender/sexual orientation will lead to a higher gender score. 

Based on each user’s preference, they can rank each component, and the weighted coefficient based on the rank will be assigned. The total weight of 4 components will be partitioned  into 5 parts equally (20% each). The top-ranked components will account for 2 shares (40%), and the rest will have 1 share (20%). Finally, the compatibility score and suggested candidate user, who has the  highest compatibility score will be generated.


 
 
## Section 6: Tools
### Numpy:
- NumPy is used to efficiently calculate the compatibility scores between users by storing user information, such as location, age, gender, and interests, in matrices. By leveraging NumPy's vectorized operations, we calculate various compatibility factors, including location proximity, interest similarity, age difference, and gender preference. These operations allow for the simultaneous calculation of scores for all potential matches, optimizing performance by eliminating the need for looping through individual users. The final compatibility score is computed by combining these factors using matrix operations, making the process both faster and more efficient.

### Pandas DataFrame:
- The user data will be loaded in the Pandas Dataframe temporarily when doing some complicated operations like computing the compatibility scores between users.
- The DataFrame allows for vectorized operations and quick comparisons, with columns representing user attributes (age, gender, interests) and interaction data (liked, disliked, and matched users).

### Dictionaries and Lists:
- Dictionaries are applied to store user information and present results in most cases, for example, it allow us to fetch user profiles or find interest similarities. 
- Lists are applied to store liked, disliked, and matched user IDs in the user profiles. 


 
 
 
