Expense Tracker CLI

A command-line based expense tracker built in Python with persistent storage, timestamp-based querying, category analytics, and optimized range queries using cumulative sums.

Features

- Add expense/income entries
- Persistent local storage using JSON
- Timestamp-based transaction history
- Binary search optimized time-range queries
- Running cumulative totals for fast analytics
- Category tracking:
  - Needs
  - Wants
  - Investment
  - Income
- Update existing transactions
- Delete transactions
- Corruption handling for invalid storage files
- Input validation for:
  - amount
  - datetime
  - categories

---

Technologies Used

- Python 3
- JSON storage
- "bisect" module for binary search
- "datetime"
- "pprint"

---

How It Works

Each transaction is stored with:

- amount
- description
- category
- cumulative running totals

The project maintains cumulative sums for:

- overall balance
- category totals

This allows fast range queries without recalculating all previous transactions repeatedly.

Example:

- Checking total expenses between two timestamps becomes much faster using prefix-sum style cumulative tracking.

---

Why I Built This

I started this project to practice:

- data structures
- file handling
- optimization
- state consistency
- software design

The project gradually evolved from a simple expense logger into a small analytics-oriented tracking system.

---

Running the Project

Clone the repository:

git clone <your-repo-link>
cd <repo-name>

Run:

python main.py

---

Future Improvements

Planned upgrades:

- SQLite database integration
- Graphical charts
- Monthly/yearly analytics
- Better CLI formatting
- CSV export
- UI frontend
- Multi-user support

---

Optimizations Used

Binary Search

Timestamps are stored in sorted order and queried using Python's "bisect" module.

Cumulative Sums

Each entry stores running totals to allow efficient range sum queries.

Tradeoff:

- Very fast reads
- More expensive historical updates/deletes

This design was chosen because finance systems are usually read-heavy.

---

Project Status

Currently functional as a local CLI-based finance tracker.

Still under active development and improvement.
