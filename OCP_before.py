''' 1. Before applying Open Closed Principle.
    2. The Open/Closed Principle states that software entities (classes, modules, functions, etc.)
    should be open for extension but closed for modification.
    In other words, you should be able to extend the behavior of a module without modifying its source code.
    This is typically achieved through abstraction and polymorphism.'''


class Order:

    def __init__(self):
        self.items = []
        self.prices = []
        self.quantities = []
        self.status = 'open'

    def add_item(self,name,price,quantity):
        self.items.append(name)
        self.prices.append(price)
        self.quantities.append(quantity)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total = total + self.quantities[i] * self.prices[i]
        return total


class PaymentProcessor:
    def pay_debit(self,order,security_code):
        print("Debit payment is processing...")
        print(f"Verifying Security code {security_code}")
        self.status = 'paid'
    def pay_credit(self,order,security_code):
        print("Credit payment is processing...")
        print(f"Verifying Security code {security_code}")
        self.status = 'paid'



order = Order()
order.add_item("Snack",52,2)
order.add_item("cookies",100,3)
order.add_item('Cigerattes',100,2)

print(order.total_price())
pay = PaymentProcessor()
pay.pay_debit(order,123456)
