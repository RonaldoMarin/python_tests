import unittest
from conversao_temperatura import convert_celsius_to_fahrenheit

class TestTemperatureConversion(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        temperatura = convert_celsius_to_fahrenheit(10.0)
        self.assertEqual(50, temperatura)

if __name__ == '__main__':
    unittest.main()