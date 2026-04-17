class Transaction:
    def __init__(self, tid, amount, t_type, merchant, tags=None):
        self.id = tid
        self.amount = amount
        self.type = t_type.lower()
        self.merchant = merchant
        self.category = self.categorize()
        self.tags = set(tags) if tags else set()

    def categorize(self):
        m = self.merchant.lower()
        if "swiggy" in m or "zomato" in m:
            return "Food"
        elif "uber" in m or "ola" in m:
            return "Transport"
        elif "amazon" in m:
            return "Shopping"
        else:
            return "Others"

    def add_tag(self, tag):
        self.tags.add(tag)

    def display(self):
        print(
            f"ID: {self.id} | Amount: {self.amount} | Type: {self.type} | "
            f"Category: {self.category} | Merchant: {self.merchant} | "
            f"Tags: {', '.join(self.tags) if self.tags else 'None'}"
        )
