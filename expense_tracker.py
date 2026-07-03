import csv
import matplotlib.pyplot as plt

FILE_NAME = "data/expenses.csv"

def show_menu():
    print("\n======================================")
    print("       SMART EXPENSE TRACKER")
    print("======================================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("5. Total Expenses")
    print("6. Category Summary")
    print("7. Monthly Report")
    print("8. Bar Chart")
    print("9. Pie Chart")
    print("10. Expense Statistics")
    print("11. Export Report")
    print("12. Exit")
    print("======================================")


def add_expense():
    date = input("Enter Date (DD-MM-YYYY): ")
    category = input("Enter Category: ")
    description = input("Enter Description: ")
    amount = input("Enter Amount: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("\nExpense added successfully!")


def view_expenses():
    print("\n================ ALL EXPENSES ================\n")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        rows = list(reader)

        if len(rows) <= 1:
            print("No expenses found.")
            return

        header = rows[0]

        print(f"{header[0]:<15}{header[1]:<15}{header[2]:<25}{header[3]:>10}")
        print("-" * 70)

        for row in rows[1:]:
            print(f"{row[0]:<15}{row[1]:<15}{row[2]:<25}{row[3]:>10}")


def search_expense():
    category = input("\nEnter Category to Search: ").strip().lower()

    found = False

    print("\n================ SEARCH RESULTS ================\n")
    print(f"{'Date':<15}{'Category':<15}{'Description':<25}{'Amount':>10}")
    print("-" * 70)

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            if row[1].strip().lower() == category:
                print(f"{row[0]:<15}{row[1]:<15}{row[2]:<25}{row[3]:>10}")
                found = True

    if not found:
        print("No matching expense found.")


def delete_expense():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if len(rows) <= 1:
        print("\nNo expenses to delete.")
        return

    print("\n================ EXPENSE LIST ================\n")
    print(f"{'No':<5}{'Date':<15}{'Category':<15}{'Description':<25}{'Amount':>10}")
    print("-" * 75)

    for i in range(1, len(rows)):
        row = rows[i]
        print(f"{i:<5}{row[0]:<15}{row[1]:<15}{row[2]:<25}{row[3]:>10}")

    try:
        choice = int(input("\nEnter expense number to delete: "))

        if 1 <= choice < len(rows):
            deleted = rows.pop(choice)

            with open(FILE_NAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)

            print(f"\n'{deleted[2]}' deleted successfully!")

        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")
def total_expenses():
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader)  # Skip header

        for row in reader:
            total += float(row[3])

    print("\n======================================")
    print("         TOTAL EXPENSES")
    print("======================================")
    print(f"Total Amount Spent : ₹{total:.2f}")
    print("======================================")
print("1. Add Expense")
print("2. View Expenses")
print("3. Search Expense")
print("4. Delete Expense")
print("5. Total Expenses")
print("6. Category Summary")
print("7. Monthly Report")
print("8. Bar Chart")
print("9. Pie Chart")
print("10. Exit")

def category_summary():
    categories = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader)  # Skip header

        for row in reader:
            category = row[1]
            amount = float(row[3])

            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

    print("\n======================================")
    print("        CATEGORY SUMMARY")
    print("======================================")

    for category, total in categories.items():
        print(f"{category:<20} ₹{total:.2f}")

    print("======================================")   
def monthly_report():
    monthly = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader)  # Skip header

        for row in reader:
            date = row[0]
            amount = float(row[3])

            # Date format: DD-MM-YYYY
            month_year = date[3:]

            if month_year in monthly:
                monthly[month_year] += amount
            else:
                monthly[month_year] = amount

    print("\n======================================")
    print("         MONTHLY REPORT")
    print("======================================")

    for month, total in monthly.items():
        print(f"{month:<15} ₹{total:.2f}")

    print("======================================")
def bar_chart():
    categories = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            category = row[1]
            amount = float(row[3])

            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

    plt.figure(figsize=(8,5))

    plt.bar(categories.keys(), categories.values())

    plt.title("Expenses by Category")

    plt.xlabel("Category")

    plt.ylabel("Amount (₹)")

    plt.grid(axis="y")

    plt.show()
def pie_chart():
    categories = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader)  # Skip header

        for row in reader:
            category = row[1]
            amount = float(row[3])

            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

    plt.figure(figsize=(7,7))

    plt.pie(
        categories.values(),
        labels=categories.keys(),
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Expense Distribution by Category")

    plt.axis("equal")

    plt.show()
def expense_statistics():

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader)  # Skip header

        rows = list(reader)

    if not rows:
        print("No expenses found.")
        return

    highest = max(rows, key=lambda row: float(row[3]))
    lowest = min(rows, key=lambda row: float(row[3]))

    print("\n======================================")
    print("        EXPENSE STATISTICS")
    print("======================================")

    print("\nHighest Expense")
    print("----------------------------")
    print(f"Description : {highest[2]}")
    print(f"Category    : {highest[1]}")
    print(f"Amount      : ₹{float(highest[3]):.2f}")

    print("\nLowest Expense")
    print("----------------------------")
    print(f"Description : {lowest[2]}")
    print(f"Category    : {lowest[1]}")
    print(f"Amount      : ₹{float(lowest[3]):.2f}")

    print("\n======================================")
def export_report():

    total = 0
    categories = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            category = row[1]
            amount = float(row[3])

            total += amount

            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

    with open("reports/summary.txt", "w", encoding="utf-8") as report:

        report.write("SMART EXPENSE TRACKER REPORT\n")
        report.write("=" * 40 + "\n\n")

        report.write(f"Total Expenses : ₹{total:.2f}\n\n")

        report.write("Category Summary\n")
        report.write("-" * 25 + "\n")

        for category, amount in categories.items():
            report.write(f"{category:<20} ₹{amount:.2f}\n")

    print("\n✅ Report exported successfully!")
    print("Saved as: reports/summary.txt")
def main():
    while True:
        show_menu()

        choice = input("Enter your choice (1-12): ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            search_expense()

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            total_expenses()

        elif choice == "6":
            category_summary()

        elif choice == "7":
            monthly_report()

        elif choice == "8":
            bar_chart()

        elif choice == "9":
            pie_chart()

        elif choice == "10":
            expense_statistics()

        elif choice == "11":
            export_report()

        elif choice == "12":
            print("\nThank you for using Smart Expense Tracker!")
            break

        else:
            print("\nInvalid choice! Please enter a number between 1 and 12.")
      

if __name__ == "__main__":
    main()