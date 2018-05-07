from random import *
import eval
x = randint(1, 10)
y = randint(1, 10)
op = choice(["+","-", "*","/"])
error = choice([-1, 0, 0, 0, 1])
result = eval.calc(x, y, op)

dis_res = result + error
print(x, op, y, "=", dis_res)
ans = input("enter your answer(Y/N)").upper()
if error == 0:
    if ans == "Y":
        print("Yayyy")
    else:
        print("Occho")
else:
    if ans =="N":
        print("Yayy")
    else: 
        print("Occho")

