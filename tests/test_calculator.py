import unittest
from src.calculator import sum, substract, divisor, product


class CalculatorTest(unittest.TestCase):

    def test_sum(self):
        assert sum(2,3) == 5

    def test_substract(self):
        assert substract(15,6) == 9

    def test_division_by_zero(self):
        """Test de división por cero"""
        with self.assertRaises(ZeroDivisionError):
            divisor(10, 0)

    def test_division_negative(self):
        """Test de división con números negativos"""
        self.assertEqual(divisor(-10, 2), -5)
        self.assertEqual(divisor(10, -2), -5)
        self.assertEqual(divisor(-10, -2), 5)      

    def test_product(self):
        assert product(7,7) == 49
        

    def test_negative_numbers_product(self):        
        self.assertEqual(product(-5,-2), 10)