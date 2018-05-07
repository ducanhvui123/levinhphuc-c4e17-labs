x = int(input("enter your number x:"))
op = input("enter your operation(+,-,*,/):")
y = int(input("enter your number y:"))
result = 0
if op == "+" :
    result = x + y
elif op == "-":
    result = x - y
elif op == "*":
    result = x*y
elif op == "/":
    result = x/y

print("{0} {1} {2} = {3}".format(x, op, y, result))