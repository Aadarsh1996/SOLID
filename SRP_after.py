'''Here I seperated payment process and for that i created new class to follow SRP which was being violated before'''

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
    def pay_debit(self,security_code):
        print("Debit payment is processing...")
        print(f"Verifying Security code {security_code}")
        self.status = 'paid'
    def pay_credit(self,security_code):
        print("Credit payment is processing...")
        print(f"Verifying Security code {security_code}")
        self.status = 'paid'



order = Order()
order.add_item("Snack",52,2)
order.add_item("cookies",100,3)
order.add_item('Cigerattes',100,2)

print(order.total_price())
pay = PaymentProcessor()
pay.pay_debit(123456)
