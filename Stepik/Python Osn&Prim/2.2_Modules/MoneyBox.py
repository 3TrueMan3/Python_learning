class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.coins = 0

    def can_add(self, v):
        self.v = v
        return v <= self.capacity - self.coins

    def add(self, v):
        self.v = v
        if self.can_add(v):
            self.coins += v
        else:
            print("Копилка не может вместить столько денег :(")


x = MoneyBox(15)
x.add(10)
x.add(12)
print(x.coins)
