# Create a class Product with a method get_price() that returns the price of the product
# Implement the Open Closed principle by creating subclasses book and bluray who
# override the get_price() method to calculate the price of their respective products.

class Product:
    def __name__(self, name: str, year: int, type: str = "general"):
        self.name = name
        self.year = year
        self.type = type

    @property
    def get_price(self) -> float:
        if self.type == "general":

            p = 100 / (2024 - self.year)
            if p < 10:
                return 9.99
            else:
                return p + 0.99
        elif self.type == "bluray":
            p = 100 - (20 * (2023 - self.year))
            if p < 20:
                return 19.99
            else:
                return p + 0.99

    @property
    def get_price2(self):
        p = 100 / (2023 - self.year) if self.type == "general" else p = 100 - (20 * (2023 - self.year))
        if p < 20 and self.type == "blueray" or p < 10 and self.type == "general":
            return 19.99 if p > 10 else 9.99
        else:
            return p + 9.99

