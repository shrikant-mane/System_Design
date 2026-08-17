from abc import ABC, abstractmethod

class Payment:
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Credit card payment: {amount}")

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"UPI payment : {amount}")

class PaypalPayment(Payment):
    def pay(self, amount):
        print(f"PayPal payment : {amount}")


# Basic Factory
class PaymentFactory:

    @staticmethod
    def create_payment(payment_type):

        if payment_type == 'credit_card':
            return CreditCardPayment()

        elif payment_type == 'upi':
            return UPIPayment()

        elif payment_type == 'paypal':
            return PaypalPayment()

        else:
            raise ValueError("Unsupported payment type")


payment = PaymentFactory().create_payment('upi')
payment.pay(5000)

