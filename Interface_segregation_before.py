''' ISP suggests that clients should not be forced to depend on interfaces
    they don't use. Instead of creating large interfaces that cater to all
    possible client needs, ISP advocates for smaller, more specific interfaces
    tailored to the requirements of individual clients.
    This prevents the clients from being burdened with unnecessary dependencies.'''

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
