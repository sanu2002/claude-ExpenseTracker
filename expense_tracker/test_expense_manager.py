"""Tests for the ExpenseManager class."""

import os
import tempfile
import pytest
from expense_manager import ExpenseManager


@pytest.fixture
def temp_data_file():
    """Create a temporary file for testing."""
    fd, path = tempfile.mkstemp(suffix='.json')
    os.close(fd)
    yield path
    if os.path.exists(path):
        os.remove(path)


@pytest.fixture
def manager(temp_data_file):
    """Create an ExpenseManager instance with a temporary data file."""
    return ExpenseManager(data_file=temp_data_file)


class TestExpenseManager:
    """Tests for ExpenseManager class."""

    def test_add_expense(self, manager):
        """Test adding a new expense."""
        expense = manager.add_expense(25.50, "food", "Lunch")

        assert expense["amount"] == 25.50
        assert expense["category"] == "food"
        assert expense["description"] == "Lunch"
        assert expense["id"] == 1
        assert "date" in expense

    def test_add_multiple_expenses(self, manager):
        """Test adding multiple expenses."""
        manager.add_expense(10.00, "food", "Breakfast")
        manager.add_expense(20.00, "transport", "Bus fare")
        manager.add_expense(30.00, "entertainment", "Movie")

        expenses = manager.view_all_expenses()
        assert len(expenses) == 3

    def test_view_all_expenses_empty(self, manager):
        """Test viewing expenses when none exist."""
        expenses = manager.view_all_expenses()
        assert expenses == []

    def test_view_all_expenses(self, manager):
        """Test viewing all expenses."""
        manager.add_expense(25.50, "food", "Lunch")
        manager.add_expense(15.00, "transport", "Taxi")

        expenses = manager.view_all_expenses()
        assert len(expenses) == 2
        assert expenses[0]["category"] == "food"
        assert expenses[1]["category"] == "transport"

    def test_calculate_total_empty(self, manager):
        """Test calculating total with no expenses."""
        total = manager.calculate_total()
        assert total == 0

    def test_calculate_total(self, manager):
        """Test calculating total spending."""
        manager.add_expense(25.50, "food", "Lunch")
        manager.add_expense(15.00, "transport", "Taxi")
        manager.add_expense(50.00, "entertainment", "Concert")

        total = manager.calculate_total()
        assert total == 90.50

    def test_calculate_total_by_category(self, manager):
        """Test calculating total by category."""
        manager.add_expense(25.50, "food", "Lunch")
        manager.add_expense(15.00, "food", "Dinner")
        manager.add_expense(50.00, "entertainment", "Concert")

        food_total = manager.calculate_total_by_category("food")
        assert food_total == 40.50

    def test_calculate_total_by_category_case_insensitive(self, manager):
        """Test that category matching is case insensitive."""
        manager.add_expense(25.50, "Food", "Lunch")
        manager.add_expense(15.00, "FOOD", "Dinner")

        total = manager.calculate_total_by_category("food")
        assert total == 40.50

    def test_calculate_total_by_category_nonexistent(self, manager):
        """Test calculating total for non-existent category."""
        manager.add_expense(25.50, "food", "Lunch")

        total = manager.calculate_total_by_category("transport")
        assert total == 0

    def test_get_categories_empty(self, manager):
        """Test getting categories when none exist."""
        categories = manager.get_categories()
        assert categories == []

    def test_get_categories(self, manager):
        """Test getting unique categories."""
        manager.add_expense(25.50, "food", "Lunch")
        manager.add_expense(15.00, "transport", "Taxi")
        manager.add_expense(10.00, "food", "Snack")

        categories = manager.get_categories()
        assert len(categories) == 2
        assert set(categories) == {"food", "transport"}

    def test_persistence(self, temp_data_file):
        """Test that expenses persist across manager instances."""
        manager1 = ExpenseManager(data_file=temp_data_file)
        manager1.add_expense(25.50, "food", "Lunch")
        manager1.add_expense(15.00, "transport", "Taxi")

        manager2 = ExpenseManager(data_file=temp_data_file)
        expenses = manager2.view_all_expenses()

        assert len(expenses) == 2
        assert expenses[0]["amount"] == 25.50
        assert expenses[1]["amount"] == 15.00

    def test_load_corrupted_file(self, temp_data_file):
        """Test loading from a corrupted JSON file."""
        with open(temp_data_file, 'w') as f:
            f.write("not valid json")

        manager = ExpenseManager(data_file=temp_data_file)
        assert manager.expenses == []

    def test_expense_ids_increment(self, manager):
        """Test that expense IDs increment correctly."""
        e1 = manager.add_expense(10.00, "food", "Item 1")
        e2 = manager.add_expense(20.00, "food", "Item 2")
        e3 = manager.add_expense(30.00, "food", "Item 3")

        assert e1["id"] == 1
        assert e2["id"] == 2
        assert e3["id"] == 3

    def test_add_expense_without_description(self, manager):
        """Test adding expense with empty description."""
        expense = manager.add_expense(25.50, "food")

        assert expense["description"] == ""

    def test_add_expense_negative_amount_raises(self, manager):
        """Test that negative amounts raise ValueError."""
        with pytest.raises(ValueError, match="cannot be negative"):
            manager.add_expense(-10.00, "food", "Invalid")

    def test_add_expense_empty_category_raises(self, manager):
        """Test that empty category raises ValueError."""
        with pytest.raises(ValueError, match="cannot be empty"):
            manager.add_expense(25.50, "", "No category")

    def test_add_expense_whitespace_category_raises(self, manager):
        """Test that whitespace-only category raises ValueError."""
        with pytest.raises(ValueError, match="cannot be empty"):
            manager.add_expense(25.50, "   ", "Whitespace category")

    def test_category_is_trimmed(self, manager):
        """Test that category whitespace is trimmed."""
        expense = manager.add_expense(25.50, "  food  ", "Lunch")
        assert expense["category"] == "food"

    def test_view_all_returns_copy(self, manager):
        """Test that view_all_expenses returns a copy, not the original list."""
        manager.add_expense(25.50, "food", "Lunch")
        expenses = manager.view_all_expenses()
        expenses.clear()
        assert len(manager.view_all_expenses()) == 1
