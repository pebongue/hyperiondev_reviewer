import unittest
from string_calculator import *

class testStringCalculator(unittest.TestCase):
    
    def test_is_valid_exp_true_value(self):
        result = is_valid_expression("9")
        self.assertTrue(result)

        result = is_valid_expression("0.9")
        self.assertTrue(result)

        result = is_valid_expression("-3.4")
        self.assertTrue(result)

        result = is_valid_expression("-7")
        self.assertTrue(result)

        result = is_valid_expression(" -5")
        self.assertTrue(result)
    

    def test_is_valid_exp_true_fac(self):
        result = is_valid_expression("factorial 9")
        self.assertTrue(result)


    def test_is_valid_exp_true_fib(self):
        result = is_valid_expression("fibonacci 13")
        self.assertTrue(result)

    
    def test_is_valid_exp_true_prime(self):
        result = is_valid_expression("prime 11")
        self.assertTrue(result)

    
    def test_is_valid_exp_true_add(self):
        result = is_valid_expression("+ 9 11")
        self.assertTrue(result)

    
    def test_is_valid_exp_true_sub(self):
        result = is_valid_expression("- 9 -23")
        self.assertTrue(result)


    def test_is_valid_exp_true_multi(self):
        result = is_valid_expression("* 9 0 1")
        self.assertTrue(result)

    
    def test_is_valid_exp_true_div(self):
        result = is_valid_expression("/ 9 5")
        self.assertTrue(result)
    
    def test_is_valid_exp_true_long_arith(self):
        result = is_valid_expression("+ 9 10 4")
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
