#!/usr/bin/env python
# coding: utf-8

# # Beginner Level: Command-Line Random Password Generator

# In[1]:


import random
import string

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    character_set = string.ascii_lowercase
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def main():
    length = int(input("Enter password length: "))
    use_uppercase = input("Use uppercase letters? (yes/no): ").lower() == 'yes'
    use_numbers = input("Use numbers? (yes/no): ").lower() == 'yes'
    use_symbols = input("Use symbols? (yes/no): ").lower() == 'yes'
    
    password = generate_password(length, use_uppercase, use_numbers, use_symbols)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()


# # Advanced Level: GUI Random Password Generator using Tkinter

# In[ ]:


import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    character_set = string.ascii_lowercase
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def generate():
    try:
        length = int(length_entry.get())
        use_uppercase = uppercase_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()
        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for length.")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_entry.get())
    root.update() # now it stays on the clipboard after the window is closed
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Length:").grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

uppercase_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var).grid(row=1, column=0, columnspan=2)

numbers_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).grid(row=2, column=0, columnspan=2)

symbols_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).grid(row=3, column=0, columnspan=2)

tk.Button(root, text="Generate", command=generate).grid(row=4, column=0, columnspan=2)

tk.Label(root, text="Generated Password:").grid(row=5, column=0)
result_entry = tk.Entry(root)
result_entry.grid(row=5, column=1)

tk.Button(root, text="Copy", command=copy_to_clipboard).grid(row=6, column=0, columnspan=2)

root.mainloop()

