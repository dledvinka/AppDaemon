import unittest
import calc
from unittest.mock import patch

class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)

    # def test_monthly_schedule(self):
    #     with patch('employee.requests.get') as mocked_get:
    #         mocked_get.return_value.ok = True
    #         mocked_get.return_value.text = 'Success'
            
    #         schedule = self.emp_1.montly_schedule('May')
    #         mocked_get.assert_called_with('http://company.com/Scahfer/May')
    #         self.assertEqual(schedule, 'Success')

if  __name__ == '__main__':
    unittest.main()
