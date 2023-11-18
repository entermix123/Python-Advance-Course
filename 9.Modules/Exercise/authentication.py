from buying_page import display_products
# import loads conversion from string to dictionary (python object), dump data to file or db
from json import loads, dump
from tkinter import Button, Entry       # import buttons and fields
from canvas import root, frame          # import root and frames
from helpers import clean_screen, get_password_hash  # import clean screen function and encoding passwords


def get_users_data():       # create function for taking user info form user info file
    info_data = []          # create empty list

    with open('db/user_info.txt', 'r') as user_file:        # open file user_info.txt
        for line in user_file:                              # iterate true user file
            info_data.append(loads(line))                   # take user input, convert to dictionary and append to file

    return info_data


def render_entry():

    register_btn = Button(  # register button definition
        root,
        text='Register',    # button text
        bg='green',         # background color
        fg='white',         # front color
        borderwidth=0,      # border setting
        width=20,           # size width
        height=3,           # size height
        command=register    # action call function register that clean screen
        )

    login_btn = Button(     # login button definition
        root,
        text='Login',       # button text
        bg='blue',          # background color
        fg='white',         # front color
        borderwidth=0,      # border setting
        width=20,           # size width
        height=3,           # size height
        command=login,
    )

    # call create window function to create register button with location
    frame.create_window(350, 260, window=register_btn)

    # call create window function to create login button with location
    frame.create_window(350, 320, window=login_btn)

    # call create text function to create text with location and settings
    frame.create_text(350, 100, text='HELLO', font=("Cosmic Sans MS", 30))


def login():
    clean_screen()

    frame.create_text(100, 50, text="username:")
    frame.create_text(100, 100, text="password:")

    frame.create_window(200, 50, window=user_name_field)
    frame.create_window(200, 100, window=password_field)

    logging_btn = Button(
        root,
        text="Login",
        bg="blue",          # can be user color picker with 16th bits values
        fg="white",
        command=logging,
    )

    frame.create_window(250, 150, window=logging_btn)


def logging():
    if check_logging():
        display_products()

    else:
        frame.create_text(160, 200, text="Invalid username or password!", fill="red")


def check_logging():
    info_data = get_users_data()                # take user input data in list
    user_username = user_name_field.get()       # take user input for username
    user_password = get_password_hash(password_field.get())        # take user input for password

    for i in range(len(info_data)):
        username = info_data[i]["username"]     # check if username is in db dictionary
        password = info_data[i]["password"]     # check if password is in db dictionary

        if username == user_username and password == user_password:
            return True

    return False


def register():                     # create register screen after register button action
    clean_screen()                  # clear screen after register button action

    frame.create_text(100, 50, text='First name')  # create text First name before input field with location and settings
    frame.create_text(100, 100, text='Last name')  # create text Last name before input field with location and settings
    frame.create_text(100, 150, text='Username')   # create text Username before input field with location and settings
    frame.create_text(100, 200, text='Password')   # create text Password before input field with location and settings

    frame.create_window(200, 50, window=first_name_field)   # connect text field for First name to the grid
    frame.create_window(200, 100, window=last_name_field)   # connect text field for Last name to the grid
    frame.create_window(200, 150, window=user_name_field)   # connect text field for Username to the grid
    frame.create_window(200, 200, window=password_field)    # connect text field for Password to the grid

    registration_btn = Button(      # create register confirmation button
        root,
        text='Register',
        bg='green',
        fg='white',
        command=registration,
        )

    frame.create_window(300, 250, window=registration_btn)      # add register confirmation button


def registration():         # definition of confirmation registration button function in register page
    info_dict = {
        "first_name": first_name_field.get(),   # take information input from user in first name field
        "last_name": last_name_field.get(),     # take information input from user in last name field
        "username": user_name_field.get(),      # take information input from user in username field
        "password": get_password_hash(password_field.get()),   # take information input from user in password field
    }

    if check_registration(info_dict):                       # if registration is with valid data input
        with open("db/user_info.txt", "a") as user_file:    # open db user_info
            dump(info_dict, user_file)                      # save user input
            user_file.write("\n")                           # make new row for every user
            display_products()                              # display products


def check_registration(info):
    for el in info.values():                        # iterate true input user data
        if not el.strip():                          # check if stripped element is not empty
            frame.create_text(                      # create screen text
                300,
                300,
                text='We are missing information',  # print info
                fill='red',                         # fill the text box with color
                tag='error'                         # config error tag
            )

            return False

    frame.delete('error')                           # after correct input, clean errors

    info_data = get_users_data()                    # if correct data in input, save data to list

    for record in info_data:                        # iterate true input data
        if record["username"] == info["username"]:  # if username is in db dictionary username keys
            frame.create_text(                      # raise error text with location and settings
                300,
                300,
                text="Username already exists!",
                fill="red",
                tag="error"
            )

            return False

    frame.delete("error")

    return True


first_name_field = Entry(root, bd=0)    # create text field for First name input with location
last_name_field = Entry(root, bd=0)     # create text field for Last name input with location
user_name_field = Entry(root, bd=0)     # create text field for Username input with location
password_field = Entry(root, bd=0, show='*')  # create text field for Password input with location and setting - '*'
