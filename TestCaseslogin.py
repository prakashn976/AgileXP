from AuthenticationKata import Login
from AuthenticationKata import Registeration
from AuthenticationKata import Validations
import unittest

class Test_Login_Validations(unittest.TestCase):      
    #Sprint 1
    def test_validate_for_only_letters_present_in_username_pass(self):
        result = Validations.validate_for_only_letters_present_in_username(str("fff"))
        self.assertFalse(result==True)
    
    def test_validate_for_only_letters_present_in_username_fail(self):
        result = Validations.validate_for_only_letters_present_in_username(str("fff112"))
        self.assertFalse(result==True)

    def test_create_registation_pass(self):
        result = Registeration.create_registation(self,"Prkmouse","Password1")
        self.assertFalse(result==True)

    def test_create_registation_fail(self):
        result = Registeration.create_registation(self,"3Prk12mouse2","Password1")
        self.assertFalse(result==False)
    #---------End------------------
    def test_validate_for_minimum_length_of_password_pass(self):
        result = Validations.validate_for_minimum_length_of_password("rrtrrrr")
        self.assertFalse(result==True)
    
    def test_validate_for_minimum_length_of_password_fail(self):
        result = Validations.validate_for_minimum_length_of_password("rrrr")
        self.assertFalse(result==False)

    def test_validate_for_minimum_one_alphabet_pass(self):
        result = Validations.validate_for_minimum_length_of_password("122ddd2222")
        self.assertFalse(result==True)

    def test_validate_for_minimum_one_alphabet_fail(self):
        result = Validations.validate_for_minimum_length_of_password("1222222")
        self.assertFalse(result==False)

if __name__ == '__main__':
    unittest.main()
