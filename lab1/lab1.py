a =  [3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ]
x = int(input("enter your integer number:"))
# in
if x in a: # in dùng trong list và dictionary
    print("Found in list")
else:
    print("Nothing")
# occurences ( so lan xuat hien)

c = a.count(x)
print(c)