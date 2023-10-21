import os
import unittest
from dataProcessor import read_json_file

class TestDataProcessor(unittest.TestCase):
    def test_read_json_file_success(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        data = read_json_file(file_path)
       
        self.assertEqual(len(data), 1000)  # Ajustar o número esperado de registros
        self.assertEqual(data[0]['name'], 'Jessica Browning')
        self.assertEqual(data[1]['age'], 34)

    def test_read_json_file_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_json_file("non_existent.json")

    def test_read_json_file_invalid_json(self):
        with open("invalid.json", "w") as file:
            file.write("invalid json data")
        with self.assertRaises(ValueError):
            read_json_file("invalid.json")
    
    def test_avgAgeCountry(self, transform_func=None):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        data = read_json_file(file_path)

        if data is not None:
            ages = 0
            quantity = 0
            for item in data:
                if item.get('age') is not None and item.get('country') is not None:
                    age = item['age']
                    if transform_func:
                        age = transform_func(age)
                    ages += age
                    quantity += 1
            avg = ages/quantity

        self.assertEqual(avg, 38.555) 
    
    def transform_to_months(age):
        return age * 12
    
    func = transform_to_months
    
    def test_avgAgeCountryWithTransformFunc(self, transform_func=func):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        data = read_json_file(file_path)

        if data is not None:
            ages = 0
            quantity = 0
            for item in data:
                if item.get('age') is not None and item.get('country') is not None:
                    age = item['age']
                    if transform_func:
                        age = transform_func(age)
                    ages += age
                    quantity += 1
            avg = ages/quantity

        self.assertEqual(avg, 462.66) 
    
if __name__ == '__main__':
    unittest.main()