import json
import os
from datetime import datetime
from typing import List, Dict


class ExpenseManager:
    """Manages expense tracking operations including adding, viewing, and saving expenses."""

    def __init__(self, data_file: str = "data/expenses.json"):
        """Initialize the ExpenseManager with a data file path."""
        self.data_file = data_file
        self.expenses: List[Dict] = []
        self.load_expenses()

    def add_expense(self, amount: float, category: str, description: str = "") -> Dict:
        """Add a new expense to the tracker.

        Args:
            amount: The expense amount
            category: Category of the expense (e.g., food, transport, entertainment)
            description: Optional description of the expense

        Returns:
            The created expense dictionary
        """
        expense = {
            "id": len(self.expenses) + 1,
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.expenses.append(expense)
        self.save_expenses()
        return expense

    def view_all_expenses(self) -> List[Dict]:
        """View all expenses.

        Returns:
            List of all expense dictionaries
        """
        return self.expenses

    def calculate_total(self) -> float:
        """Calculate total spending across all expenses.

        Returns:
            Total amount spent
        """
        return sum(expense["amount"] for expense in self.expenses)

    def calculate_total_by_category(self, category: str) -> float:
        """Calculate total spending for a specific category.

        Args:
            category: The category to calculate total for

        Returns:
            Total amount spent in the category
        """
        return sum(
            expense["amount"]
            for expense in self.expenses
            if expense["category"].lower() == category.lower()
        )

    def get_categories(self) -> List[str]:
        """Get all unique categories.

        Returns:
            List of unique category names
        """
        return list(set(expense["category"] for expense in self.expenses))

    def save_expenses(self) -> None:
        """Save expenses to the data file."""
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        with open(self.data_file, 'w') as f:
            json.dump(self.expenses, f, indent=2)

    def load_expenses(self) -> None:
        """Load expenses from the data file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    self.expenses = json.load(f)
            except json.JSONDecodeError:
                self.expenses = []
        else:
            self.expenses = []
