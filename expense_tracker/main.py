#!/usr/bin/env python3
"""
Simple Expense Tracker Application
A command-line tool to track and manage your expenses.
"""

from expense_manager import ExpenseManager


def display_menu():
    """Display the main menu options."""
    print("\n" + "=" * 50)
    print("           EXPENSE TRACKER")
    print("=" * 50)
    print("1. Add new expense")
    print("2. View all expenses")
    print("3. View total spending")
    print("4. View spending by category")
    print("5. Exit")
    print("=" * 50)


def add_expense_interactive(manager: ExpenseManager):
    """Interactive prompt to add a new expense."""
    print("\n--- Add New Expense ---")
    try:
        amount = float(input("Enter amount: $"))
        category = input("Enter category (e.g., food, transport, entertainment): ").strip()
        description = input("Enter description (optional): ").strip()

        expense = manager.add_expense(amount, category, description)
        print(f"\n✓ Expense added successfully!")
        print(f"  ID: {expense['id']}")
        print(f"  Amount: ${expense['amount']:.2f}")
        print(f"  Category: {expense['category']}")
        print(f"  Date: {expense['date']}")
    except ValueError:
        print("\n✗ Error: Invalid amount. Please enter a number.")
    except Exception as e:
        print(f"\n✗ Error adding expense: {e}")


def view_all_expenses(manager: ExpenseManager):
    """Display all expenses in a formatted table."""
    expenses = manager.view_all_expenses()

    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    print(f"{'ID':<5} {'Date':<20} {'Category':<15} {'Amount':<10} {'Description'}")
    print("-" * 80)

    for expense in expenses:
        print(
            f"{expense['id']:<5} "
            f"{expense['date']:<20} "
            f"{expense['category']:<15} "
            f"${expense['amount']:<9.2f} "
            f"{expense['description']}"
        )

    print("-" * 80)
    print(f"Total expenses: {len(expenses)}")


def view_total_spending(manager: ExpenseManager):
    """Display total spending information."""
    total = manager.calculate_total()
    expenses = manager.view_all_expenses()

    print("\n--- Total Spending Summary ---")
    print(f"Total amount spent: ${total:.2f}")
    print(f"Number of expenses: {len(expenses)}")

    if expenses:
        avg = total / len(expenses)
        print(f"Average expense: ${avg:.2f}")


def view_spending_by_category(manager: ExpenseManager):
    """Display spending breakdown by category."""
    categories = manager.get_categories()

    if not categories:
        print("\nNo expenses recorded yet.")
        return

    print("\n--- Spending by Category ---")
    print(f"{'Category':<20} {'Amount':<15} {'Percentage'}")
    print("-" * 50)

    total = manager.calculate_total()
    for category in sorted(categories):
        category_total = manager.calculate_total_by_category(category)
        percentage = (category_total / total * 100) if total > 0 else 0
        print(f"{category:<20} ${category_total:<14.2f} {percentage:.1f}%")

    print("-" * 50)
    print(f"{'Total':<20} ${total:<14.2f} 100.0%")


def main():
    """Main application entry point."""
    manager = ExpenseManager()

    print("\nWelcome to Expense Tracker!")
    print("All data is automatically saved to 'data/expenses.json'")

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == '1':
            add_expense_interactive(manager)
        elif choice == '2':
            view_all_expenses(manager)
        elif choice == '3':
            view_total_spending(manager)
        elif choice == '4':
            view_spending_by_category(manager)
        elif choice == '5':
            print("\nThank you for using Expense Tracker. Goodbye!")
            break
        else:
            print("\n✗ Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
