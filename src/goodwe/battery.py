class Battery:
    
    max_capacity_kwh = 7.2

    def __init__(self, state_of_charge_percent: float):
        self.state_of_charge_percent = state_of_charge_percent

    def get_state_of_charge_kwh(self) -> float:
        return self.max_capacity_kwh / 100.0 * self.state_of_charge_percent

    state_of_charge_kwh = property(get_state_of_charge_kwh, None, None)

