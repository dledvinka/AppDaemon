from energy_prices import EnergyPrices
from battery import Battery

class HourPlan:
    def __init__(self, hour: int, charge_percentage: int, charge_period_minutes: int, heat_water: bool):
        self.hour = hour
        self.charge_percentage = charge_percentage
        self.charge_period_minutes = charge_period_minutes
        self.heat_water = heat_water

class Plan:
    def __init__(self, charge_kwh: float, heat_water: bool):
        self.charge_kwh = charge_kwh
        self.heat_water = heat_water


class Planner:

    MINIMAL_MORNING_CONSUMPTION_KWH = 1.0

    def __init__(self, battery_state: Battery, energy_production_today: float):
        self.battery_state = battery_state
        self.energy_production_today = energy_production_today
    
    def get_morning_plan(self) -> Plan:

        charge_kwh = 0.0
        
        if (self.battery_state.remaining_charge_kwh < self.MINIMAL_MORNING_CONSUMPTION_KWH):
            charge_kwh += self.MINIMAL_MORNING_CONSUMPTION_KWH

        return Plan(charge_kwh, False)

    def get_afternoon_plan(self) -> Plan:
        return Plan(0.0, False)
        