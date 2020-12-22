import re
class Initialization:
    def __init__(self):
        self.credentials = {}

class Login:
    def check(self, user, pas):
        """print(self.credentials)"""
        if user in self.credentials.keys() and pas == self.credentials[user]:
            print("Login success!")
        else:
            print('Wrong Username or Password')

    def validate_for_only_letters_present(p):
        res = True if next((chr for chr in p if chr.isdigit()), None) else False
        return res 

    def validate_for_minimum_length_of_password(password):
            flag = 0
        #while True:   
            if (len(password)<=6): 
                flag = -1
            elif not re.search("[a-z]", password): 
                flag = -1
            elif not re.search("[A-Z]", password): 
                flag = -1
            elif not re.search("[0-9]", password): 
                flag = -1
            else: 
                flag = 0
                print("Valid Password")
                return True 

            if flag ==-1: 
                print("Not a Valid Password")
                return False   

class Register:
    def register(self, username, password):
        self.credentials[username] = password
        print("UserAccount created successfully")

"""
s = Login()
r =  Register()
Stop = False

while Stop == False:
    tasks = (input('What would you like to do? enter [Register], [Login], or [quit]'))
    # Calling functions with that class object
    if tasks == 'Register':
        Name = (input('Please enter username'))
        Password = (input('Please enter password'))
        r.register(Name, Password)

    if tasks == 'Login':
        LoginInfoUser = (input('Please enter Username'))
        LoginInfoPassword = (input('Please enter Password'))
        s.check(LoginInfoUser, LoginInfoPassword)
    if tasks == 'quit':
        print("See you later!")
        Stop = True"""