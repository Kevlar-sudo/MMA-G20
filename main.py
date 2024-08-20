import sqlite3
from typing import Optional, List
from tkinter import *
from tkinter import messagebox
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from random import randint
import pandas as pd
import numpy as np



#Button commands should call the function UserManager class and functions in the UserManager class should call UI functions to display info and inputs/command from user.

class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Matching U")
        self.canvas = Canvas(height=512, width=512)
        self.commandcanvas = Canvas(height = 164, width = 512)
        self.logo_png = PhotoImage(file="logo.png")
        self.label = Label(self.window, text="Welcome to Matching U", font=('Arial', 16))
        self.label.grid(row=0, column=0)

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

        self.user_browse = Button(self.window, text="        Start Browsing        ", font=('Arial', 16), fg='green', command=lambda: self.browse_page(current_user))
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

    def browse_page(self, current_user):
        other_user = manager.recommend_user(current_user)

        self.label.destroy()
        self.label = Label(self.window, text=f"You are viewing {other_user.name}'s profile", font=('Arial', 16))
        self.label.grid(row=0, column=0)

        # Clear the canvas to show the user profile details
        self.canvas.delete("all")

        self.canvas.create_text(100, 150, text="Name", font=('Arial', 16))
        self.canvas.create_text(100, 200, text="Age", font=('Arial', 16))
        self.canvas.create_text(100, 250, text="Gender", font=('Arial', 16))
        self.canvas.create_text(100, 300, text="Location", font=('Arial', 16))
        self.canvas.create_text(100, 350, text="Interests", font=('Arial', 16))

        self.canvas.create_text(300, 150, text=other_user.name, font=('Arial', 16))
        self.canvas.create_text(300, 200, text=other_user.age, font=('Arial', 16))
        self.canvas.create_text(300, 250, text=other_user.gender, font=('Arial', 16))
        self.canvas.create_text(300, 300, text=other_user.location, font=('Arial', 16))
        self.canvas.create_text(300, 350, text=','.join(current_user.interests), font=('Arial', 16))

        # Remove buttons from previous page
        self.commandcanvas.delete("all")

        # Function to change the button's appearance on hover
        def on_enter(e, button):
            button['background'] = 'lightblue'  # Highlight color

        def on_leave(e, button):
            button['background'] = 'SystemButtonFace'  # Default color

        # Show user options with hover effects
        self.like_button = Button(self.window, text="LIKE", font=('Arial', 16), command=lambda: self.like_user(current_user, other_user))
        self.like_button.bind("<Enter>", lambda e: on_enter(e, self.like_button))
        self.like_button.bind("<Leave>", lambda e: on_leave(e, self.like_button))
        self.commandcanvas.create_window(90, 30, window=self.like_button)

        self.dislike_button = Button(self.window, text="DISLIKE", font=('Arial', 16), command=lambda: self.dislike_user(current_user, other_user))
        self.dislike_button.bind("<Enter>", lambda e: on_enter(e, self.dislike_button))
        self.dislike_button.bind("<Leave>", lambda e: on_leave(e, self.dislike_button))
        self.commandcanvas.create_window(230, 30, window=self.dislike_button)

        self.back_to_profile = Button(self.window, text="Back to My Profile", font=('Arial', 16), command=lambda: self.profile_page(current_user))
        self.back_to_profile.bind("<Enter>", lambda e: on_enter(e, self.back_to_profile))
        self.back_to_profile.bind("<Leave>", lambda e: on_leave(e, self.back_to_profile))
        self.commandcanvas.create_window(400, 30, window=self.back_to_profile)

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
            self.liked_entry = OptionMenu(self.window, selected_user, *list(user_dict.keys()))
            self.commandcanvas.create_window(90, 30, window=self.liked_entry)

            self.display_button = Button(self.window, text="Display Selected User Profile", font=('Arial', 16),
                                  command=lambda: self.display_profile(user_dict[selected_user.get()]))
            self.commandcanvas.create_window(300, 30, window=self.display_button)

        self.back_to_profile = Button(self.window, text="Back to My Profile", font=('Arial', 16),
                                      command=lambda: self.profile_page(current_user))
        self.commandcanvas.create_window(300, 80, window=self.back_to_profile)

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
            selected_user = StringVar()
            self.disliked_entry = OptionMenu(self.window, selected_user, *list(user_dict.keys()))
            self.commandcanvas.create_window(90, 30, window=self.disliked_entry)

            self.display_button = Button(self.window, text="Display Selected User Profile", font=('Arial', 16),
                                  command=lambda: self.display_profile(user_dict[selected_user.get()]))
            self.commandcanvas.create_window(300, 30, window=self.display_button)

        self.back_to_profile = Button(self.window, text="Back to My Profile", font=('Arial', 16),
                                      command=lambda: self.profile_page(current_user))
        self.commandcanvas.create_window(300, 80, window=self.back_to_profile)

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

    def delete_current_user(self, current_user):
            confirmation = messagebox.askyesno("Delete Profile", "Are you sure you want to delete your profile?")
            if confirmation:
                manager.delete_user(current_user.user_id)
                messagebox.showinfo("Profile Deleted", "Your profile has been deleted successfully.")
                # Redirect to the login page or exit the application
                self.log_in_page()


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

    def like_user(self, current_user, other_user):
        #The returned result is a list of booleans, first indicate if this person is already liked, second indicate if this person is matched
        result = manager.like_user(current_user.user_id, other_user.user_id)

        if result[0] == True:
            current_user.liked_users.append(other_user.user_id)
            messagebox.showinfo(title="Thank you!", message="You LIKE has been saved")
            if result[1] == True:
                current_user.matched_users.append(other_user.user_id)
        else:
            messagebox.showinfo(title="oops!", message="You already liked this person")
        self.browse_page(current_user)

    def dislike_user(self, current_user, other_user):
        result = manager.dislike_user(current_user.user_id, other_user.user_id)
        if result == True:
            current_user.disliked_users.append(other_user.user_id)
            messagebox.showinfo(title="Thank you!", message="You DISLIKE has been saved")
        else:
            messagebox.showinfo(title="oops!", message="You already disliked this person")
        self.browse_page(current_user)

    def compare_users(self):
        user_id1 = int(self.id_entry.get())
        self.compare_id_entry = Entry(self.window, font=('Arial', 16), width=8)
        self.compare_id_entry.grid(row=3, column=2)

        compare_button = Button(self.window, text="Get Compatibility", font=('Arial', 16),
                                command=lambda: manager.compare_users(user_id1, int(self.compare_id_entry.get())))
        compare_button.grid(row=3, column=3)


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
        self.liked_users = list(map(int,liked_users.split(','))) if liked_users != '' else []
        self.disliked_users = list(map(int,disliked_users.split(','))) if disliked_users != '' else []
        self.matched_users = list(map(int,matched_users.split(','))) if matched_users != '' else []
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
            INSERT INTO users (name, age, gender, location, interests, liked_users, disliked_users, matches)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (self.name, self.age, self.gender, self.location, ','.join(self.interests),'','',''))
        self.user_id = cursor.lastrowid
        conn.commit()

    #This function is not needed, user update function in UserManager Class
    '''
    def update_profile(self, conn: sqlite3.Connection, name: Optional[str] = None, age: Optional[int] = None,
                    gender: Optional[str] = None, location: Optional[str] = None,
                    interests: Optional[List[str]] = None, liked_users: Optional[List[int]] = None,
                    disliked_users: Optional[List[int]] = None, matched_users: Optional[List[int]] = None) -> None:
        cursor = conn.cursor()
        # Retrieve the current values if not provided
        cursor.execute("SELECT name, age, gender, location, interests, liked_users, disliked_users, matches FROM users WHERE user_id = ?", (self.user_id,))
        current_values = cursor.fetchone()
        if current_values:
            current_name, current_age, current_gender, current_location, current_interests, \
            current_liked_users, current_disliked_users, current_matched_users = current_values
            self.name = name if name is not None else current_name
            self.age = age if age is not None else current_age
            self.gender = gender if gender is not None else current_gender
            self.location = location if location is not None else current_location
            self.interests = interests if interests is not None else current_interests.split(',')
            self.liked_users = liked_users if liked_users is not None else current_liked_users.split(',') if current_liked_users else []
            self.disliked_users = disliked_users if disliked_users is not None else current_disliked_users.split(',') if current_disliked_users else []
            self.matched_users = matched_users if matched_users is not None else current_matched_users.split(',') if current_matched_users else []

            # Update the database
            cursor.execute("""
                UPDATE users
                SET name = ?, age = ?, gender = ?, location = ?, interests = ?, liked_users = ?, disliked_users = ?, matches = ?
                WHERE user_id = ?
            """, (self.name, self.age, self.gender, self.location, ','.join(self.interests),
                ','.join(map(str, self.liked_users)),
                ','.join(map(str, self.disliked_users)),
                ','.join(map(str, self.matched_users)),
                self.user_id))
            conn.commit()
            print(f"User {self.user_id} updated successfully!")
        else:
            print(f"User {self.user_id} not found!")


    def view_profile(self) -> None:
        print(f"ID: {self.user_id}, Name: {self.name}, Age: {self.age}, "
              f"Gender: {self.gender}, Location: {self.location}, "
              f"Interests: {', '.join(self.interests)}")'''
        
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
                temp_user = UserProfile(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                user_dict.update({str(row[0]) + ': ' + row[1]: [row[0], row[1], row[2], row[3], row[4], row[5]]})
            return user_dict

    def compare_users(self, user_id1: int, user_id2: int) -> None:
        if self.user_exists(user_id1) and self.user_exists(user_id2):
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id1,))
            row1 = cursor.fetchone()
            user1 = UserProfile(row1[0], row1[1], row1[2], row1[3], row1[4], row1[5],row1[6],row1[7],row1[8])

            cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id2,))
            row2 = cursor.fetchone()
            user2 = UserProfile(row2[0], row2[1], row2[2], row2[3], row2[4], row2[5],row2[6],row2[7],row2[8])

            compatibility_score = user1.calculate_compatibility(user2)
            if compatibility_score is not None:
                print(f"The compatibility score between User {user1.name} and User {user2.name} is: {compatibility_score}%")
            else:
                print("Unable to calculate compatibility score due to missing location data.")
        else:
            print("One or both user IDs do not exist.")

    def update_user(self, current_user, name, age, gender, location, interests):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (current_user.user_id,))
        row = cursor.fetchone()

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


    def view_user(self, user_id: int) -> None:
        if self.user_exists(user_id):
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
            row = cursor.fetchone()
            user = UserProfile(row[0], row[1], row[2], row[3], row[4], row[5],row[6],row[7],row[8])
            user.view_profile()
        else:
            print(f"User ID {user_id} does not exist.")

    #Working delete user method that deletes all instances of the user in the database in liked_users, disliked_users and matches
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

        

    def view_all_users(self) -> None:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            user = UserProfile(row[0], row[1], row[2], row[3], row[4], row[5],row[6],row[7],row[8])
            user.view_profile()

    def recommend_user(self, current_user):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users ORDER BY user_id DESC LIMIT 1")
        last_user = cursor.fetchone()
        recommend = randint(1, last_user[0])
        if recommend == current_user.user_id:
            recommend += 1
        while recommend in current_user.liked_users or recommend in current_user.disliked_users:
            recommend = randint(1, current_user.user_id - 1)
        cursor.execute("SELECT * FROM users WHERE user_id = ?", (recommend,))
        row = cursor.fetchone()
        other_user = UserProfile(row[0], row[1], row[2], row[3], row[4], row[5],row[6],row[7],row[8])
        return other_user



