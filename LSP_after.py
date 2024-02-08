''' 1. Before applying Liskov's Segregation Principle.
    2. This principle states that objects of a superclass should be replaceable
       with objects of a subclass without affecting the correctness of the program.
       In other words, derived classes must be substitutable for their base classes
       without altering the desirable properties of the program.
    3. If we add a new payment method paypal which requires email in place of security_code.
       We need to initialize security code in the defined classes for payment processor.'''

from abc import ABC,abstractmethod

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

class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self,order):
        pass


class PaymentProcessorDebit(PaymentProcessor):
    def __init__(self,security_code):
        self.security_code = security_code

    def pay(self,order):
        print("Debit payment is processing...")
        print(f"Verifying Security code {self.security_code}")
        self.status = 'paid'

class PaymentProcessorCredit(PaymentProcessor):
    def __init__(self,security_code):
        self.security_code = security_code

    def pay(self,order):
        print("Credit payment is processing...")
        print(f"Verifying Security code {self.security_code}")
        self.status = 'paid'

class PaymentProcessorPaypal(PaymentProcessor):

    def __init__(self,email):
        self.email = email

    def pay(self,order):
        print("Paypal payment is processing...")
        print(f"Verifying email address  {self.email}")
        self.status = 'paid'


order = Order()
order.add_item("Snack",52,2)
order.add_item("cookies",100,3)
order.add_item('Cigerattes',100,2)

print(order.total_price())
processor = PaymentProcessorPaypal('abc@gmail.com')
processor.pay(order)
