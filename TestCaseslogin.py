from AuthenticationKata import Login
import unittest

class Test_Login_Validations(unittest.TestCase):      
    def test_validate_for_only_letters_present_pass(self):
        result = Login.validate_for_only_letters_present(str("fff"))
        self.assertFalse(result==True)
    
    def test_validate_for_only_letters_present_with_numbers_fail(self):
        result = Login.validate_for_only_letters_present(str("fff112"))
        self.assertFalse(result==True)

    def test_validate_for_minimum_length_of_password_pass(self):
        result = Login.validate_for_minimum_length_of_password("rrtrrrr")
        self.assertFalse(result==True)
    
    def test_validate_for_minimum_length_of_password_fail(self):
        result = Login.validate_for_minimum_length_of_password("rrrr")
        self.assertFalse(result==False)

    def test_validate_for_minimum_one_alphabet_pass(self):
        result = Login.validate_for_minimum_length_of_password("122ddd2222")
        self.assertFalse(result==True)

    def test_validate_for_minimum_one_alphabet_fail(self):
        result = Login.validate_for_minimum_length_of_password("1222222")
        self.assertFalse(result==False)

if __name__ == '__main__':
    unittest.main()
