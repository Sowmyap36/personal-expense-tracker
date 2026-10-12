

import csv
import os

FILE_NAME = "expenses.csv"
FIELDS = ["Date", "Category", "Amount", "Description"]


def add_expense():
    date = input("Enter date (YYYY-MM-DD): ").strip()
    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    file_exists = os.path.exists(FILE_NAME)
    needs_header = (
        not file_exists or os.path.getsize(FILE_NAME) == 0
    )

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)

        if needs_header:
            writer.writeheader()

        writer.writerow({
            "Date": date,
            "Category": category,
            "Amount": f"{amount:.2f}",
            "Description": description
        })

    print("Expense added successfully!")


def read_expenses():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def view_expenses():
    expenses = read_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print("\n--- All Expenses ---")
    for expense in expenses:
        print(
            f"{expense['Date']} | "
            f"{expense['Category']} | "
            f"Rs. {expense['Amount']} | "
            f"{expense['Description']}"
        )


def filter_expenses():
    category = input("Enter category to filter: ").strip().lower()
    expenses = read_expenses()

    matches = [
        expense for expense in expenses
        if expense["Category"].strip().lower() == category
    ]

    if not matches:
        print("No expenses found in this category.")
        return

    for expense in matches:
        print(
            f"{expense['Date']} | "
            f"{expense['Category']} | "
            f"Rs. {expense['Amount']} | "
            f"{expense['Description']}"
        )


def category_summary():
    expenses = read_expenses()

    if not expenses:
        print("No expenses found.")
        return

    totals = {}

    for expense in expenses:
        category = expense["Category"]
        amount = float(expense["Amount"])
        totals[category] = totals.get(category, 0) + amount

    print("\n--- Category Summary ---")
    for category, total in sorted(totals.items()):
        print(f"{category}: Rs. {total:.2f}")

    grand_total = sum(totals.values())
    print(f"Total Expenses: Rs. {grand_total:.2f}")


def main():
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter Expenses by Category")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_expenses()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()
    