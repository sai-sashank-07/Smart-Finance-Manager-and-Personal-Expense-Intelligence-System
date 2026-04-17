import json
from sfm.transaction import Transaction


def save_data(transactions, filename="data.json"):
    data = []
    for t in transactions:
        data.append({
            "id": t.id,
            "amount": t.amount,
            "type": t.type,
            "merchant": t.merchant,
            "tags": list(t.tags)
        })

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def load_data(filename="data.json"):
    transactions = []
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            for item in data:
                t = Transaction(
                    item["id"],
                    item["amount"],
                    item["type"],
                    item["merchant"],
                    item.get("tags", [])
                )
                transactions.append(t)
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        print("Warning: data file is corrupted. Starting fresh.")
    return transactions
