import unittest
import city_functions


class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        full_name = city_functions.get_city_country('KyIv', 'ukraine')
        self.assertEqual(full_name, 'Kyiv, Ukraine')

    def test_city_country_population(self):
        full_name = city_functions.get_city_country('new york', 'uSa', 50000000)
        self.assertEqual(full_name, 'New York, Usa - population=50000000')


if __name__ == '__main__':
    unittest.main()
