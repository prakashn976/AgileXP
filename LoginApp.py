import re
class login_app:
    def __init__(self):
        self.credintials = {}
    
    def validate_username(self,p):
        res = False if next((chr for chr in p if chr.isdigit()), None) else True
        return res
    
    def validate_for_minimum_length_of_password(self,password):
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

    def register(self, username, password):
        self.credintials[username] = password
        validate_only_letteres_allowed_in_username=login_app.validate_username(self,username)
        
        validate_for_minimum_length_of_password=login_app.validate_for_minimum_length_of_password(self,password)

        if validate_only_letteres_allowed_in_username==True and validate_for_minimum_length_of_password==True:
            print("user creation successful!")
            return True
        else:
            print("user creation failed! Only letters are allowed in username, Minimum password length should be 6, Password should consist of at least 1 alphabet")
            return False

    def check(self, user, pas):
        print(self.credintials )
        if user in self.credintials.keys() and pas == self.credintials[user] :
            print("Login success!")
            return True
        else:
            print('Login failed. Wrong Username or Password')
            return False

    