import unittest
from energy_prices import EnergyPrices, EnergyPriceDict

class TestEnergyPrices(unittest.TestCase):

    prices_dist = {'0': 119.69, '1': 106.93, '2': 89.18, '3': 95.0, '4': 123.73, '5': 130.52, '6': 174.79, 
                   '7': 206.05, '8': 215.15, '9': 209.9, '10': 204.96, '11': 199.33, '12': 200.67, '13': 189.01, '14': 205.25, '15': 212.59, '16': 216.99, '17': 239.99, '18': 240.55, 
                   '19': 217.74, '20': 195.58, '21': 187.0, '22': 179.8, '23': 172.1}

    def test_get_hours_ordered_by_price_desc_morning(self):
        
        prices = EnergyPrices(self.prices_dist)
        hours = prices.get_hours_ordered_by_price_desc(0,6)
        self.assertEqual(hours, [2, 3, 1, 0, 4, 5])

    def test_get_hours_ordered_by_price_desc_day(self):
        
        prices = EnergyPrices(self.prices_dist)
        hours = prices.get_hours_ordered_by_price_desc(7,18)
        self.assertEqual(hours, [13, 11, 12, 10, 14, 7, 9, 15, 8, 16, 17])

if  __name__ == '__main__':
    unittest.main()
