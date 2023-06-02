from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

BUTTON_WIDTH = 16
ENTRY_WIDTH = 25
PROGRAM_TITLE = "Password Manager"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, "end")
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- FIND PASSWORD ------------------------------- #
def website_search_password():
    website_data = website_entry.get()
    # 1. no data
    try:
        with open("password_manager.json", 'r') as data_open:
            data = json.load(data_open)
    except FileNotFoundError:
        messagebox.showinfo(title=PROGRAM_TITLE, message="No Data File Found!")
    else:
        if website_data in data:
            load_email = data[website_data]['email']
            load_password = data[website_data]['password']
            messagebox.showinfo(title=PROGRAM_TITLE,
                                message=f"Your {website_data}\n Email: {load_email} \nPassword: {load_password}")
            pyperclip.copy(load_password)
        else:
            messagebox.showinfo(title=PROGRAM_TITLE, message=f"No details for the {website_data} exists!")




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()
    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data
        }
    }

    if len(website_data) == 0 or len(email_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Oops!!", message="Please don't leave any fields empty! ")
    else:
        try:
            with open("password_manager.json", 'r') as data_open:
                data = json.load(data_open)
        except FileNotFoundError:
            with open("password_manager.json", 'w') as data_open:
                json.dump(new_data, data_open, indent=4)
        else:
            data.update(new_data)
            with open("password_manager.json", 'w') as data_open:
                json.dump(data, data_open, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)
        messagebox.showinfo(title=PROGRAM_TITLE, message="Save succeed~")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title(PROGRAM_TITLE)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=ENTRY_WIDTH)
website_entry.grid(column=1, row=1)
website_entry.focus()
website_search_button = Button(text="Search", width=BUTTON_WIDTH, command=website_search_password)
website_search_button.grid(column=2, row=1)

# email
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=ENTRY_WIDTH)
email_entry.insert(0, "myEmail@gmail.com")
email_entry.grid(column=1, row=2)

# password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=ENTRY_WIDTH)
password_entry.grid(column=1, row=3)
password_button = Button(text="Generate Password", width=BUTTON_WIDTH, command=password_generator)
password_button.grid(column=2, row=3)


# add
add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
