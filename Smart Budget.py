#Author: Christina C. Buchanan
#Date 7/7/2025
#Assignment: Final Project
#Description: This is a budget and retirement calculator.  The budget section lets you know how much you have left over to put in savings and the retirement calculator lets you know how much you'll need per month to reach your goals.

#main.py
from tkinter import * #Import all Tkinter functions
from tkinter import messagebox #For dialog boxes like exit confirmation
from tkinter import Toplevel  #For creating additional windows
from PIL import Image, ImageTk  #For handling and displaying image files
import budget  #Custom module for budget calculator
import retirement #Custom module for retirement calculator

# --- Main Menu Callback Functions ---

def open_budget_window():  #Opens a secondary window with app information
    """Opens a new window for the Budget Calculator."""
    budget_win = Toplevel(root) #Creates a new top-level window
    budget_win.title("Budget Calculator")  #Sets title
    budget_win.geometry("500x1000")  #Sets window size (width x height)

    Label(budget_win, text="Budget Calculator", font=("Arial", 14, "bold")).pack(pady=10)  #Budget calculator button description

    #Images
    img1 = Image.open("budget_icon.png") #Loads image from PNG file
    img1 = img1.resize((80, 80))  #Resizes image to 80X80 pixels
    img1_tk = ImageTk.PhotoImage(img1)  #Converts to format that Tkinter can display
    Label(budget_win, image=img1_tk).pack()  #Diplays the image on the screen
    Label(budget_win, text="Budget", font=("Arial", 12)).pack()  #Text label for accessibility
    budget_win.image = img1_tk  #Keep reference!

    #Inject budget tools
    budget.create_budget_section(budget_win)  #Creates the budget input section from budget.py module


def open_retirement_window():  #Opens a secondary window with app information
    """Opens a new window for the Retirement Calculator."""
    retire_win = Toplevel(root)  #Creates a new top-level window
    retire_win.title("Retirement Calculator")  #Sets title
    retire_win.geometry("500x600")  #Sets window size (width x height)

    Label(retire_win, text="Retirement Calculator", font=("Arial", 14, "bold")).pack(pady=10)  #Retirement calculator button description

    #Images
    img2 = Image.open("retirement_icon.png")  #Loads image from PNG file
    img2 = img2.resize((80, 80))  #Resizes image to 80X80 pixels
    img2_tk = ImageTk.PhotoImage(img2)  #Converts to format that Tkinter can display
    Label(retire_win, image=img2_tk).pack()  #Displays the image on the screen
    Label(retire_win, text="Retirement Goals!", font=("Arial", 12)).pack()  #Text label for accessibility 
    retire_win.image = img2_tk  #Keep reference!

    #Inject retirement tools
    retirement.create_retirement_section(retire_win)  #Creates the retirement input section from retirement.py


def open_about_window():  #Opens a secondary window with app information
    """Opens a window with app info."""
    about_win = Toplevel(root)  #Creates a new top-level window
    about_win.title("About This App")  #Sets title
    about_win.geometry("400x250")  #Sets window size (width x height)

    #Adds text content to About window
    Label(about_win, text="Budget & Retirement App", font=("Arial", 16, "bold")).pack(pady=10)
    Label(about_win, text="Created by Christina C. Buchanan", font=("Arial", 12)).pack(pady=5)
    Label(about_win, text="Plan your budget and retirement with ease!  This app helps users manage their day-to-day finances while also planning for their long-term financial goals, particularly retirement.", wraplength=350, justify="center").pack(pady=10)

    #Close button
    Button(about_win, text="Close", command=about_win.destroy, bg="gray", fg="white").pack(pady=20)


def exit_program():  #Function to exit program
    """Safely exits the application."""
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        root.destroy()  #closes the main application window


# --- Main Application Window ---
root = Tk()  #Creates the main GUI application window
root.title("Smart Budget Main Menu")  #Name of the app and display for main menu
root.geometry("400x400")  #Sets window size (width x height)

Label(root, text="Welcome!", font=("Arial", 18, "bold")).pack(pady=10)
Label(root, text="Select a tool to get started:", font=("Arial", 12)).pack(pady=5)

#Buttons for navigation
Button(root, text="Open Budget Calculator", command=open_budget_window, bg="green", fg="white", width=25).pack(pady=10)
Button(root, text="Open Retirement Calculator", command=open_retirement_window, bg="purple", fg="white", width=25).pack(pady=10)
Button(root, text="About", command=open_about_window, bg="blue", fg="white", width=25).pack(pady=10)
Button(root, text="Exit", command=exit_program, bg="red", fg="white", width=25).pack(pady=10)

root.mainloop()  #Runs the GUI application loop
