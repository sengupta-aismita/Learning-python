class ChaiOrder:
    def __init__(self, type_, size):
        self.type = type_ #why extra underscore? type is an operator in python
        self.size = size

    def summary(self):
         return f"{self.size} of {self.type} chai"   
    

order = ChaiOrder("Masala", 200)
print(order.summary())

order_two = ChaiOrder("Ginger", 500)
print(order_two.summary())