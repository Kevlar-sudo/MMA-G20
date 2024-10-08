import sqlite3
from typing import Optional, List
from tkinter import *
from tkinter import messagebox

import nltk
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from random import randint
import pandas as pd
import numpy as np
from nltk.corpus import wordnet

# Download WordNet data if not already done
nltk.download('wordnet')

pd.options.mode.chained_assignment = None  # default='warn'

class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Matching U")
        self.canvas = Canvas(height=512, width=512)
        self.commandcanvas = Canvas(height = 164, width = 512)
        self.logo_png = PhotoImage(file="logo.png")
        self.label = Label(self.window, text="Welcome to Matching U", font=('Arial', 16))
        self.label.grid(row=0, column=0)

    #GUI menu page, user can select either log in as existing user or register as a new user.
    def menu_page(self):
        self.label.destroy()
        self.label = Label(self.window, text="Welcome to Matching U", font=('Arial', 16))
        self.label.grid(row=0, column=0)

        self.canvas.delete("all")
        self.canvas.create_image(256, 256, image=self.logo_png)
        self.canvas.grid(row=1, column=0)

        self.commandcanvas.delete("all")

        # Function to change the button's appearance on hover
        def on_enter(e, button):
            button['background'] = 'lightblue'  # Highlight color

        def on_leave(e, button):
            button['background'] = 'SystemButtonFace'  # Default color

        # New User button with hover effect
        self.new_button = Button(self.window, text="New User", font=('Arial', 16), command=self.register_page)
        self.new_button.bind("<Enter>", lambda e: on_enter(e, self.new_button))
        self.new_button.bind("<Leave>", lambda e: on_leave(e, self.new_button))
        self.commandcanvas.create_window(100, 30, window=self.new_button)

        # Existing User button with hover effect
        self.existing_button = Button(self.window, text="Existing User", font=('Arial', 16), command=self.log_in_page)
        self.existing_button.bind("<Enter>", lambda e: on_enter(e, self.existing_button))
        self.existing_button.bind("<Leave>", lambda e: on_leave(e, self.existing_button))
        self.commandcanvas.create_window(400, 30, window=self.existing_button)

        self.commandcanvas.grid(row=2, column=0)

    #Collect user info for new registration, calls check_profile function to check user inputs.
    def register_page(self):
        self.label.destroy()
        self.label = Label(self.window, text="Please Enter Your Info to Register", font=('Arial', 16))
        self.label.grid(row=0, column=0)

        self.canvas.delete("all")

        # Create user info entry boxes
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
        self.canvas.create_text(256, 300, text="Interests (Please separate your interests by comma)", font=('Arial', 16))

        # Remove buttons from menu page
        self.commandcanvas.delete("all")

        # Function to change the button's appearance on hover
        def on_enter(e, button):
            button['background'] = 'lightblue'  # Highlight color

        def on_leave(e, button):
            button['background'] = 'SystemButtonFace'  # Default color

        # Create user profile button with hover effect
        self.create_user = Button(self.window, text="Complete My Profile", font=('Arial', 16), command=self.check_profile)
        self.create_user.bind("<Enter>", lambda e: on_enter(e, self.create_user))
        self.create_user.bind("<Leave>", lambda e: on_leave(e, self.create_user))
        self.commandcanvas.create_window(400, 30, window=self.create_user)

        self.back_to_menu = Button(self.window, text="Back To Menu", font=('Arial', 16),
                                  command=self.menu_page)
        self.back_to_menu.bind("<Enter>", lambda e: on_enter(e, self.back_to_menu))
        self.back_to_menu.bind("<Leave>", lambda e: on_leave(e, self.back_to_menu))
        self.commandcanvas.create_window(130, 30, window=self.back_to_menu)

    #Collect user name and id as log in credentials, calls check_log_in function to verify.
    def log_in_page(self):
        self.label.destroy()
        self.label = Label(self.window, text="Log In to Your Account", font=('Arial', 16))
        self.label.grid(row=0, column=0)

        # Create user log in entry boxes
        self.canvas.delete("all")
        self.name_entry = Entry(self.window, font=('Arial', 16), width=24)
        self.id_entry = Entry(self.window, font=('Arial', 16), width=8)

        self.canvas.create_window(300, 200, window=self.name_entry)
        self.canvas.create_window(204, 150, window=self.id_entry)

        self.canvas.create_text(100, 200, text="Name", font=('Arial', 16))
        self.canvas.create_text(100, 150, text="User ID", font=('Arial', 16))

        # Remove buttons from the menu page
        self.commandcanvas.delete("all")

        # Function to change the button's appearance on hover
        def on_enter(e, button):
            button['background'] = 'lightblue'  # Highlight color

        def on_leave(e, button):
            button['background'] = 'SystemButtonFace'  # Default color

        # Log in as existing user, check if the user exists
        self.user_log_in = Button(self.window, text="Log In", font=('Arial', 16), command=self.check_log_in)
        self.user_log_in.bind("<Enter>", lambda e: on_enter(e, self.user_log_in))
        self.user_log_in.bind("<Leave>", lambda e: on_leave(e, self.user_log_in))
        self.commandcanvas.create_window(400, 30, window=self.user_log_in)

        self.back_to_menu = Button(self.window, text="Back To Menu", font=('Arial', 16),
                                  command=self.menu_page)
        self.back_to_menu.bind("<Enter>", lambda e: on_enter(e, self.back_to_menu))
        self.back_to_menu.bind("<Leave>", lambda e: on_leave(e, self.back_to_menu))
        self.commandcanvas.create_window(130, 30, window=self.back_to_menu)

    #User profile page that displays all the user options after log in.
    def profile_page(self, current_user):
        self.label.destroy()
        self.label = Label(self.window, text=f"{current_user.name}, Welcome Back!", font=('Arial', 16))
        self.label.grid(row=0, column=0)

        # Clear the canvas to show the user profile details
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

        # Function to change the button's appearance on hover
        def on_enter(e, button):
            button['background'] = 'lightblue'  # Highlight color

        def on_leave(e, button):
            button['background'] = 'SystemButtonFace'  # Default color

        # Show user options with hover effects
        self.user_log_out = Button(self.window, text="Log Out", font=('Arial', 16), command=self.menu_page)
        self.user_log_out.bind("<Enter>", lambda e: on_enter(e, self.user_log_out))
        self.user_log_out.bind("<Leave>", lambda e: on_leave(e, self.user_log_out))
        self.commandcanvas.create_window(90, 30, window=self.user_log_out)

        self.user_browse = Button(self.window, text="        Start Browsing        ", font=('Arial', 16), fg='green', command=lambda: self.factor_page(current_user))
        self.user_browse.bind("<Enter>", lambda e: on_enter(e, self.user_browse))
        self.user_browse.bind("<Leave>", lambda e: on_leave(e, self.user_browse))
        self.commandcanvas.create_window(230, 140, window=self.user_browse)


        self.user_update = Button(self.window, text="Update Profile", font=('Arial', 16), command=lambda: self.update_page(current_user))
        self.user_update.bind("<Enter>", lambda e: on_enter(e, self.user_update))
        self.user_update.bind("<Leave>", lambda e: on_leave(e, self.user_update))
        self.commandcanvas.create_window(400, 30, window=self.user_update)

        self.user_liked = Button(self.window, text="Liked User", font=('Arial', 16), command=lambda: self.liked_page(current_user))
        self.user_liked.bind("<Enter>", lambda e: on_enter(e, self.user_liked))
        self.user_liked.bind("<Leave>", lambda e: on_leave(e, self.user_liked))
        self.commandcanvas.create_window(90, 80, window=self.user_liked)

        self.user_disliked = Button(self.window, text="Disliked User", font=('Arial', 16), command=lambda: self.disliked_page(current_user))
        self.user_disliked.bind("<Enter>", lambda e: on_enter(e, self.user_disliked))
        self.user_disliked.bind("<Leave>", lambda e: on_leave(e, self.user_disliked))
        self.commandcanvas.create_window(230, 80, window=self.user_disliked)

        self.user_matched = Button(self.window, text="Matched User", font=('Arial', 16), command=lambda: self.matched_page(current_user))
        self.user_matched.bind("<Enter>", lambda e: on_enter(e, self.user_matched))
        self.user_matched.bind("<Leave>", lambda e: on_leave(e, self.user_matched))
        self.commandcanvas.create_window(400, 80, window=self.user_matched)

        self.user_delete = Button(self.window, text="Delete My Profile", font=('Arial', 16), command=lambda: self.delete_current_user(current_user))
        self.user_delete.bind("<Enter>", lambda e: on_enter(e, self.user_delete))
        self.user_delete.bind("<Leave>", lambda e: on_leave(e, self.user_delete))
        self.commandcanvas.create_window(230, 30, window=self.user_delete)

    #Ask for user preference of the scoring factors before starts browsing
    def factor_page(self, current_user):
        self.label.destroy()
        self.label = Label(self.window, text="What is the most important factor in selecting your partner",
                           font=('Arial', 16))
        self.label.grid(row=0, column=0)
        self.canvas.delete("all")

        pref_entry = StringVar(self.window)
        self.preference_entry = OptionMenu(self.window, pref_entry, "age_diff_score", "location_score", "gender_score",
                                           "interests_score")
        self.canvas.create_window(250, 200, window=self.preference_entry)

        self.canvas.create_text(100, 200, text="Deciding Factor", font=('Arial', 16))

        # Remove buttons from menu page
        self.commandcanvas.delete("all")

        # Function to change the button's appearance on hover
        def on_enter(e, button):
            button['background'] = 'lightblue'  # Highlight color

        def on_leave(e, button):
            button['background'] = 'SystemButtonFace'  # Default color

        # Function to be called when the user clicks "Start Browsing"
        def start_browsing():
            preference = pref_entry.get()  # Get the user's selection when button is clicked
            self.browse_page(current_user, preference)

        # Create user profile button with hover effect
        self.create_user = Button(self.window, text="Start Browsing", font=('Arial', 16), fg='green',
                                  command=start_browsing)
        self.create_user.bind("<Enter>", lambda e: on_enter(e, self.create_user))
        self.create_user.bind("<Leave>", lambda e: on_leave(e, self.create_user))
        self.commandcanvas.create_window(400, 30, window=self.create_user)

        self.back_to_menu = Button(self.window, text="Back To Menu", font=('Arial', 16), command=self.menu_page)
        self.back_to_menu.bind("<Enter>", lambda e: on_enter(e, self.back_to_menu))
        self.back_to_menu.bind("<Leave>", lambda e: on_leave(e, self.back_to_menu))
        self.commandcanvas.create_window(130, 30, window=self.back_to_menu)

    #Shows the profile info of the recommended user with the highest compatibility score
    def browse_page(self, current_user, preference):
        result = manager.recommend_user(current_user, preference)
        self.label.destroy()
        self.canvas.delete("all")
        self.commandcanvas.delete("all")
        #Check if the current user have viewed all other users
        if result[0] == False:
            self.label = Label(self.window, text=f"You viewed all the existing users", font=('Arial', 16))
            self.label.grid(row=0, column=0)
            self.canvas.create_text(200, 300, text="Please come back later!", font=('Arial', 16))

        else:
            other_user = result[0]
            compatibility_score = result[1]
            self.label = Label(self.window, text=f"You are viewing {other_user.name}'s profile", font=('Arial', 16))
            self.label.grid(row=0, column=0)

            # Clear the canvas to show the user profile details
            self.canvas.create_text(100, 150, text="Name", font=('Arial', 16))
            self.canvas.create_text(100, 200, text="Age", font=('Arial', 16))
            self.canvas.create_text(100, 250, text="Gender", font=('Arial', 16))
            self.canvas.create_text(100, 300, text="Location", font=('Arial', 16))
            self.canvas.create_text(100, 350, text="Interests", font=('Arial', 16))
            self.canvas.create_text(100, 400, text="Compatibility Score", font=('Arial', 16))

            self.canvas.create_text(300, 150, text=other_user.name, font=('Arial', 16))
            self.canvas.create_text(300, 200, text=other_user.age, font=('Arial', 16))
            self.canvas.create_text(300, 250, text=other_user.gender, font=('Arial', 16))
            self.canvas.create_text(300, 300, text=other_user.location, font=('Arial', 16))
            self.canvas.create_text(300, 350, text=','.join(current_user.interests), font=('Arial', 16))
            self.canvas.create_text(300, 400, text=round(compatibility_score, 3), font=('Arial', 16))


            # Show user options with hover effects
            self.like_button = Button(self.window, text="LIKE", font=('Arial', 16),
                                      command=lambda: self.like_user(current_user, other_user, preference))
            self.like_button.bind("<Enter>", lambda e: on_enter(e, self.like_button))
            self.like_button.bind("<Leave>", lambda e: on_leave(e, self.like_button))
            self.commandcanvas.create_window(90, 30, window=self.like_button)

            self.dislike_button = Button(self.window, text="DISLIKE", font=('Arial', 16),
                                         command=lambda: self.dislike_user(current_user, other_user, preference))
            self.dislike_button.bind("<Enter>", lambda e: on_enter(e, self.dislike_button))
            self.dislike_button.bind("<Leave>", lambda e: on_leave(e, self.dislike_button))
            self.commandcanvas.create_window(230, 30, window=self.dislike_button)



        # Function to change the button's appearance on hover
        def on_enter(e, button):
            button['background'] = 'lightblue'  # Highlight color

        def on_leave(e, button):
            button['background'] = 'SystemButtonFace'  # Default color

        #Show the "Back to My Profile" button
        self.back_to_profile = Button(self.window, text="Back to My Profile", font=('Arial', 16), command=lambda: self.profile_page(current_user))
        self.back_to_profile.bind("<Enter>", lambda e: on_enter(e, self.back_to_profile))
        self.back_to_profile.bind("<Leave>", lambda e: on_leave(e, self.back_to_profile))
        self.commandcanvas.create_window(400, 30, window=self.back_to_profile)

    #Allow user to view the liked users, also allow user to dislike instead
    def liked_page(self, current_user):
        #fetch all the info of the liked users, put in a dict, key are names
        user_dict = manager.fetch_users(current_user.liked_users)

        self.label.destroy()
        self.label = Label(self.window, text=f"You have liked {len(current_user.liked_users)} users", font=('Arial', 16))
        self.label.grid(row=0, column=0)

        # clear the canvas to show the user profile details
        self.canvas.delete("all")
        # Remove buttons from previous page
        self.commandcanvas.delete("all")
        selected_user = StringVar()

        if user_dict is not False:
            selected_user = StringVar(self.window)
            keys = list(user_dict.keys())
            self.liked_entry = OptionMenu(self.window, selected_user, *keys)
            selected_user.set(keys[0])
            self.liked_entry = OptionMenu(self.window, selected_user, *list(user_dict.keys()))
            self.commandcanvas.create_window(90, 30, window=self.liked_entry)

            self.display_button = Button(self.window, text="Display Selected User Profile", font=('Arial', 16),
                                  command=lambda: self.display_profile(user_dict[selected_user.get()]))
            self.commandcanvas.create_window(300, 30, window=self.display_button)
            self.dislike_instead_button = Button(self.window, text="Dislike Instead", font=('Arial', 16),
                                       command=lambda: self.dislike_instead(current_user, manager.fetch_one_user(user_dict[selected_user.get()][0])))
            self.commandcanvas.create_window(90, 80, window=self.dislike_instead_button)


        self.back_to_profile = Button(self.window, text="Back to My Profile", font=('Arial', 16),
                                      command=lambda: self.profile_page(current_user))
        self.commandcanvas.create_window(300, 80, window=self.back_to_profile)

    # Allow user to view the disliked users, also allow user to like instead
    def disliked_page(self, current_user):
        #fetch all the info of the liked users, put in a dict, key are names
        user_dict = manager.fetch_users(current_user.disliked_users)

        self.label.destroy()
        self.label = Label(self.window, text=f"You have disliked {len(current_user.disliked_users)} users", font=('Arial', 16))
        self.label.grid(row=0, column=0)

        # clear the canvas to show the user profile details
        self.canvas.delete("all")
        # Remove buttons from previous page
        self.commandcanvas.delete("all")

        if user_dict is not False:
            selected_user = StringVar(self.window)
            keys = list(user_dict.keys())
            self.disliked_entry = OptionMenu(self.window, selected_user, *keys)
            selected_user.set(keys[0])
            self.commandcanvas.create_window(90, 30, window=self.disliked_entry)

            self.display_button = Button(self.window, text="Display Selected User Profile", font=('Arial', 16),
                                  command=lambda: self.display_profile(user_dict[selected_user.get()]))
            self.commandcanvas.create_window(300, 30, window=self.display_button)

            self.like_instead_button = Button(self.window, text="Like Instead", font=('Arial', 16),
                                  command=lambda: self.like_instead(current_user, manager.fetch_one_user(user_dict[selected_user.get()][0])))
            self.commandcanvas.create_window(90, 80, window=self.like_instead_button)

        self.back_to_profile = Button(self.window, text="Back to My Profile", font=('Arial', 16),
                                      command=lambda: self.profile_page(current_user))
        self.commandcanvas.create_window(300, 80, window=self.back_to_profile)

    # Allow user to view the matched users
    def matched_page(self, current_user):
        #fetch all the info of the liked users, put in a dict, key are names
        user_dict = manager.fetch_users(current_user.matched_users)

        self.label.destroy()
        self.label = Label(self.window, text=f"You have matched {len(current_user.matched_users)} users", font=('Arial', 16))
        self.label.grid(row=0, column=0)

        # clear the canvas to show the user profile details
        self.canvas.delete("all")
        # Remove buttons from previous page
        self.commandcanvas.delete("all")

        if user_dict is not False:
            selected_user = StringVar()
            self.matched_entry = OptionMenu(self.window, selected_user, *list(user_dict.keys()))
            self.commandcanvas.create_window(90, 30, window=self.matched_entry)

            self.display_button = Button(self.window, text="Display Selected User Profile", font=('Arial', 16),
                                  command=lambda: self.display_profile(user_dict[selected_user.get()]))
            self.commandcanvas.create_window(300, 30, window=self.display_button)

        self.back_to_profile = Button(self.window, text="Back to My Profile", font=('Arial', 16),
                                      command=lambda: self.profile_page(current_user))
        self.commandcanvas.create_window(300, 80, window=self.back_to_profile)

    # Allow user to update profile, calls check_update to verify input.
    def update_page(self, current_user):
        self.label.destroy()
        self.label = Label(self.window, text="Please update your profile", font=('Arial', 16))
        self.label.grid(row=0, column=0)

        # Clear the canvas to show the user profile details
        self.canvas.delete("all")

        self.canvas.create_text(100, 100, text="User ID", font=('Arial', 16))
        self.canvas.create_text(100, 150, text="Name", font=('Arial', 16))
        self.canvas.create_text(100, 200, text="Age", font=('Arial', 16))
        self.canvas.create_text(100, 250, text="Gender", font=('Arial', 16))
        self.canvas.create_text(100, 300, text="Location", font=('Arial', 16))
        self.canvas.create_text(256, 350, text="Interests", font=('Arial', 16))

        self.name_entry = Entry(self.window, font=('Arial', 16), width=8)
        self.age_entry = Entry(self.window, font=('Arial', 16), width=8)
        self.gender = StringVar(self.window)
        self.gender_entry = OptionMenu(self.window, self.gender, "M", "F")
        self.location_entry = Entry(self.window, font=('Arial', 16), width=24)
        self.interests_entry = Entry(self.window, font=('Arial', 16), width=36)

        #Set user's current info as default in the text boxes
        self.name_entry.insert(0,current_user.name)
        self.age_entry.insert(0,current_user.age)
        self.gender.set(current_user.gender)
        self.location_entry.insert(0, current_user.location)
        self.interests_entry.insert(0, ','.join(current_user.interests))

        self.canvas.create_text(200, 100, text=current_user.user_id, font=('Arial', 16))
        self.canvas.create_window(204, 150, window=self.name_entry)
        self.canvas.create_window(204, 200, window=self.age_entry)
        self.canvas.create_window(172, 250, window=self.gender_entry)
        self.canvas.create_window(300, 300, window=self.location_entry)
        self.canvas.create_window(256, 400, window=self.interests_entry)

        # Remove buttons from the menu page
        self.commandcanvas.delete("all")

        # Function to change the button's appearance on hover
        def on_enter(e, button):
            button['background'] = 'lightblue'  # Highlight color

        def on_leave(e, button):
            button['background'] = 'SystemButtonFace'  # Default color

        # Log in as existing user, check if the user exists
        self.user_update = Button(self.window, text="Update", font=('Arial', 16), command=lambda: self.check_update(current_user))
        self.user_update.bind("<Enter>", lambda e: on_enter(e, self.user_update))
        self.user_update.bind("<Leave>", lambda e: on_leave(e, self.user_update))
        self.commandcanvas.create_window(400, 30, window=self.user_update)

        self.back_to_profile = Button(self.window, text="Back To Menu", font=('Arial', 16),
                                   command= lambda: self.profile_page(current_user))
        self.back_to_profile.bind("<Enter>", lambda e: on_enter(e, self.back_to_profile))
        self.back_to_profile.bind("<Leave>", lambda e: on_leave(e, self.back_to_profile))
        self.commandcanvas.create_window(130, 30, window=self.back_to_profile)

    #Delete current user's profile permanently
    def delete_current_user(self, current_user):
            confirmation = messagebox.askyesno("Delete Profile", "Are you sure you want to delete your profile?")
            if confirmation:
                manager.delete_user(current_user.user_id)
                messagebox.showinfo("Profile Deleted", "Your profile has been deleted successfully.")
                # Redirect to the login page or exit the application
                self.log_in_page()
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
        elif int(user_age) < 18:
            messagebox.showinfo(title="Oops", message="Please be over 18 to user this app")
        else:
            manager.add_user(None, user_name, int(user_age), user_gender, user_location, user_interests)

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

    def display_profile(self, selected_user):
        self.canvas.delete("all")
        self.canvas.create_text(100, 150, text="Name", font=('Arial', 16))
        self.canvas.create_text(100, 200, text="Age", font=('Arial', 16))
        self.canvas.create_text(100, 250, text="Gender", font=('Arial', 16))
        self.canvas.create_text(100, 300, text="Location", font=('Arial', 16))
        self.canvas.create_text(100, 350, text="Interests", font=('Arial', 16))

        self.canvas.create_text(300, 150, text=selected_user[1], font=('Arial', 16))
        self.canvas.create_text(300, 200, text=selected_user[2], font=('Arial', 16))
        self.canvas.create_text(300, 250, text=selected_user[3], font=('Arial', 16))
        self.canvas.create_text(300, 300, text=selected_user[4], font=('Arial', 16))
        self.canvas.create_text(300, 350, text=selected_user[5], font=('Arial', 16))

    def check_update(self, current_user):
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
            manager.update_user(current_user, user_name, int(user_age), user_gender, user_location, user_interests)
            messagebox.showinfo(title="Done!", message="Your profile has been successfully updated")
            user_result = manager.user_exists(current_user.user_id, user_name)
            self.profile_page(user_result)

    def like_user(self, current_user, other_user, preference):
        #The returned result is a list of booleans, first indicate if this person is already liked, second indicate if this person is matched
        result = manager.like_user(current_user.user_id, other_user.user_id)

        if result[0] == True:
            current_user.liked_users.append(other_user.user_id)
            messagebox.showinfo(title="Thank you!", message="You LIKE has been saved")
            if result[1] == True:
                current_user.matched_users.append(other_user.user_id)
        else:
            messagebox.showinfo(title="oops!", message="You already liked this person")
        self.browse_page(current_user, preference)

    def dislike_user(self, current_user, other_user, preference):
        result = manager.dislike_user(current_user.user_id, other_user.user_id)
        if result == True:
            current_user.disliked_users.append(other_user.user_id)
            messagebox.showinfo(title="Thank you!", message="You DISLIKE has been saved")
        else:
            messagebox.showinfo(title="oops!", message="You already disliked this person")
        self.browse_page(current_user, preference)

    def like_instead(self, current_user, other_user):
        #remove the disliked user for user's dislike list.
        current_user.disliked_users.remove(other_user.user_id)
        current_user.update_db()
        # The returned result is a list of booleans, first indicate if this person is already liked, second indicate if this person is matched
        result = manager.like_user(current_user.user_id, other_user.user_id)

        current_user.liked_users.append(other_user.user_id)
        messagebox.showinfo(title="Thank you!", message="You LIKE has been saved")
        #check if matched
        if result[1] == True:
            current_user.matched_users.append(other_user.user_id)

        self.profile_page(current_user)

    def dislike_instead(self, current_user, other_user):
        #remove the liked user for user's like list.
        current_user.liked_users.remove(other_user.user_id)
        if other_user.user_id in current_user.matched_users:
            current_user.matched_users.remove(other_user.user_id)
            other_user.matched_users.remove(current_user.user_id)
            other_user.update_db()
        current_user.update_db()
        manager.dislike_user(current_user.user_id, other_user.user_id)
        current_user.disliked_users.append(other_user.user_id)
        messagebox.showinfo(title="Thank you!", message="You DISLIKE has been saved")
        self.profile_page(current_user)


