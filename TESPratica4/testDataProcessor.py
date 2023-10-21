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

        us = []
        uk = []
        ca = []
        au = []
        fr = []
        de = []
        jp = []
        br = []

        if data is not None:
            ages = 0
            quantity = 0
            for item in data:
                if item.get('age') is not None and item.get('country') is not None:
                    country = item['country']
                    age = item['age']
                    if transform_func:
                        age = transform_func(age)
                        
                    if(country == "US"): 
                        us.append(age)
                    if(country == "UK"): 
                        uk.append(age)
                    if(country == "CA"): 
                        ca.append(age)
                    if(country == "AU"): 
                        au.append(age)
                    if(country == "FR"): 
                        fr.append(age)
                    if(country == "DE"): 
                        de.append(age)
                    if(country == "JP"): 
                        jp.append(age)
                    if(country == "BR"): 
                        br.append(age)
                    ages += age
                    quantity += 1
            avg = ages/quantity
            
            br_avg = sum(br)/len(br)
            jp_avg = sum(jp)/len(jp)
            de_avg = sum(de)/len(de)
            fr_avg = sum(fr)/len(fr)
            au_avg = sum(au)/len(au)
            ca_avg = sum(ca)/len(ca)
            uk_avg = sum(uk)/len(uk)
            us_avg = sum(us)/len(us)

        self.assertEqual(avg, 38.555) 
        self.assertEqual(br_avg, 37.31531531531532) 
        self.assertEqual(jp_avg, 38.21739130434783) 
        self.assertEqual(de_avg, 39.3) 
        self.assertEqual(fr_avg, 39.169642857142854) 
        self.assertEqual(au_avg, 38.744680851063826) 
        self.assertEqual(ca_avg, 36.5) 
        self.assertEqual(uk_avg, 39.42553191489362) 
        self.assertEqual(us_avg, 39.42028985507246) 
    
    
    def transform_to_months(age):
        return age * 12
    
    func = transform_to_months
    
    def test_avgAgeCountryWithTransformFunc(self, transform_func=func):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        data = read_json_file(file_path)

        us = []
        uk = []
        ca = []
        au = []
        fr = []
        de = []
        jp = []
        br = []

        if data is not None:
            ages = 0
            quantity = 0
            for item in data:
                if item.get('age') is not None and item.get('country') is not None:
                    country = item['country']
                    age = item['age']
                    if transform_func:
                        age = transform_func(age)
                        
                    if(country == "US"): 
                        us.append(age)
                    if(country == "UK"): 
                        uk.append(age)
                    if(country == "CA"): 
                        ca.append(age)
                    if(country == "AU"): 
                        au.append(age)
                    if(country == "FR"): 
                        fr.append(age)
                    if(country == "DE"): 
                        de.append(age)
                    if(country == "JP"): 
                        jp.append(age)
                    if(country == "BR"): 
                        br.append(age)
                    ages += age
                    quantity += 1
            avg = ages/quantity
            
            br_avg = sum(br)/len(br)
            jp_avg = sum(jp)/len(jp)
            de_avg = sum(de)/len(de)
            fr_avg = sum(fr)/len(fr)
            au_avg = sum(au)/len(au)
            ca_avg = sum(ca)/len(ca)
            uk_avg = sum(uk)/len(uk)
            us_avg = sum(us)/len(us)

        self.assertEqual(avg, 462.66 ) 
        self.assertEqual(br_avg, 447.7837837837838) 
        self.assertEqual(jp_avg, 38.21739130434783* 12) 
        self.assertEqual(de_avg, 471.6) 
        self.assertEqual(fr_avg, 470.0357142857143) 
        self.assertEqual(au_avg, 464.93617021276594) 
        self.assertEqual(ca_avg, 36.5* 12) 
        self.assertEqual(uk_avg, 473.1063829787234) 
        self.assertEqual(us_avg, 473.04347826086956) 
    
if __name__ == '__main__':
    unittest.main()