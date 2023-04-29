import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self) -> None:
        self.my_emp = Employee('Maksym', 'Lushchan', 15000)
        self.custom_raise = 7000

    def test_give_default_raise(self):
        self.my_emp.give_raise()
        self.assertEqual(self.my_emp.year_salary, 20000)

    def test_give_custom_raise(self):
        self.my_emp.give_raise(self.custom_raise)
        self.assertEqual(self.my_emp.year_salary, 22000)


if __name__ == '__main__':
    unittest.main()