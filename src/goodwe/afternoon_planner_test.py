import unittest
from battery import Battery
from planner import Planner

class TestPlanner(unittest.TestCase):

    def test_get_afternoon_plan_high_battery_high_estimate(self):
        battery_state = Battery(50.0)
        planner = Planner(battery_state, 30.0)
        
        afternoon_plan = planner.get_afternoon_plan()
        self.assertEqual(afternoon_plan.charge_kwh, 0)
        self.assertEqual(afternoon_plan.heat_water, False)

    def test_get_afternoon_plan_medium_battery_high_estimate(self):
        battery_state = Battery(40.0)
        planner = Planner(battery_state, 30.0)
        
        afternoon_plan = planner.get_afternoon_plan()
        self.assertEqual(afternoon_plan.charge_kwh, 0)
        self.assertEqual(afternoon_plan.heat_water, False)

    def test_get_afternoon_plan_low_battery_high_estimate(self):
        battery_state = Battery(30.0)
        planner = Planner(battery_state, 30.0)
        
        afternoon_plan = planner.get_afternoon_plan()
        self.assertEqual(afternoon_plan.charge_kwh, 0)
        self.assertEqual(afternoon_plan.heat_water, False)

if  __name__ == '__main__':
    unittest.main()
