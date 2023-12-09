# ------------------------------------------------------------------------------- #
# Title: Testing Data Classes in Assignment 08
# # Description: A collection of tests for the data classes module
# ChangeLog: (Who, When, What)
# LBatista, 12.3.2023, Created Script
# ------------------------------------------------------------------------------- #
import unittest
from data_classes import Person, Employee


class TestPerson(unittest.TestCase):

    def test_person_init(self):  # Tests the constructor
        person = Person("John", "Doe")
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Doe")

    def test_person_invalid_name(self):  # test the first and last name validations
        with self.assertRaises(ValueError):
            person = Person("123", "Doe")
        with self.assertRaises(ValueError):
            person = Person("John", "123")

    def test_person_str(self):  # tests the __str__() magic method
        person = Person("John", "Doe")
        self.assertEqual(str(person), "John,Doe")


class TestEmployee(unittest.TestCase):

    def test_employee_init(self):  # Tests the constructor
        employee = Employee("Alice", "Smith", "2023-11-30", 3)
        self.assertEqual(employee.first_name, "Alice")
        self.assertEqual(employee.last_name, "Smith")
        self.assertEqual(employee.review_date, "2023-11-30")
        self.assertEqual(employee.review_rating, 3)

    def test_employee_review_date_format(self):
        with self.assertRaises(ValueError):
            employee = Employee("Lisa", "Robinson", "12/3/23", 5)

    def test_employee_review_rating_type(self):  # Test the review rating validation
        with self.assertRaises(ValueError):
            employee = Employee("Bob", "Johnson", "2022-12-25", "four")
        with self.assertRaises(ValueError):
            employee = Employee("Sue", "Fisher", "2020-03-14", 15)

    def test_employee_str(self):  # Tests the __str__ magic method
        employee = Employee("Eve", "Brown", "2020-03-14", 4)
        self.assertEqual(str(employee), "Eve,Brown,2020-03-14,4")


if __name__ == '__main__':
    unittest.main()