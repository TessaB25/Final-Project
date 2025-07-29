#Author: Christina C. Buchanan
#Date: 7/24/2025
#Description: Part 2: The retirement calculator


from tkinter import *
from tkinter import messagebox

#Module to handle retirement savings calculation
def create_retirement_section(root):
    def calculate_retirement():
        try:
            age = int(entry_age.get())  #Current age
            retire_age = int(entry_retire_age.get())  #Desired retirement age
            goal = float(entry_goal.get())  #Goal amount
            current = float(entry_current.get())  #Current savings
            rate = float(entry_return.get()) / 100  #Annual interest rate

            if any(val < 0 for val in [age, retire_age, goal, current, rate]):
                raise ValueError("Negative values are not allowed.")
            if retire_age <= age:
                messagebox.showerror("Input Error", "Retirement age must be greater than current age.")
                return

            years = retire_age - age
            months = years * 12
            monthly_rate = rate / 12

            future_savings = current * ((1 + monthly_rate) ** months)
            needed = goal - future_savings

            if needed <= 0:
                result.config(text="You're already on track!")
                return

            monthly_save = (needed * monthly_rate) / (((1 + monthly_rate) ** months) - 1)
            result.config(text=f"You need to save ${monthly_save:.2f} per month.")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values for all fields.")

    Label(root, text="--- Retirement Calculator ---", font=("Arial", 14, "bold")).pack(pady=10)

    Label(root, text="Current Age:").pack()
    entry_age = Entry(root)
    entry_age.pack()

    Label(root, text="Retirement Age:").pack()
    entry_retire_age = Entry(root)
    entry_retire_age.pack()

    Label(root, text="Goal Amount ($):").pack()
    entry_goal = Entry(root)
    entry_goal.pack()

    Label(root, text="Current Savings ($):").pack()
    entry_current = Entry(root)
    entry_current.pack()

    Label(root, text="Expected Annual Return (%):").pack()
    entry_return = Entry(root)
    entry_return.pack()

    Button(root, text="Calculate Retirement Needs", command=calculate_retirement).pack(pady=5)
    result = Label(root, text="", wraplength=400, justify="center")
    result.pack()
