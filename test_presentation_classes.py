# ------------------------------------------------------------------------------- #
# Title: Testing Presentation Classes in Assignment 08
# # Description: A collection of tests for the presentation (I/O) classes module
# ChangeLog: (Who, When, What)
# LBatista, 12.4.2023, Created Script
# LBatista, 12.8.2023, Updated Script
# ------------------------------------------------------------------------------- #
import unittest
from unittest.mock import patch
from presentation_classes import IO
from data_classes import Employee


class TestIOProcessor(unittest.TestCase):
    def test_input_menu_choice(self):
        with patch('builtins.input', return_value='3'):
            choice = IO.input_menu_choice()
            self.assertEqual('3', choice)
            print(choice)

    def test_input_employee_data(self):  # testing the input feature for employee data
        with patch("builtins.input", side_effect=['Vic', 'Vu', '2019-04-28', '2']):
            employees = []
            employees = IO.input_employee_data(employee_data=employees, employee_type=Employee)  # Employee type ??
            self.assertEqual(1, len(employees))
            self.assertEqual("Vic", employees[0].first_name)
            self.assertEqual("Vu", employees[0].last_name)
            self.assertEqual("2019-04-28", employees[0].review_date)
            self.assertEqual(2, employees[0].review_rating)


if __name__ == '__main__':
    unittest.main()