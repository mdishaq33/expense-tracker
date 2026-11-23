import sqlite3
from datetime import date

DB_NAME = "expenses.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_table():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item TEXT NOT NULL,
                amount REAL NOT NULL CHECK(amount > 0),
                category TEXT NOT NULL,
                expense_date TEXT NOT NULL
            )
        """)


def add_expense(item, amount, category):
    with connect() as conn:
        conn.execute(
            "INSERT INTO expenses (item, amount, category, expense_date) VALUES (?, ?, ?, ?)",
            (item, amount, category, date.today().isoformat())
        )


def get_expenses():
    with connect() as conn:
        return conn.execute(
            "SELECT id, item, amount, category, expense_date FROM expenses ORDER BY id DESC"
        ).fetchall()


def get_total():
    with connect() as conn:
        result = conn.execute("SELECT COALESCE(SUM(amount), 0) FROM expenses").fetchone()
        return result[0]
