class Budget:
    def __init__(self, limit):
        self.limit = limit

    def check(self, total_spent):
        if total_spent > self.limit:
            print("⚠ Budget exceeded!")
        elif total_spent > 0.75 * self.limit:
            print("⚠ 75% budget used")
