from typing import TypedDict

class EnergyPriceDict(TypedDict):
    hour: str
    priceEurPerMwh: float

class EnergyPrices:
    def __init__(self, energy_prices_dict: EnergyPriceDict):
        self.energy_prices_dict = energy_prices_dict

    def get_hours_ordered_by_price_desc(self, from_hour_including: int, to_hour_excluding: int):
        prices_dict = dict(list(self.energy_prices_dict.items())[from_hour_including:to_hour_excluding])
        sorted_by_values = dict(sorted(prices_dict.items(), key=lambda x:x[1]))
        keys = list(sorted_by_values.keys())
        as_hours = [eval(i) for i in keys]

        return as_hours
