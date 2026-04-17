import numpy as np


def analyze(transactions):
    if not transactions:
        print("No data available")
        return

    amounts = np.array([t.amount for t in transactions])
    debit_amounts = np.array([t.amount for t in transactions if t.type == "debit"])
    credit_amounts = np.array([t.amount for t in transactions if t.type == "credit"])

    print("\n--- Analysis ---")
    print("Total Transactions Amount:", np.sum(amounts))
    print("Average Transaction:", np.mean(amounts))
    print("Maximum Transaction:", np.max(amounts))
    print("Total Debit:", np.sum(debit_amounts) if len(debit_amounts) > 0 else 0)
    print("Total Credit:", np.sum(credit_amounts) if len(credit_amounts) > 0 else 0)
