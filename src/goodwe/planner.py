from energy_prices import EnergyPrices
from battery import Battery

class HourPlan:
    def __init__(self, hour: int, charge_percentage: int, charge_period_minutes: int, heat_water: bool):
        self.hour = hour
        self.charge_percentage = charge_percentage
        self.charge_period_minutes = charge_period_minutes
        self.heat_water = heat_water


class Planner:
    def __init__(self, energy_prices: EnergyPrices, battery_state: Battery, energy_production_today: float):
        self.energy_prices = energy_prices
    
    def get_morning_plan(self) -> list[HourPlan]:
        return [ HourPlan(1, 20, 55, True)]
        