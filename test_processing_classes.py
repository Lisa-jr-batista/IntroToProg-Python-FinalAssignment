# ------------------------------------------------------------------------------- #
# Title: Testing Processing Classes in Assignment 08
# # Description: A collection of tests for the processing classes module
# ChangeLog: (Who, When, What)
# LBatista, 12.3.2023, Created Script
# ------------------------------------------------------------------------------- #
import json
from json import JSONDecodeError
import tempfile
import unittest

from data_classes import Employee
from processing_classes import FileProcessor


class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name

    def tearDown(self):
        self.temp_file.close()

    def test_read_employee_data_from_file(self):
        sample_data = [
            {"FirstName": "Bob", "LastName": "Smith", "ReviewDate": "2023-11-30", "ReviewRating": 4},
            {"FirstName": "Lisa", "LastName": "Batista", "ReviewDate": "2023-12-01", "ReviewRating": 5}
        ]
        with open(self.temp_file_name, 'w') as file:
            json.dump(sample_data, file)

        employees = FileProcessor.read_employee_data_from_file(self.temp_file_name, [], Employee)

        self.assertEqual(len(sample_data), len(employees))

        for i in range(len(sample_data)):
            self.assertEqual(sample_data[i]["FirstName"], employees[i].first_name)
            self.assertEqual(sample_data[i]['LastName'], employees[i].last_name)
            self.assertEqual(sample_data[i]['ReviewDate'], employees[i].review_date)
            self.assertEqual(sample_data[i]['ReviewRating'], employees[i].review_rating)

    def test_read_employee_data_from_non_existent_file(self):  # Discovered answer through chatGPT!!
        non_existent_file = "hello world!"  # Replace this with your file name
        # Call the method and check for FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            employees = FileProcessor.read_employee_data_from_file('hello world!', [], Employee)

    def test_read_employee_data_from_file_json_decode_error(self):
        # Writing invalid JSON content into the file
        with open(self.temp_file_name, 'w') as file:
            file.write('hello world!')

        # Now, when you call the function, it should encounter a JSONDecodeError
        with self.assertRaises(JSONDecodeError):
            employees = FileProcessor.read_employee_data_from_file(self.temp_file_name, [], Employee)

    def test_write_employee_data_to_file(self):
        sample_data = [
            Employee('Bob','Smith','2023-11-30',4),
            Employee('Lisa',"Batista",'2023-12-01',5)
        ]

        FileProcessor.write_employee_data_to_file(self.temp_file_name, sample_data)

        with open(self.temp_file_name, 'r') as file:
            file_data = json.load(file)

        self.assertEqual(len(sample_data), len(file_data))

        for i in range(len(sample_data)):
            self.assertEqual(sample_data[i].first_name, file_data[i]['FirstName'])
            self.assertEqual(sample_data[i].last_name, file_data[i]['LastName'])
            self.assertEqual(sample_data[i].review_date, file_data[i]['ReviewDate'])
            self.assertEqual(sample_data[i].review_rating, file_data[i]['ReviewRating'])


if __name__ == '__main__':
    unittest.main()
