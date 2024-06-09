class Item:

    item_values = ["Mango", "Apple"] 
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price}"

class Order:

    def __init__(self, items):
        self.items = items

    def __str__(self):
        pass

    def get_total(self):
        total_so_far = 0
        for item in self.items:
            total_so_far += item.price
        return total_so_far


item1 = Item("Mango",100)
item2 = Item("Apple",200)
item3 = Item("Orange",300)


order1 = Order([item1, item2, item3])

print(order1.get_total())