class UserProfile:
    def __init__(self, user_id: int, name: str, age: int, gender: str, location: str, interests: str,
                 liked_users: Optional[str] = '', disliked_users: Optional[str] = '',
                 matched_users: Optional[str] = ''):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.gender = gender
        self.location = location
        self.interests = interests.split(',')
        self.liked_users = list(map(int, liked_users.split(','))) if liked_users != '' else []
        self.disliked_users = list(map(int, disliked_users.split(','))) if disliked_users != '' else []
        self.matched_users = list(map(int, matched_users.split(','))) if matched_users != '' else []
        self.geolocator = Nominatim(user_agent="dating_app")
        self.categorize_interests()  # Categorize interests when the object is initialized

    def get_hobby_category(self,hobby):
        synsets = wordnet.synsets(hobby)
        if synsets:
            hypernym = synsets[0].hypernyms()[0].lemmas()[0].name()
            if 'sport' in hypernym:
                return 'sports'
            elif 'art' in hypernym:
                return 'art'
            elif 'activity' in hypernym or 'lifestyle' in hypernym:
                return 'lifestyle'
            elif 'intellect' in hypernym or 'knowledge' in hypernym:
                return 'intellectual'
        return None
    
    def categorize_interests(self):
        self.categorized_interests = {hobby: self.get_hobby_category(hobby) for hobby in self.interests}
    
    def calculate_interest_compatibility(self, other_user: 'UserProfile') -> float:
        exact_matches = set(self.interests) & set(other_user.interests)
        exact_score = len(exact_matches)
        
        # Calculate partial category matches
        user_categories = set(self.categorized_interests.values())
        match_categories = set(other_user.categorized_interests.values())
        
        category_matches = user_categories & match_categories
        category_score = len(category_matches) - exact_score  # Subtract exact matches to avoid double counting
        
        total_score = exact_score + (category_score * 0.5)  # Partial score of 0.5 for category matches
        
        max_possible_score = max(len(self.interests), len(other_user.interests))
        
        return total_score / max_possible_score if max_possible_score > 0 else 0

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

    def calculate_location_compatibility(self, other_user: 'UserProfile') -> Optional[float]:
        distance = self.calculate_distance(other_user)
        if distance is not None:
            max_distance = 4000  # Define a max distance to normalize the score
            compatibility_score = max(0, (max_distance - distance) / max_distance) 
            return round(compatibility_score, 2)
        else:
            return None

    def save_to_db(self, conn: sqlite3.Connection) -> None:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (name, age, gender, location, interests, liked_users, disliked_users, matches)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (self.name, self.age, self.gender, self.location, ','.join(self.interests),'','',''))
        self.user_id = cursor.lastrowid
        conn.commit()

    def update_db(self):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        query = """
                    UPDATE users 
                    SET name = ?, age = ?, gender = ?, location = ?, interests = ?, liked_users = ?, disliked_users = ?, matches = ? 
                    WHERE user_id = ?
                """
        parameters = (
            self.name,
            self.age,
            self.gender,
            self.location,
            ','.join(map(str, self.interests)) if self.interests else '',
            ','.join(map(str, self.liked_users)) if self.liked_users else '',
            ','.join(map(str, self.disliked_users)) if self.disliked_users else '',
            ','.join(map(str, self.matched_users)) if self.matched_users else '',
            self.user_id
        )
        cursor.execute(query, parameters)
        conn.commit()
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


    #POTENTIALLY REMOVE THIS TBD
        def delete_user(self, current_user):
            #fetch all the info of the liked users, put in a dict, key are names
            user_dict = manager.fetch_users(current_user.matched_users)

            self.label.destroy()
            self.label = Label(self.window, text=f"You have matched {len(current_user.matched_users)} users", font=('Arial', 16))
            self.label.grid(row=0, column=0)

            # clear the canvas to show the user profile details
            self.canvas.delete("all")
            # Remove buttons from previous page
            self.commandcanvas.delete("all")

            if user_dict is not False:
                selected_user = StringVar()
                self.matched_entry = OptionMenu(self.window, selected_user, *list(user_dict.keys()))
                self.commandcanvas.create_window(90, 30, window=self.matched_entry)

                self.display_button = Button(self.window, text="Display Selected User Profile", font=('Arial', 16),
                                    command=lambda: self.display_profile(user_dict[selected_user.get()]))
                self.commandcanvas.create_window(300, 30, window=self.display_button)

            self.back_to_profile = Button(self.window, text="Back to My Profile", font=('Arial', 16),
                                        command=lambda: self.profile_page(current_user))
            self.commandcanvas.create_window(300, 80, window=self.back_to_profile)

    def add_user(self, user_id: Optional[int], name: str, age: int, gender: str, location: str, interests: str):
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
                user1 = UserProfile(row1[0], row1[1], row1[2], row1[3], row1[4], row1[5],row1[6],row1[7],row1[8])
                return user1

    def like_user(self, current_user_id: int, liked_user_id: int):
        cursor = self.conn.cursor()

        cursor.execute("SELECT liked_users FROM users WHERE user_id = ?", (current_user_id,))
        liked_users = cursor.fetchone()[0]
        liked_users_list = liked_users.split(',') if liked_users else []
        if str(liked_user_id) not in liked_users_list:
            liked_users_list.append(str(liked_user_id))
            cursor.execute("""
                UPDATE users 
                SET liked_users = ?
                WHERE user_id = ?
            """, (','.join(liked_users_list), current_user_id))
            self.conn.commit()
            cursor.execute("SELECT liked_users FROM users WHERE user_id = ?", (liked_user_id,))
            other_liked_users = cursor.fetchone()[0]
            other_liked_users_list = other_liked_users.split(',') if other_liked_users else []
            if str(current_user_id) in other_liked_users_list:
                self._add_to_matches(current_user_id, liked_user_id)
                self._add_to_matches(liked_user_id, current_user_id)
                messagebox.showinfo(title="It's a Match!", message="You have a new match!")
                return [True, True]
            else:
                return [True, False]
        else:
            return [False, False]

    def _add_to_matches(self, user_id: int, matched_user_id: int):
        cursor = self.conn.cursor()
        cursor.execute("SELECT matches FROM users WHERE user_id = ?", (user_id,))
        matched_users = cursor.fetchone()[0]
        matched_users_list = matched_users.split(',') if matched_users else []

        if str(matched_user_id) not in matched_users_list:
            matched_users_list.append(str(matched_user_id))
            cursor.execute("""
                UPDATE users
                SET matches = ?
                WHERE user_id = ?
            """, (','.join(matched_users_list), user_id))
            self.conn.commit()

    def dislike_user(self, current_user_id: int, disliked_user_id: int):
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
            return True
        else:
            return False

    def update_user(self, current_user, name, age, gender, location, interests):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (current_user.user_id,))
        cursor.execute("""
                        UPDATE users
                        SET name = ?, age = ?, gender = ?, location = ?, interests = ?, liked_users = ?, disliked_users = ?, matches = ?
                        WHERE user_id = ?
                    """, (name, age, gender, location, interests,
                          ','.join(map(str, current_user.liked_users)) if len(current_user.liked_users) != 0 else '',
                          ','.join(map(str, current_user.disliked_users))if len(current_user.disliked_users) != 0 else '',
                          ','.join(map(str, current_user.matched_users))if len(current_user.matched_users) != 0 else '',
                          current_user.user_id))
        self.conn.commit()

    #Delete user method that deletes all instances of the user in the database in liked_users, disliked_users and matches
    def delete_user(self, user_id: int) -> None:
        cursor = self.conn.cursor()

        # Delete the user from the 'users' table
        cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))

        # Remove the user_id from the 'liked_users' column in all users
        cursor.execute("UPDATE users SET liked_users = REPLACE(liked_users, ?, '') WHERE liked_users LIKE ?", (f',{user_id}', f'%{user_id}%'))
        cursor.execute("UPDATE users SET liked_users = REPLACE(liked_users, ?, '') WHERE liked_users LIKE ?", (f'{user_id},', f'%{user_id}%'))
        cursor.execute("UPDATE users SET liked_users = REPLACE(liked_users, ?, '') WHERE liked_users = ?", (f'{user_id}', f'{user_id}'))
        # Set the 'liked_users' column

    # Remove the user_id from the 'disliked_users' column in all users
        cursor.execute("UPDATE users SET disliked_users = REPLACE(disliked_users, ?, '') WHERE disliked_users LIKE ?", (f',{user_id}', f'%{user_id}%'))
        cursor.execute("UPDATE users SET disliked_users = REPLACE(disliked_users, ?, '') WHERE disliked_users LIKE ?", (f'{user_id},', f'%{user_id}%'))
        cursor.execute("UPDATE users SET disliked_users = REPLACE(disliked_users, ?, '') WHERE disliked_users = ?", (f'{user_id}', f'{user_id}'))


        # Remove the user_id from the 'matches' column in all users
        cursor.execute("UPDATE users SET matches = REPLACE(matches, ?, '') WHERE matches LIKE ?", (f',{user_id}', f'%{user_id}%'))
        cursor.execute("UPDATE users SET matches = REPLACE(matches, ?, '') WHERE matches LIKE ?", (f'{user_id},', f'%{user_id}%'))
        cursor.execute("UPDATE users SET matches = REPLACE(matches, ?, '') WHERE matches = ?", (f'{user_id}', f'{user_id}'))


        self.conn.commit()
        print(f"User {user_id} and all associated references have been deleted successfully!")

    #This function gets the current UserProfile from the browse_page function in the GUI class, and returned the eligible user with the highest compatibility score, if no other users are eligible (current user viewed all the existing profiles), this function returns False.
    def recommend_user(self, current_user, factor_preference):
        cursor = self.conn.cursor()
        df = self.fetch_all_users()
        eligible_users = []
        #exclude current user himself/herself, users in current user's liked and disliked list, and get a list of eligible users
        for ind in df.index:
            if df["user_id"][ind] in current_user.liked_users or df["user_id"][ind] in current_user.disliked_users or df["user_id"][ind] == current_user.user_id:
                continue
            else:
                eligible_users.append(df["user_id"][ind])
        #check if there are eligible users
        if len(eligible_users) == 0:
            return [False, False]
        else:
            if len(current_user.liked_users) == 0:
                age_preference = current_user.age
                gender_preference = 0.5
            else:
                liked_df = df[df["user_id"].isin(current_user.liked_users)]
                like_count = len(liked_df.index)
                age_preference = (current_user.age + like_count * liked_df.loc[:, 'age'].mean())/(like_count + 1)
                gender_dict = liked_df['gender'].value_counts().to_dict()
                if 'M' in liked_df.keys():
                    gender_preference = (gender_dict['M'] + 0.5) / (like_count + 1)
                else:
                    gender_preference = 0.5/(like_count +1)

        recommend = compute_compatibility_score(current_user, df[df["user_id"].isin(eligible_users)], age_preference, gender_preference, factor_preference)

        return [self.fetch_one_user(int(recommend[0])), recommend[1]]

    #fetch one user from the database, return the requested UserProfile
    def fetch_one_user(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        row = cursor.fetchone()
        user = UserProfile(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        return user

    #fetch a list of users and save their info in a dict, used for display liked, disliked and matched users
    def fetch_users(self, user_list):
        if user_list == []:
            return False
        else:
            user_dict = {}
            cursor = self.conn.cursor()
            for id in user_list:
                cursor.execute("SELECT * FROM users WHERE user_id = ?", (id,))
                row = cursor.fetchone()
                #temp_user = UserProfile(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                user_dict.update({str(row[0]) + ': ' + row[1]: [row[0], row[1], row[2], row[3], row[4], row[5]]})
            return user_dict

    #fetch all users for database and save all the info in a pandas datafram
    def fetch_all_users(self):
        df = pd.read_sql_query("SELECT * FROM users", self.conn)
        # Convert each comma-separated string in the 'interests' column to a list of interests
        df['interests'] = df['interests'].apply(
            lambda x: x.split(',') if x else [])
            # lambda x:        -> Defines an anonymous function with 'x' as the input (each element in the 'interests' column)
            # x.split(',')     -> Splits the string 'x' by commas into a list (e.g., "hiking,reading" becomes ['hiking', 'reading'])
            # if x             -> Checks if 'x' is not empty or None. If 'x' has content, split it by commas.
            # else []          -> If 'x' is empty or None, return an empty list instead of trying to split 'x'
        df['liked_users'] = df['liked_users'].apply(
            lambda x: map(int, x.split(',')) if x else [])
        df['disliked_users'] = df['disliked_users'].apply(
            lambda x: map(int, x.split(',')) if x else [])
        df['matches'] = df['matches'].apply(
            lambda x: map(int, x.split(',')) if x else [])


        return df


# Compute Compatibility Scores (compute the score of the current user and the other eligible user), return the id of the user with highest score
def compute_compatibility_score(logged_in_user: UserProfile, potential_matches, age_preference, gender_preference, factor_preference):
    # Fetch other users from the DataFrame by their user IDs
    other_users = potential_matches['user_id'].apply(manager.fetch_one_user)

    # Use list comprehensions or pandas `apply` to calculate location and interest compatibility
    location_scores = np.array([logged_in_user.calculate_location_compatibility(other_user) for other_user in other_users])
    interest_scores = np.array([logged_in_user.calculate_interest_compatibility(other_user) for other_user in other_users])

    # Calculate age difference scores using NumPy vectorized operations
    age_diff_scores = 1 / (1 + np.abs(potential_matches['age'].values - age_preference))

    # Calculate gender scores using vectorized operations based on gender preference
    gender_scores = np.where(potential_matches['gender'].values == 'M', 
                             1 - (1 - gender_preference), 
                             1 - gender_preference)

    # Add the calculated scores back to the DataFrame
    potential_matches['location_score'] = location_scores
    potential_matches['interests_score'] = interest_scores
    potential_matches['age_diff_score'] = age_diff_scores
    potential_matches['gender_score'] = gender_scores

    # Combine the individual scores into a final compatibility score
    potential_matches['compatibility_score'] = (
        0.2 * potential_matches['location_score'] +
        0.2 * potential_matches['age_diff_score'] +
        0.2 * potential_matches['gender_score'] +
        0.2 * potential_matches['interests_score']+
        0.2 * potential_matches[factor_preference]
    )

    # Sort by the compatibility score based on the `factor_preference`
    sorted_matches = potential_matches.sort_values(by=factor_preference, ascending=False)

    # Return the user with the highest compatibility score
    return [sorted_matches['user_id'].iloc[0], sorted_matches['compatibility_score'].iloc[0]]

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

    #Test Code
    #use a user in database to test the recommend function
    #manager.like_user(5, 6)
    #user = manager.user_exists(int(8), "Hannibal")
    #other_user = manager.recommend_user(user)
    #print(other_user[0].name)

#Load All Users into a Pandas DataFrame