def fetch_all_users():
    conn = sqlite3.connect('users.db')
    global df
    df = pd.read_sql_query("SELECT * FROM users", conn)
    # Convert each comma-separated string in the 'interests' column to a list of interests
    df['interests'] = df['interests'].apply(
        lambda x: x.split(',') if x else [])
        # lambda x:        -> Defines an anonymous function with 'x' as the input (each element in the 'interests' column)
        # x.split(',')     -> Splits the string 'x' by commas into a list (e.g., "hiking,reading" becomes ['hiking', 'reading'])
        # if x             -> Checks if 'x' is not empty or None. If 'x' has content, split it by commas.
        # else []          -> If 'x' is empty or None, return an empty list instead of trying to split 'x'

    conn.close()
    return df

       


# Compute Compatibility Scores
def compute_compatibility_scores(logged_in_user, users_df):
    # Exclude the logged-in user from potential matches
    # exclude yourself
    potential_matches = users_df[users_df['user_id'] != logged_in_user.user_id].copy()
    # Calculate **location** compatibility score using a boolean mask and convert to float
    # original approach
    # potential_matches['location_score'] = (potential_matches['location'] == logged_in_user.location).astype(
    #    float)

    # updated Calculated **location** compatibility score -> use Geo-location
    potential_matches['location_score'] = calculate_compatibility(logged_in_user, potential_matches)

    # Alternative is to go over location by location and set to 1.0 when matches and 0.0 if doesn't
    # more creative: use Geo-location (so convert address to GPS point)

    # we also want to consider gender as a factor that can affect the matching sco

    # Calculate **age** difference score using NumPy's vectorized operations
    potential_matches['age_diff_score'] = 1 / (1 + np.abs(potential_matches['age'] - logged_in_user.age))

    #INTEREST SCORE

    # Convert interests lists into a set for the logged-in user for faster comparison
    logged_in_interests_set = set(logged_in_user.interests)

    # Optimize shared interests score calculation using list comprehension and apply
    def calculate_interest_similarity(interests):
        interests_set = set(interests)
        intersection = len(logged_in_interests_set & interests_set)
        union = len(logged_in_interests_set | interests_set)
        return intersection/union if union > 0 else 0
        
    potential_matches['interests_score'] = potential_matches['interests'].apply(calculate_interest_similarity)
    
    # Convert **interests** lists into a set for the logged-in user for faster comparison
    # logged_in_interests_set = set(logged_in_user.interests)

    # Optimize shared interests score calculation using list comprehension and apply
    # def calculate_jaccard_similarity_vectorized(interests):

                # Calculate intersection and union sizes directly
             
        #category = []
        #for interest in df["interests"]:
            #if interest in ["cycling", "hiking", "swimming", "dancing", "running", "sports", "yoga"]:
                #category.append("Sports")
            #elif interest in ["music", "art", "painting"]:
                #category.append("Art")
            #elif interest in ["gardening", "fishing", "photography", "travelling", "cooking"]:
                #category.append("Lifestyle")
            #elif interest in ["reading", "coding", "writing", "gaming"]:
                #category.append("Intellectual")

        #category_set = set(category)
        #logged_in_category_set = set(logged_in_user.category)
        #intersection_size = len(logged_in_category_set & category_set)
        #union_size = len(logged_in_category_set | category_set)

        # Return the Jaccard similarity score
        #return intersection_size / union_size if union_size > 0 else 0

    # Apply the vectorized Jaccard similarity calculation to all potential matches
    potential_matches['interests_score'] = potential_matches['interests'].apply(
        calculate_jaccard_similarity_vectorized)

    # Combine the individual scores into a final compatibility score using NumPy's vectorized operations
    potential_matches['compatibility_score'] = (
             0.25 * potential_matches['location_score'] +
            0.5 * potential_matches['age_diff_score'] +
            0.25 * potential_matches['interests_score'])
    #may update with kevin's code later
   
  


    

    # Sort by the compatibility score in descending order
    potential_matches = potential_matches.sort_values(by='compatibility_score', ascending=False)

    return potential_matches

    # Rank the Potential Matches and Display the Top 3
def display_top_matches(potential_matches, top_n=3):
    top_matches = potential_matches[['user_id', 'name', 'location', 'age', 'compatibility_score']].head(top_n)
    print("Top Matches:")
    print(top_matches)
    return top_matches



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
#Load All Users into a Pandas DataFrame
