# Expense Tracker

A simple command-line application to track and manage your personal expenses.

## Features

- Add expenses with amount, category, and description
- View all recorded expenses in a formatted table
- Calculate total spending across all expenses
- View spending breakdown by category with percentages
- Automatic data persistence to JSON file

## Requirements

- Python 3.6+ (3.8+ recommended for full typing support)
- No external dependencies (uses only standard library)

## Installation

```bash
git clone https://github.com/sanu2002/claude-ExpenseTracker.git
cd claude-ExpenseTracker/expense_tracker
```

## Usage

Run the application:

```bash
python main.py
```

### Menu Options

| Option | Description |
|--------|-------------|
| 1 | Add a new expense |
| 2 | View all expenses |
| 3 | View total spending summary |
| 4 | View spending by category |
| 5 | Exit the application |

### Example Session

```
==================================================
           EXPENSE TRACKER
==================================================
1. Add new expense
2. View all expenses
3. View total spending
4. View spending by category
5. Exit
==================================================

Enter your choice (1-5): 1

--- Add New Expense ---
Enter amount: $25.50
Enter category (e.g., food, transport, entertainment): food
Enter description (optional): Lunch at cafe

✓ Expense added successfully!
  ID: 1
  Amount: $25.50
  Category: food
  Date: 2026-02-02 12:30:00
```

## Data Storage

Expenses are automatically saved to `data/expenses.json`. The file is created automatically on first use.

### Expense Format

```json
{
  "id": 1,
  "amount": 25.50,
  "category": "food",
  "description": "Lunch at cafe",
  "date": "2026-02-02 12:30:00"
}
```

## Testing

Run the test suite:

```bash
cd expense_tracker
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install pytest
pytest -v
```

The test suite includes 20 tests covering:
- Adding single and multiple expenses
- Viewing expenses
- Calculating totals (overall and by category)
- Category operations
- Data persistence
- Input validation (negative amounts, empty categories)
- Edge cases (empty data, corrupted files, defensive copying)

## Project Structure

```
expense_tracker/
├── main.py                  # CLI interface and menu system
├── expense_manager.py       # Core expense management logic
├── test_expense_manager.py  # Test suite
├── requirements.txt         # Dependencies (none required)
├── venv/                    # Virtual environment
└── data/
    └── expenses.json        # Stored expense data
```

## API Reference

### Expense Type

Each expense is a dictionary with the following structure:

| Field | Type | Description |
|-------|------|-------------|
| `id` | int | Unique identifier (auto-incremented) |
| `amount` | float | Expense amount (must be non-negative) |
| `category` | str | Category name (trimmed, non-empty) |
| `description` | str | Optional description |
| `date` | str | Timestamp in `YYYY-MM-DD HH:MM:SS` format |

### ExpenseManager Class

| Method | Description |
|--------|-------------|
| `add_expense(amount, category, description="")` | Add a new expense. Raises `ValueError` if amount is negative or category is empty. |
| `view_all_expenses()` | Return a copy of all expenses list |
| `calculate_total()` | Calculate total spending across all expenses |
| `calculate_total_by_category(category)` | Calculate total for a category (case-insensitive) |
| `get_categories()` | Get list of unique category names |

### Input Validation

The `add_expense` method validates input:
- **Amount**: Must be >= 0 (raises `ValueError: Amount cannot be negative`)
- **Category**: Must be non-empty after trimming (raises `ValueError: Category cannot be empty`)

## License

MIT License
