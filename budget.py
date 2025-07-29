#Author: Christina C. Buchanan
#Date: 7/22/2025
#Description: Part 1: The budget code

#budget.py
from tkinter import *
from tkinter import messagebox

#Function to calculate budget based on detailed individual expenses
def calculate_budget(entry_income, entries, result_label):
    try:
        monthly_income = float(entry_income.get())  #Get and convert monthly income
        total_expenses = 0

        for label, entry in entries.items():
            value = entry.get()
            if value.strip() == "":
                value = "0"
            expense = float(value)
            total_expenses += expense  #Sum each individual expense

        savings = monthly_income - total_expenses
        result_label.config(text=f"Monthly Savings: ${savings:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers in all fields.")


#Function to create the budget section UI and return it as a frame
def create_budget_section(root):
    frame = Frame(root)
    frame.pack(pady=10)

    Label(frame, text="--- Monthly Budget ---", font=("Arial", 14, "bold")).pack(pady=5)

    Label(frame, text="Monthly Income ($):").pack()
    entry_income = Entry(frame)
    entry_income.pack()

    #Define individual expense categories
    expense_labels = [
        "Rent/Mortgage", "Water", "Electricity", "Gas", "Internet",
        "Tithes & Offering", "Charities", "Auto Gas", "Car Insurance",
        "Groceries", "Lifestyle Expenses", "Subscriptions",
        "Necessities", "Credit Card Debt", "Student Loans", "Personal Loans"
    ]

    entries = {}  #Dictionary to store Entry widgets for each expense
    for label in expense_labels:
        Label(frame, text=f"{label} ($):").pack()
        entry = Entry(frame)
        entry.pack()
        entries[label] = entry

    #Result label for savings
    result_label = Label(frame, text="")
    result_label.pack(pady=5)

    #Button to trigger budget calculation
    Button(
        frame,
        text="Calculate Budget",
        command=lambda: calculate_budget(entry_income, entries, result_label)
    ).pack(pady=10)

    return frame

