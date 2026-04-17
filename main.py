from sfm.transaction import Transaction
from sfm.budget import Budget
from sfm.storage import save_data, load_data
from sfm.analytics import analyze


def main():
    transactions = load_data("data.json")
    budget = Budget(5000)

    while True:
        print("\n===== SFM-PEIS =====")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Analyze")
        print("4. Save")
        print("5. Add Tag to Transaction")
        print("6. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            try:
                tid = int(input("ID: "))
                amount = float(input("Amount: "))
                t_type = input("Type (credit/debit): ").strip().lower()
                merchant = input("Merchant: ").strip()

                if amount <= 0:
                    raise ValueError("Amount must be greater than 0")
                if t_type not in ["credit", "debit"]:
                    raise ValueError("Type must be credit or debit")
                if any(t.id == tid for t in transactions):
                    raise ValueError("Transaction ID already exists")

                t = Transaction(tid, amount, t_type, merchant)
                transactions.append(t)

                total_spent = sum(x.amount for x in transactions if x.type == "debit")
                budget.check(total_spent)

                print("Transaction added successfully")

            except ValueError as e:
                print("Invalid input:", e)

        elif ch == "2":
            if not transactions:
                print("No transactions found")
            else:
                for t in transactions:
                    t.display()

        elif ch == "3":
            analyze(transactions)

        elif ch == "4":
            save_data(transactions, "data.json")
            print("Data saved successfully")

        elif ch == "5":
            try:
                tid = int(input("Enter Transaction ID: "))
                tag = input("Enter tag: ").strip()

                found = False
                for t in transactions:
                    if t.id == tid:
                        t.add_tag(tag)
                        print("Tag added successfully")
                        found = True
                        break

                if not found:
                    print("Transaction not found")

            except ValueError:
                print("Invalid ID")

        elif ch == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
