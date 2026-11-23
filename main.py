from database import create_table, add_expense, get_expenses, get_total


def show_menu():
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total spending")
    print("4. Exit")


def add_new_expense():
    item = input("What did you spend on? ").strip()
    if not item:
        print("Item name cannot be empty.")
        return

    try:
        amount = float(input("Amount (₹): "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    category = input("Category (Food/Travel/Bills/Other): ").strip() or "Other"
    add_expense(item, amount, category)
    print("Expense saved successfully!")


def view_expenses():
    expenses = get_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nID | Item | Amount | Category | Date")
    print("-" * 55)
    for expense_id, item, amount, category, expense_date in expenses:
        print(f"{expense_id} | {item} | ₹{amount:.2f} | {category} | {expense_date}")


def main():
    create_table()

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_new_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print(f"Total spending: ₹{get_total():.2f}")
        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
