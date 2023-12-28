from tkinter import *
import os
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


#def add():
 #   print("I got clicked")
 #add infor to note
  #  new_text = input.get()
   # my_label.config(text=new_text)

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
# canvas.create_image(100, 100, image=logo_img)
# canvas.pack()
logo_label = Label(image=logo_img)
logo_label.grid(column=1, row=0, columnspan=3)


#
# Button ADD
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=3, row=3)

add_button = Button(text="Add", width=36) #, command=save_password)
add_button.grid(column=1, row=4, columnspan=3)

#Labels and Boxs
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_label = Label(text="Website:", font=("Arial", 14, "bold"))
website_label.grid(column=0, row=1)

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_label = Label(text="Email/Username:", font=("Arial", 14, "bold"))
email_label.grid(column=0, row=2)

password_input = Entry(width=21)
password_input.grid(column=1, row=3, columnspan=2)
password_label = Label(text="Password:", font=("Arial", 14, "bold"))
password_label.grid(column=0, row=3)


window.mainloop()
# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #