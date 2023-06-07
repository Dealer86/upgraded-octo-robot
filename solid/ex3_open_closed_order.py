class DiscountCalculator:
    def calculate_discount(self, product, discount_type):
        if discount_type == 'percentage':
            return product.price * 0.2  # Apply 20% discount
        elif discount_type == 'fixed':
            return product.price - 10  # Apply $10 discount
        elif discount_type == 'seasonal':
            return product.price * 0.1  # Apply 10% seasonal discount
#------------------------------------------------------------------------------------------

from abc import ABC, abstractmethod


class DiscountMethod(ABC):
    @abstractmethod
    def get_discount_type(self, product):
        pass


class Percentage(DiscountMethod):
    def get_discount_type(self, product):
        pass


class Fixed(DiscountMethod):
    def get_discount_type(self, product):
        pass


class Seasonal(DiscountMethod):
    def get_discount_type(self, product):
        pass


class DiscountCalc:
    def __init__(self, discount_type: DiscountMethod):
        self.discount_type = discount_type

    def calculate_discount(self, product):
        return self.discount_type.get_discount_type(product)


seasonal = Seasonal()
dicscalc = DiscountCalc(seasonal)

dicscalc.calculate_discount("a")
