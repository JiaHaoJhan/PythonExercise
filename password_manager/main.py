from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


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


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()

    if len(website_data) == 0 or len(email_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Oops!!", message="Please don't leave any fields empty! ")
    else:
        is_ok = messagebox.askokcancel(title="Password Manager", message=f"These are the details:\n"
                                                                         f"{website_data}\n"
                                                                         f"{email_data}\n"
                                                                         f"{password_data}\n"
                                                                         f"Is it ok to save? ")
        if is_ok:
            with open("password_manager.txt", 'a') as data:
                data.write(f"{website_data} | {email_data} | {password_data} \n")
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")
            messagebox.showinfo(title="Password Manager", message="Save succeed~")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=45)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# email
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=45)
email_entry.insert(0, "myEmail@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

# password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=28)
password_entry.grid(column=1, row=3)
password_button = Button(text="Generate Password", command=password_generator)
password_button.grid(column=2, row=3)


# add
add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
