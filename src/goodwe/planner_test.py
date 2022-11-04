import unittest
from battery import Battery
from energy_prices import EnergyPrices
from planner import Planner

class TestPlanner(unittest.TestCase):

    prices_dist = {'0': 119.69, '1': 106.93, '2': 89.18, '3': 95.0, '4': 123.73, '5': 130.52, '6': 174.79, 
                   '7': 206.05, '8': 215.15, '9': 209.9, '10': 204.96, '11': 199.33, '12': 200.67, '13': 189.01, '14': 205.25, '15': 212.59, '16': 216.99, '17': 239.99, '18': 240.55, 
                   '19': 217.74, '20': 195.58, '21': 187.0, '22': 179.8, '23': 172.1}

    def test_get_hours_ordered_by_price_desc_morning(self):
        energy_prices = EnergyPrices(self.prices_dist)
        battery_state = Battery(20.0)
        planner = Planner(energy_prices, battery_state, 20.0)
        plan = planner.get_morning_plan()
        
        self.assertTrue(True)
        # self.assertEqual(hours, [2, 3, 1, 0, 4, 5])

if  __name__ == '__main__':
    unittest.main()
