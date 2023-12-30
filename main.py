from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 14))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_numbers + password_letters
    shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please mae sure you haven't left any fields empty")
    else:
        try:
            with open("data.json", 'r') as data_file:
                # Reading old data
                data = json.load(data_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            # Create an empty dictionary if the file doesn't exist or is empty
            data = {}

            # Updating old data with new data
        data.update(new_data)

        with open("data.json", 'w') as data_file:
            # Saving updated data
            json.dump(data, data_file, indent=4)

        messagebox.showinfo(title="Success", message="Password saved successfully")
        website_input.delete(0, END)
        password_input.delete(0, END)

# ---------------------------- Search ------------------------------- #
def find_password():
    website = website_input.get()
    try:
        with open("data.json", 'r') as data_file:
            # Reading old data
            data = json.load(data_file)
            # Verificar se o website está nos dados
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\n\nPassword: {password}")
            else:
                messagebox.showerror(title="Erro", message="No deatails for the website exists")
    except FileNotFoundError:
        messagebox.showerror(title="Erro", message="No Data File Found")

    website_input.delete(0, END)
    password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0,column=1)

# Button ADD and Generate Password
generate_password_button = Button(text="Generate Password", command=gen_password)
generate_password_button.grid(column=3, row=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=3)
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=3, row=1)

# Labels
website_label = Label(text="Website:", font=("Arial", 10, "bold"))
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", font=("Arial", 10, "bold"))
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=("Arial", 10, "bold"))
password_label.grid(column=0, row=3)

# Boxs
website_input = Entry(width=32)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
email_input = Entry(width=51)
email_input.insert(0, " vascobfrances@gmail.com")
email_input.grid(column=1, row=2, columnspan=3)
password_input = Entry(width=32)
password_input.grid(column=1, row=3, columnspan=2)

window.mainloop()