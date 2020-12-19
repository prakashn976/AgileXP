import unittest
import Calculator

class TestCalculatorFunctions(unittest.TestCase):
    def test_addition_of_two_numbers(self):
        result = Calculator.addTwoNumbers(10,40)
        self.assertEqual(result,50)

    def test_addition_of_two_negative_numbers(self):
        result = Calculator.addTwoNumbers(-3,-6)
        self.assertEqual(result,-9)
    
    def test_subtraction_of_two_numbers(self):
        result = Calculator.subtractTwoNumbers(30,40)
        self.assertEqual(result,-10)
    
    def test_multiplication_of_two_numbers(self):
        result = Calculator.multiplyTwoNumbers(4,4)
        self.assertEqual(result,16)
    
    def test_division_Of_two_numbers(self):
        result = Calculator.divideTwoNumbers(40,10)
        self.assertEqual(result,4)
           
    def test_error_raised_for_division_of_number_by_zero(self):
        with self.assertRaises(ValueError):
           Calculator.divideTwoNumbers(10,0)

if __name__ == '__main__':
    unittest.main()

