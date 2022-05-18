# The tkinter package is the standard Python interface to the
# Tcl/Tk GUI toolkit.
from tkinter import *

# The OS module in Python provides functions for interacting with
# the operating system.
import os

# This is the login module, which defines successful and unsuccessful
# login outcomes.
def login():

    # These are the variables for retrieving username and password from file.
    UNverify = username.get()
    PWverify = password.get()

    # Deletes username and password text if login is successful or unsuccessful.
    un_entry.delete(0, END)
    pw_entry.delete(0, END)

    # This is the variable set for the file that contains list of users.
    # UNverify and PWverify will get the username and password from this file.
    list_of_users = os.listdir()

    # If the username matches that on list_of_users then checks password.
    # If the password also matches then pong.py opens in new window.
    # Else the system will display message Incorrect username or password.
    if UNverify in list_of_users:
        file1 = open(UNverify, "r")
        pw = file1.read().splitlines()
        if PWverify in pw:
            os.startfile("pong.py")
        else:
            print("Incorrect username or password")
    else:
        print("Incorrect username or password")

# This determines action when clicking Submit button on Registration screen.
def submit():

    # These are the variables for registering new username and password.
    # Variables are global.
    global username_info
    global password_info
    username_info = reg_username.get()
    password_info = reg_password.get()

    # Opens temp file to create username and password before
    # uploading to list directory above.
    file1 = open(username_info, "w")
    file1.write(password_info)
    file1.close()

    # Deletes username and password if registration is successful or unsuccessful.
    unreg_entry.delete(0, END)
    pwreg_entry.delete(0, END)

# This determines action when clicking Register button on Login screen.
def register():

    # Opens new window on clicking Register, allowing user to create credentials.
    register_screen = Toplevel(root)

    # Labels for Registration screen.
    label3 = Label(register_screen, text= "Enter chosen username ")
    label4 = Label(register_screen, text="Enter chosen password ")

    # These are string variables for username and password so they can be reused.
    global reg_username
    global reg_password
    reg_username = StringVar()
    reg_password = StringVar()

    # This sets a variable to a username entry box and password entry box.
    # On entry, the text becomes the variable reg_username and reg_password.
    # Text box variables are global.
    global unreg_entry
    global pwreg_entry
    unreg_entry = Entry(register_screen, textvariable = reg_username)
    # For security purposes masking (*) is used.
    pwreg_entry = Entry(register_screen, textvariable = reg_password, show= "*")

    # Create Account button for Registration screen.  Clicking will save
    # username and password to directory.
    button3 = Button(register_screen, text= "Create account", command = submit)

    # Positions text boxes on Registration screen.
    unreg_entry.grid(row=0, column=1)
    pwreg_entry.grid(row=1, column=1)

    # Positions labels on Registration screen.
    label3.grid(row=0, column=0)
    label4.grid(row=1, column=0)

    # Positions Create Account button on Registration screen.
    button3.grid(row=2, column=0)

# This is the module for default Login screen.
def mainscreen():

    # Opens new window using the tkinter library.
    # Window is global.
    global root
    root = Tk()

    # Title for Login and Registration screens.
    root.title('Pong game')

    # Labels for Login screen.
    label1 = Label(root, text= "Enter username ")
    label2 = Label(root, text="Enter password ")

    # This sets a string variable to username and password for reuse.
    # Variables are global.
    global username
    global password
    username = StringVar()
    password = StringVar()

    # This sets a variable to a username entry box and password entry box.
    # On entry, the text becomes the variable un_entry and pw_entry.
    # Text box variables are global.
    global un_entry
    global pw_entry
    un_entry = Entry(root, textvariable = username)

    # For security purposes masking (*) is used.
    pw_entry = Entry(root, textvariable = password, show= "*")

    # On clicking Login button, login module is run.
    button1 = Button(root, text= "Login", command = login)

    # On clicking Register button register module is run.
    button2 = Button(root, text="Register", command= register)

    # Positions labels on Login screen.
    label1.grid(row=0, column=0)
    label2.grid(row=1, column=0)

    # Positions text boxes on Login screen.
    un_entry.grid(row=0, column=1)
    pw_entry.grid(row=1, column=1)

    # Positions buttons on Login screen.
    button1.grid(row=2, column=0)
    button2.grid(row=2, column=2)

    # This tells Python to run the Tkinter event loop. It will listen for
    # events, such as button clicks or key presses.
    mainloop()

# This initiates the program, after which program is event-driven.
mainscreen()

