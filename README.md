# Expense Tracker

A simple command-line application to track and manage your personal expenses.

## Features

- Add expenses with amount, category, and description
- View all recorded expenses in a formatted table
- Calculate total spending across all expenses
- View spending breakdown by category with percentages
- Automatic data persistence to JSON file

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Installation

```bash
git clone <repository-url>
cd claude_code_Mastery/expense_tracker
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

The test suite includes 15 tests covering:
- Adding single and multiple expenses
- Viewing expenses
- Calculating totals (overall and by category)
- Category operations
- Data persistence
- Edge cases (empty data, corrupted files)

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

### ExpenseManager Class

| Method | Description |
|--------|-------------|
| `add_expense(amount, category, description)` | Add a new expense |
| `view_all_expenses()` | Return list of all expenses |
| `calculate_total()` | Calculate total spending |
| `calculate_total_by_category(category)` | Calculate total for a category |
| `get_categories()` | Get list of unique categories |

## License

MIT License
