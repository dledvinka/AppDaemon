from hassapi import Hass
from typing import TypedDict

from energy_prices import EnergyPrices

ATTR_OTE_ENERGY_COSTS = "sensor.current_ote_energy_cost"
ATTR_ENERGY_PRODUCTION_TODAY = "sensor.energy_production_today_2"
ATTR_BATTERY_STATE_OF_CHARGE = "sensor.battery_state_of_charge"
ATTR_INVERTER_OPERATION_MODE = "select.inverter_operation_mode"

class EnergyPriceDict(TypedDict):
    hour: str
    priceEurPerMwh: float

def get_hour_with_lowest_energy_price(energy_prices_dict: EnergyPriceDict, from_hour_including: int, to_hour_excluding: int) -> int:
    prices_dict = dict(list(energy_prices_dict.items())[from_hour_including:to_hour_excluding])
    min_price_hour: int = int(min(prices_dict, key=prices_dict.get))
    return min_price_hour

hass = Hass(hassurl="http://192.168.88.44:8123/", token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIzZDVjNTZjOTgyZTg0NjMwOTM4NjdiNTNmNDk3ZTRhMiIsImlhdCI6MTY2MTMxMzMxMiwiZXhwIjoxOTc2NjczMzEyfQ.8xDcSHeGLNM5DDYXF2gHkx8piVrMqO3Q3YwzSuQHwqs")

# hass.listen_state(hass.on_timestamp, "sensor.timestamp")
energy_costs = hass.get_state(ATTR_OTE_ENERGY_COSTS)
energy_production_today = float(hass.get_state(ATTR_ENERGY_PRODUCTION_TODAY).state)
battery_state_of_charge = int(hass.get_state(ATTR_BATTERY_STATE_OF_CHARGE).state)
inverter_operation_mode = hass.get_state(ATTR_INVERTER_OPERATION_MODE).state # ['General mode', 'Off grid mode', 'Backup mode', 'Eco mode']
morning_cheapest_hour = get_hour_with_lowest_energy_price(energy_costs.attributes, 0, 6)
afternoon_cheapest_hour = get_hour_with_lowest_energy_price(energy_costs.attributes, 12, 24)



# print("State " + energy_costs.attributes)

# for key, value in energy_costs.attributes.items():
#     print(key, ' : ', value)

# print("State 0 " + str(energy_costs.attributes["0"]))
# t = list(energy_costs.attributes)[1]
# print("State 0 " + str(list(energy_costs.attributes)[1]))

energy_dict = dict(list(energy_costs.attributes.items())[:24])
print(energy_dict)

min_price_hour: int = int(min(energy_dict, key=energy_dict.get))
print(min_price_hour)

sorted = dict(sorted(energy_dict.items(), key=lambda x:x[1]))
print(sorted)

keys = list(sorted.keys())
print(keys)

res = [eval(i) for i in keys]
print("Modified list is: ", res)

prices = EnergyPrices(energy_dict)
hours = prices.get_hours_ordered_by_price_desc(0,6)
print(hours)

# tt = get_hour_with_lowest_energy_price(energy_dict, 0, 6)
# prices_dict = dict(list(energy_dict.items())[:24])
# min_price = min(prices_dict, key=prices_dict.get)
# min_price_2 = min(prices_dict)


# d2 = dict(energy_costs.attributes[1:25])
# >>> d = {320: 1, 321: 0, 322: 3}
# >>> min(d, key=d.get)

def on_timestamp(self, entity, attribute, old, new, kwargs):
    print("Test " + new)




