import unittest
from battery import Battery

class TestBattery(unittest.TestCase):

    def test_0_percent(self):
        battery = Battery(0)
        state_kwh = battery.state_of_charge_kwh
        self.assertAlmostEqual(state_kwh, 0.0, 5)

    def test_20_percent(self):
        battery = Battery(20)
        state_kwh = battery.state_of_charge_kwh
        self.assertAlmostEqual(state_kwh, 1.44, 5)

    def test_100_percent(self):
        battery = Battery(100)
        state_kwh = battery.state_of_charge_kwh
        self.assertAlmostEqual(state_kwh, 7.2, 5)

if  __name__ == '__main__':
    unittest.main()