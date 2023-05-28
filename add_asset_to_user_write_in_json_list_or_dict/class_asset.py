class Asset:
    def __init__(self, ticker: str, price: int, country: str):
        self.__ticker = ticker
        self.__price = price
        self.__country = country

    @property
    def ticker(self):
        return self.__ticker

    @property
    def price(self):
        return self.__price

    @property
    def country(self):
        return self.__country

    def to_dict(self) -> dict:
        return {"ticker": self.ticker, "price": self.price, "country": self.country}

    @classmethod
    def from_dict(cls, d: dict):
        return Asset(ticker=d["ticker"], price=d["price"], country=d["country"])

    def to_tuple(self) -> tuple:
        return self.ticker, self.price, self.country

    @classmethod
    def from_tuple(cls, info: tuple):
        return Asset(ticker=info[0], price=info[1], country=info[2])
