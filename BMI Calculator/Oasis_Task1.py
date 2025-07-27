#!/usr/bin/env python
# coding: utf-8

# # Beginner Version: Command-line BMI Calculator

# In[1]:


def get_user_input():
    while True:
        try:
            weight = float(input("Enter your weight in kilograms: "))
            height = float(input("Enter your height in meters: "))
            if weight > 0 and height > 0:
                return weight, height
            else:
                print("Weight and height must be positive numbers.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    weight, height = get_user_input()
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)
    print(f"Your BMI is {bmi:.2f}, which is considered {category}.")

if __name__ == "__main__":
    main()


# # Advanced Version: GUI BMI Calculator

# In[2]:


import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        if weight > 0 and height > 0:
            bmi = weight / (height ** 2)
            category = classify_bmi(bmi)
            label_result.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")
        else:
            messagebox.showerror("Input Error", "Weight and height must be positive numbers.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

app = tk.Tk()
app.title("BMI Calculator")

tk.Label(app, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=5)
entry_weight = tk.Entry(app)
entry_weight.grid(row=0, column=1, padx=10, pady=5)

tk.Label(app, text="Height (m):").grid(row=1, column=0, padx=10, pady=5)
entry_height = tk.Entry(app)
entry_height.grid(row=1, column=1, padx=10, pady=5)

btn_calculate = tk.Button(app, text="Calculate BMI", command=calculate_bmi)
btn_calculate.grid(row=2, column=0, columnspan=2, pady=10)

label_result = tk.Label(app, text="BMI: \nCategory: ")
label_result.grid(row=3, column=0, columnspan=2, pady=10)

app.mainloop()

