#!/usr/bin/env python3
"""
Simple Expense Tracker Application
A command-line tool to track and manage your expenses.
"""

from typing import Callable, Dict
from expense_manager import ExpenseManager

# UI Constants
MENU_WIDTH = 50
SEPARATOR = "=" * MENU_WIDTH
TABLE_WIDTH = 80

MENU_OPTIONS = """
{sep}
           EXPENSE TRACKER
{sep}
1. Add new expense
2. View all expenses
3. View total spending
4. View spending by category
5. Exit
{sep}""".format(sep=SEPARATOR)


def display_menu() -> None:
    """Display the main menu options."""
    print(MENU_OPTIONS)


def add_expense_interactive(manager: ExpenseManager) -> None:
    """Interactive prompt to add a new expense."""
    print("\n--- Add New Expense ---")
    try:
        amount_str = input("Enter amount: $")
        amount = float(amount_str)
        category = input("Enter category (e.g., food, transport, entertainment): ").strip()
        description = input("Enter description (optional): ").strip()

        expense = manager.add_expense(amount, category, description)
        print(f"\n✓ Expense added successfully!")
        print(f"  ID: {expense['id']}")
        print(f"  Amount: ${expense['amount']:.2f}")
        print(f"  Category: {expense['category']}")
        print(f"  Date: {expense['date']}")
    except ValueError as e:
        if "could not convert" in str(e).lower() or not amount_str.strip():
            print("\n✗ Error: Invalid amount. Please enter a number.")
        else:
            print(f"\n✗ Error: {e}")


def view_all_expenses(manager: ExpenseManager) -> None:
    """Display all expenses in a formatted table."""
    expenses = manager.view_all_expenses()

    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    print(f"{'ID':<5} {'Date':<20} {'Category':<15} {'Amount':<10} {'Description'}")
    print("-" * TABLE_WIDTH)

    for expense in expenses:
        print(
            f"{expense['id']:<5} "
            f"{expense['date']:<20} "
            f"{expense['category']:<15} "
            f"${expense['amount']:<9.2f} "
            f"{expense['description']}"
        )

    print("-" * TABLE_WIDTH)
    print(f"Total expenses: {len(expenses)}")


def view_total_spending(manager: ExpenseManager) -> None:
    """Display total spending information."""
    total = manager.calculate_total()
    expenses = manager.view_all_expenses()
    count = len(expenses)

    print("\n--- Total Spending Summary ---")
    print(f"Total amount spent: ${total:.2f}")
    print(f"Number of expenses: {count}")

    if count > 0:
        avg = total / count
        print(f"Average expense: ${avg:.2f}")


def view_spending_by_category(manager: ExpenseManager) -> None:
    """Display spending breakdown by category."""
    categories = manager.get_categories()

    if not categories:
        print("\nNo expenses recorded yet.")
        return

    print("\n--- Spending by Category ---")
    print(f"{'Category':<20} {'Amount':<15} {'Percentage'}")
    print("-" * MENU_WIDTH)

    total = manager.calculate_total()
    for category in sorted(categories):
        category_total = manager.calculate_total_by_category(category)
        percentage = (category_total / total * 100) if total > 0 else 0
        print(f"{category:<20} ${category_total:<14.2f} {percentage:.1f}%")

    print("-" * MENU_WIDTH)
    print(f"{'Total':<20} ${total:<14.2f} 100.0%")


def main() -> None:
    """Main application entry point."""
    manager = ExpenseManager()

    # Menu action dispatch table
    actions: Dict[str, Callable[[], None]] = {
        '1': lambda: add_expense_interactive(manager),
        '2': lambda: view_all_expenses(manager),
        '3': lambda: view_total_spending(manager),
        '4': lambda: view_spending_by_category(manager),
    }

    print("\nWelcome to Expense Tracker!")
    print("All data is automatically saved to 'data/expenses.json'")

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == '5':
            print("\nThank you for using Expense Tracker. Goodbye!")
            break

        action = actions.get(choice)
        if action:
            action()
        else:
            print("\n✗ Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
