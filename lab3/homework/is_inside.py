def is_inside(x, y):
    if 140 <= x and x <= 240 and 60 <= y and y <= 260:
        print(True)
        return(True)
    else:
        print(False)
        return False

x = int(input("Enter your X: "))
y = int(input("Enter your Y: "))
is_inside(x, y)
