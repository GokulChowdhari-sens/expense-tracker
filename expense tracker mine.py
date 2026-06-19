

import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    category = input("Category: ")
    amount = float(input("Amount: ₹"))
    description = input("Description: ")

    expense = {
        "id": len(expenses) + 1,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully.\n")

def view_expenses(expenses):
    if not expenses:
        print("No expenses found.\n")
        return

    print("\n--- Expense List ---")
    print(
        f"{'ID':<5}{'Date':<20}{'Category':<15}"
        f"{'Amount':<12}{'Description'}"
    )

    for exp in expenses:
        print(
            f"{exp['id']:<5}"
            f"{exp['date']:<20}"
            f"{exp['category']:<15}"
            f"₹{exp['amount']:<10.2f}"
            f"{exp['description']}"
        )

    print()



def delete_expense(expenses):
    view_expenses(expenses)

    try:
        expense_id = int(input("Enter Expense ID to delete: "))

        for exp in expenses:
            if exp["id"] == expense_id:
                expenses.remove(exp)

                for i, e in enumerate(expenses, start=1):
                    e["id"] = i

                save_expenses(expenses)

                print("Expense deleted.\n")
                return

        print("Expense ID not found.\n")

    except ValueError:
        print("Enter a valid number.\n")


def total_spending(expenses):
    total = sum(exp["amount"] for exp in expenses)

    print(f"\nTotal Spending: ₹{total:.2f}\n")



def category_summary(expenses):
    summary = {}

    for exp in expenses:
        category = exp["category"]

        if category in summary:
            summary[category] += exp["amount"]
        else:
            summary[category] = exp["amount"]

    print("\n--- Category Summary ---")

    for category, total in summary.items():
        print(f"{category}: ₹{total:.2f}")

    print()


def search_category(expenses):
    search = input("Enter category: ").lower()

    found = False

    for exp in expenses:
        if exp["category"].lower() == search:
            print(exp)
            found = True

    if not found:
        print("No matching expenses found.\n")



def main():
    expenses = load_expenses()

    while True:
        print("====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. Delete Expense")
        print("3. View Expenses")
        print("4. Show Total Spending")
        print("5. Category Summary (Bonus)")
        print("6. Search by Category (Bonus)")
        print("7. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            delete_expense(expenses)

        elif choice == "3":
            view_expenses(expenses)

        elif choice == "4":
            total_spending(expenses)

        elif choice == "5":
            category_summary(expenses)

        elif choice == "6":
            search_category(expenses)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    main()
