import csv
from database import get_expenses


def export_to_csv(filename="expenses.csv"):
    expenses = get_expenses()

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["ID", "Item", "Amount", "Category", "Date"])
        writer.writerows(expenses)

    print(f"Exported {len(expenses)} expenses to {filename}.")


if __name__ == "__main__":
    export_to_csv()
