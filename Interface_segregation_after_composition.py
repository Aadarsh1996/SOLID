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

class SMSAuthorizer:

    def __init__(self):
        self.authorized = False

    def verify_code(self,code):
        print(f"Verifying SMS code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized

class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self,order):
        pass



class PaymentProcessorDebit(PaymentProcessor):
    def __init__(self,security_code,authorizer:SMSAuthorizer):
        self.security_code = security_code
        self.authorizer = authorizer
        self.verified = False

    def pay(self,order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
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

    def __init__(self,email,authorizer:SMSAuthorizer):
        self.email = email
        self.verified = False
        self.authorizer = authorizer

    def pay(self,order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Paypal payment is processing...")
        print(f"Verifying email address  {self.email}")
        self.status = 'paid'



order = Order()
order.add_item("Snack",52,2)
order.add_item("cookies",100,3)
order.add_item('Cigerattes',100,2)

order = Order()
order.add_item("Snack", 52, 2)
order.add_item("cookies", 100, 3)
order.add_item('Cigarettes', 100, 2)

print(order.total_price())

# Initialize the SMSAuthorizer
authorizer = SMSAuthorizer()
# Verify the code
authorizer.verify_code(232323)

# Initialize the PaymentProcessorDebit with the verified authorizer
processor = PaymentProcessorDebit('212121', authorizer)
processor.pay(order)

