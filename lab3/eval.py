from random import *

def calc(x, y, op):
    # x = randint(1, 10)
    # y = randint(1, 10)
    # op = choice(["+", "-", "*", "/"])
    result = 0
    # op = "+"
    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "/":
        result = x/y
    elif op == "*":
        result = x*y
    return result

# print(result)
    
#usage/ call
# calc(3, 7, "-")

#return
# result = calc(1, 2, "+")
# print(result)
print(__name__)
if __name__ == "__main__":
    print("eval.py imported")
