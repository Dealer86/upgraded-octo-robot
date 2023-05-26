
class Asset:
    def __init__(self, ticker: str, country: str, sector: int = 0):
        self.__ticker = ticker
        self.__country = country
        self.__sector = sector

    @property
    def ticker(self):
        return self.__ticker

    @property
    def country(self):
        return self.__country

    @property
    def sector(self):
        return self.__sector

    def to_dict(self) -> dict:
        return {"ticker": self.ticker, "country": self.country, "sector": self.sector}

    @classmethod
    def from_dict(cls, d: dict):
        return Asset(ticker=d["ticker"], country=d["country"], sector=d["sector"])

