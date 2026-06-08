# CLI Expense Tracker

A command-line expense tracker built with Python that allows users to record, view, and filter expenses. Data is stored locally using JSON files.

## Features

- Add new expenses
- Automatically record today's date
- View all saved expenses
- Filter expenses by category
- Persistent JSON storage

## Categories

- Food
- Transport
- Entertainment
- Other

## Project Structure

expense_tracker/
├── main.py
├── expenses.json
├── README.md
└── .gitignore

## Requirements

- Python 3.x

No external libraries are required.

## How to Run

```bash
python main.py
```

## Sample Menu

```text
1. Add Expense
2. View Expenses
3. Filter By Category
4. Exit
```

---

## Data Storage

Expenses are stored in `expenses.json` in the following format:

```json
{
  "date": "2026-06-08",
  "category": "Food",
  "amount": 230,
  "note": "Burger"
}
```

---

## Author

Divyansh