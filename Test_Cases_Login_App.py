from LoginApp import login_app
import unittest

uname = "prakash"
pwd = "Prakash123"

class Test_Login_App(unittest.TestCase):         
    
    def test_user_creation_success(self):
        login_app.__init__(self)
        result=login_app.register(self,uname,pwd)
        self.assertTrue(result)

    def test_user_creation_failure(self):
        login_app.__init__(self)
        uname="prakash123"
        result=login_app.register(self,uname,pwd)
        self.assertTrue(result)
    
    def test_success_login(self):
        login_app.__init__(self)
        result=login_app.register(self,uname,pwd)
        self.assertTrue(result)

        result=login_app.check(self,uname,pwd)
        self.assertTrue(result)

    def test_failure_login(self):
        login_app.__init__(self)
        result=login_app.register(self,uname,pwd)
        self.assertTrue(result)

        result=login_app.check(self,"pk",pwd)
        self.assertTrue(result)
    
    def test_minimum_password_length(self):
        login_app.__init__(self)
        pwd="rrrrr"
        result=login_app.register(self,uname,pwd)
        self.assertTrue(result)

    def test_password_consists_of_one_alphabet(self):
        login_app.__init__(self)
        pwd="1234567"
        result=login_app.register(self,uname,pwd)
        self.assertTrue(result)

    def test_password_consists_of_atleast_one_integer(self):
        login_app.__init__(self)
        pwd="prakash"
        result=login_app.register(self,uname,pwd)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()