

#task_003

import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    length = int(length_var.get())
    include_uppercase = uppercase_var.get()
    include_numbers = numbers_var.get()
    include_special = special_var.get()

    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)


root = tk.Tk()
root.title("Password Generator")

length_var = tk.StringVar(value='12')
uppercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
special_var = tk.BooleanVar()
password_var = tk.StringVar()


tk.Label(root, text="Password Length:").grid(row=0, column=0, sticky="w")
tk.Entry(root, textvariable=length_var, width=5).grid(row=0, column=1, sticky="w")

tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var).grid(row=1, columnspan=2, sticky="w")
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).grid(row=2, columnspan=2, sticky="w")
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).grid(row=3, columnspan=2, sticky="w")

tk.Button(root, text="Generate Password", command=generate_password).grid(row=4, columnspan=2)

tk.Entry(root, textvariable=password_var, width=40).grid(row=5, columnspan=2)


root.mainloop()

