from abc import ABC, abstractmethod

# client
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


#adaptee 1
class Razorpay:
    def make_payment(self, amount):
        print(f"Razorpay: {amount}")

#adaptee 2
class UPI:
    def phone_bill(self, amount):
        print(f"UPI Phone Bill: {amount}")

# adaptor 1
class RazorpayAdaptor(Payment):
    def __init__(self,razorpay):
        self.razorpay = razorpay

    def pay(self, amount):
        self.razorpay.make_payment(amount)


# adaptor 2
class UPIAdaptor(Payment):
    def __init__(self, upi):
        self.upi = upi

    def pay(self, amount):
        self.upi.phone_bill(amount)


razorpay = Razorpay()
upi = UPI()
payment_1 = RazorpayAdaptor(razorpay)
payment_2 = UPIAdaptor(upi)
payment_1.pay(1000)
payment_2.pay(2000)


