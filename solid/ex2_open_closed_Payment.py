# Here's an example in Python that violates the OCP:


class PaymentProcessor:
    def process_payment(self, amount, payment_method):
        if payment_method == 'credit_card':
            # Code to process credit card payment
            pass
        elif payment_method == 'paypal':
            # Code to process PayPal payment
            pass
        elif payment_method == 'bank_transfer':
            # Code to process bank transfer payment
            pass


# ---------------------------------------------------------------------

from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    def process_payment(self, amount):
        pass


class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        pass


class PayPal(PaymentMethod):
    def process_payment(self, amount):
        pass


class BankTransfer(PaymentMethod):
    def process_payment(self, amount):
        pass


class PaymentProc:
    @classmethod
    def process_payment(cls, amount, payment_method: PaymentMethod):
        return payment_method.process_payment(amount)


credit = CreditCard()


PaymentProc.process_payment(1, credit)
