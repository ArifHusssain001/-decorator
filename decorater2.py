def salam_kar(naam):
    print(f"Assalamualaikum, {naam}!")

def muskurahat_decorator(func):
    def wrapper(naam):
        print("😊")  
        func(naam)
        print("😉")
    return wrapper 
 
@muskurahat_decorator
def salam_kar(naam):
    print(f"Assalamualaikum, {naam}!")   

salam_kar("Ammi")      