import unittest

def convert_celsius_to_fahrenheit(celsius:float) -> float : 
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit

class TestTemperatureConversion(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        temperatura = convert_celsius_to_fahrenheit(10.0)
        self.assertEqual(50, temperatura)

if __name__ == '__main__':
    unittest.main()