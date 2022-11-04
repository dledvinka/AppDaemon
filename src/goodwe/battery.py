class Battery:
    
    MAX_CAPACITY_KWH = 7.2
    DEPTH_OF_DISCHARGE = 0.2
    MIN_CAPACITY_KWH = MAX_CAPACITY_KWH * DEPTH_OF_DISCHARGE

    def __init__(self, state_of_charge_percent: float):
        self.state_of_charge_percent = state_of_charge_percent

    def get_state_of_charge_kwh(self) -> float:
        return self.MAX_CAPACITY_KWH / 100.0 * self.state_of_charge_percent

    def get_remaining_charge_kwh(self) -> float:
        return max(self.MAX_CAPACITY_KWH / 100.0 * self.state_of_charge_percent - self.MIN_CAPACITY_KWH, 0.0)

    state_of_charge_kwh = property(get_state_of_charge_kwh, None, None)
    remaining_charge_kwh = property(get_remaining_charge_kwh, None, None)


