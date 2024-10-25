#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import messagebox


class BudgetTracker:
    def __init__(self, master):
        self.master = master
        self.master.title("StellyArrays Budget Tracker")

        # Initialize variables
        self.sources_of_income = []
        self.all_expenses = []
        self.total_income = 0

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # Income section
        tk.Label(self.master, text="Income Name:").grid(row=0, column=0)
        self.income_name_entry = tk.Entry(self.master)
        self.income_name_entry.grid(row=0, column=1)

        tk.Label(self.master, text="Income Amount:").grid(row=1, column=0)
        self.income_amount_entry = tk.Entry(self.master)
        self.income_amount_entry.grid(row=1, column=1)

        tk.Button(self.master, text="Add Income", command=self.add_income).grid(row=2, columnspan=2)

        # Expense section
        tk.Label(self.master, text="Expense Name:").grid(row=3, column=0)
        self.expense_name_entry = tk.Entry(self.master)
        self.expense_name_entry.grid(row=3, column=1)

        tk.Label(self.master, text="Expense Amount:").grid(row=4, column=0)
        self.expense_amount_entry = tk.Entry(self.master)
        self.expense_amount_entry.grid(row=4, column=1)

        tk.Button(self.master, text="Add Expense", command=self.add_expense).grid(row=5, columnspan=2)

        # Delete expense section
        tk.Label(self.master, text="Delete Expense Name:").grid(row=6, column=0)
        self.delete_expense_entry = tk.Entry(self.master)
        self.delete_expense_entry.grid(row=6, column=1)

        tk.Button(self.master, text="Delete Expense", command=self.delete_expense).grid(row=7, columnspan=2)

        # Display section
        self.display_area = tk.Text(self.master, height=10, width=40)
        self.display_area.grid(row=8, columnspan=2)

    def add_income(self):
        income_name = self.income_name_entry.get()
        try:
            income_amount = int(self.income_amount_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for income amount.")
            return

        self.total_income += income_amount
        self.sources_of_income.append({'income_name': income_name, 'income_amount': income_amount})
        self.update_display(f"Added Income: {income_name} - Amount: {income_amount}\nTotal Income: {self.total_income}")

        # Clear entry fields
        self.income_name_entry.delete(0, tk.END)
        self.income_amount_entry.delete(0, tk.END)

    def add_expense(self):
        expense_name = self.expense_name_entry.get()
        try:
            expense_amount = int(self.expense_amount_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for expense amount.")
            return

        if expense_amount > self.total_income:
            messagebox.showerror("Budget Error", "You don't have enough income to cover this expense.")
            return

        self.total_income -= expense_amount
        self.all_expenses.append({'expense_name': expense_name, 'expense_amount': expense_amount})
        self.update_display(
            f"Added Expense: {expense_name} - Amount: {expense_amount}\nRemaining Income: {self.total_income}")

        # Clear entry fields
        self.expense_name_entry.delete(0, tk.END)
        self.expense_amount_entry.delete(0, tk.END)

    def delete_expense(self):
        expense_name = self.delete_expense_entry.get()
        found = False

        for exp in self.all_expenses:
            if exp['expense_name'].lower() == expense_name.lower():
                self.all_expenses.remove(exp)
                self.total_income += exp['expense_amount']
                found = True
                self.update_display(f"Deleted Expense: {expense_name}\nNew Total Income: {self.total_income}")
                break

        if not found:
            messagebox.showerror("Expense Not Found", f"Expense named '{expense_name}' not found.")

        # Clear entry field
        self.delete_expense_entry.delete(0, tk.END)

    def update_display(self, message):
        self.display_area.insert(tk.END, message + "\n")
        self.display_area.see(tk.END)  # Scroll to the end


if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetTracker(root)
    root.mainloop()


