# Basic Calculator Program
def addTwoNumbers(x, y):
    return x + y

def subtractTwoNumbers(x, y):
    return x - y

def multiplyTwoNumbers(x, y):
    return x * y

def divideTwoNumbers(x, y):
    if y==0:
        raise ValueError('Cannot divide by Zero')
    else:
        return x / y
