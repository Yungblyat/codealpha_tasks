import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry  

class Expense:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

expenses = []

categories_list = ["Food", "Transportation", "Utilities", "Entertainment", "Clothing", "Other"]

def add_expense():
    try:
        amount = float(amount_entry.get())
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return
    
    category = category_var.get()  # Get selected category from dropdown menu
    
    try:
        date = date_entry.get_date().strftime("%Y-%m-%d")  # Get selected date from DateEntry widget
    except ValueError:
        messagebox.showerror("Error", "Please select a valid date.")
        return
    
    expenses.append(Expense(amount, category, date))
    status_label.config(text="Expense added successfully!")

def show_summary():
    if not expenses:
        messagebox.showinfo("Information", "No expenses added yet.")
        return
    
    categories = {}
    for expense in expenses:
        if expense.category in categories:
            categories[expense.category].append((expense.amount, expense.date))  # Store amount and date as tuple
        else:
            categories[expense.category] = [(expense.amount, expense.date)]
    
    summary_text = "Expense Summary:\n"
    for category, expenses_list in categories.items():
        category_total = sum(amount for amount, _ in expenses_list)
        summary_text += f"{category}: ${category_total:.2f}\n"
        for amount, date in expenses_list:
            summary_text += f"  - ${amount:.2f} on {date}\n"
    
    summary_label.config(text=summary_text)

# Create Tkinter window
window = tk.Tk()
window.title("Expense Tracker")

# Set window size
window.geometry("400x400")  # Width x Height

# Add Expense Section
amount_label = tk.Label(window, text="Amount:")
amount_label.pack()
amount_entry = tk.Entry(window)
amount_entry.pack()

category_label = tk.Label(window, text="Category:")
category_label.pack()
category_var = tk.StringVar(window)
category_var.set(categories_list[0])  # Set default category
category_menu = tk.OptionMenu(window, category_var, *categories_list)
category_menu.pack()

date_label = tk.Label(window, text="Date:")
date_label.pack()
date_entry = DateEntry(window, date_pattern="yyyy-mm-dd")
date_entry.pack()

add_button = tk.Button(window, text="Add Expense", command=add_expense)
add_button.pack()

status_label = tk.Label(window, text="")
status_label.pack()

# Show Summary Section
summary_button = tk.Button(window, text="Show Summary", command=show_summary)
summary_button.pack()

summary_label = tk.Label(window, text="")
summary_label.pack()

window.mainloop()
