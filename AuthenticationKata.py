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

class Validations:
    def validate_for_only_letters_present_in_username(p):
        res = True if next((chr for chr in p if chr.isdigit()), None) else False
        return res 

    def validate_for_minimum_length_of_password(password):
            flag = 0
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

class Registeration(Validations):
    def create_registation(self, username, password):
        validate_letters_in_username=Validations.validate_for_only_letters_present_in_username(username)
        if validate_letters_in_username==True:
            self.credentials[username] = password
            print("UserAccount created successfully")
            return True
        else:
            return False  
        
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