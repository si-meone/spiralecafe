import unittest
from calc import Calculator



class MyTestCase(unittest.TestCase):
    def test_adding_one_and_one_is_two(self):
        calc = Calculator()
        result = calc.add(1,1)
        self.assertEqual(2, result)


if __name__ == '__main__':
    unittest.main()
