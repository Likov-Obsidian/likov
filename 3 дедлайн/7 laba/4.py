from abc import ABC, abstractmethod

class PaymentSystem(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    @abstractmethod
    def refund(self, amount):
        pass
class CreditCardPayment(PaymentSystem):
    def pay(self, amount):
        print(f"Оплата картой {amount}")
    def refund(self, amount):
        print(f"Возврат на карту {amount}")
class PayPalPayment(PaymentSystem):
    def pay(self, amount):
        print(f"Оплата через PayPal {amount}")
    
    def refund(self, amount):
        print(f"Возврат через PayPal {amount}")

card = CreditCardPayment()
paypal = PayPalPayment()
card.pay(1000)
paypal.pay(500)
try:
    abstract_payment = PaymentSystem()
except TypeError as e:
    print(f"Ошибка при создании абстрактного класса: {e}")