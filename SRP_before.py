''' 1. Here all the functionalities are defined in one class which violates Single Responsibility Principle.
    2. A class can have only single responsibility'''

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

    def pay(self,payment_type,security_code):
        if payment_type == 'debit':
            print("Debit payment is processing...")
            print(f"Verifying Security code {security_code}")
            self.status = 'paid'
        elif payment_type == 'credit':
            print("Credit payment is processing...")
            print(f"Verifying Security code {security_code}")
            self.status = 'paid'
        else:
            raise Exception(f"Unknown payment type {payment_type}")

order = Order()
order.add_item("Snack",50,2)
order.add_item("cookies",100,3)
order.add_item('Ciggerattes',100,2)

print(order.total_price())
order.pay('debit',12345)
