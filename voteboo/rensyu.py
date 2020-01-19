import sys
from setup import get_description

def start_end_func(func):
    def new_function(*args,**kwargs):
        print("start function:",new_function.__name__)
        result = func(*args,**kwargs)
        print("Result:",result)
        print("end function")
        return result

    return new_function

def add_ints(a,b):
    return a + b

cooler_add_ints = start_end_func(add_ints)

# print("引数:",sys.argv)

print(get_description())