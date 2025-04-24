def salam_kar():
    print("Assalamualaikum!!")

def salam_with_smile():
    print("😊")
    salam_kar()
    print("😊") 

salam_with_smile()

def muskurahat_decorator(func):
    def wrapper():
        print("😊")
        func()
        print("😊")
    return wrapper
@muskurahat_decorator
def salam_kar():
    print("Assalamualaikum!!")
def salaam_kar():
    print("Assalamualaikum!")    
 
