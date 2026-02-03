import json
import os
from datetime import datetime
from typing import List, Dict, TypedDict


class Expense(TypedDict):
    """Type definition for an expense record."""
    id: int
    amount: float
    category: str
    description: str
    date: str


class ExpenseManager:
    """Manages expense tracking operations including adding, viewing, and saving expenses."""

    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

    def __init__(self, data_file: str = "data/expenses.json"):
        """Initialize the ExpenseManager with a data file path."""
        self.data_file = data_file
        self.expenses: List[Expense] = []
        self.load_expenses()

    def add_expense(self, amount: float, category: str, description: str = "") -> Expense:
        """Add a new expense to the tracker.

        Args:
            amount: The expense amount (must be positive)
            category: Category of the expense (e.g., food, transport, entertainment)
            description: Optional description of the expense

        Returns:
            The created expense dictionary

        Raises:
            ValueError: If amount is negative or category is empty
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        if not category or not category.strip():
            raise ValueError("Category cannot be empty")

        expense: Expense = {
            "id": len(self.expenses) + 1,
            "amount": amount,
            "category": category.strip(),
            "description": description,
            "date": datetime.now().strftime(self.DATE_FORMAT)
        }
        self.expenses.append(expense)
        self.save_expenses()
        return expense

    def view_all_expenses(self) -> List[Expense]:
        """View all expenses.

        Returns:
            List of all expense dictionaries
        """
        return self.expenses.copy()

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
        dir_name = os.path.dirname(self.data_file)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.expenses, f, indent=2)

    def load_expenses(self) -> None:
        """Load expenses from the data file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    self.expenses = json.load(f)
            except (json.JSONDecodeError, IOError):
                self.expenses = []
        else:
            self.expenses = []
