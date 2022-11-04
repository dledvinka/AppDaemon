import unittest
from battery import Battery
from planner import Planner

class TestMorningPlanner(unittest.TestCase):

    def test_get_morning_plan_high_battery_high_estimate(self):
        battery_state = Battery(50.0)
        planner = Planner(battery_state, 30.0)
        
        morning_plan = planner.get_morning_plan()
        self.assertEqual(morning_plan.charge_kwh, 0)
        self.assertEqual(morning_plan.heat_water, False)

    def test_get_morning_plan_medium_battery_high_estimate(self):
        battery_state = Battery(40.0)
        planner = Planner(battery_state, 30.0)
        
        morning_plan = planner.get_morning_plan()
        self.assertEqual(morning_plan.charge_kwh, 0)
        self.assertEqual(morning_plan.heat_water, False)

    def test_get_morning_plan_low_battery_high_estimate(self):
        battery_state = Battery(30.0)
        planner = Planner(battery_state, 30.0)
        
        morning_plan = planner.get_morning_plan()
        self.assertEqual(morning_plan.charge_kwh, Planner.MINIMAL_MORNING_CONSUMPTION_KWH)
        self.assertEqual(morning_plan.heat_water, False)

if  __name__ == '__main__':
    unittest.main()
