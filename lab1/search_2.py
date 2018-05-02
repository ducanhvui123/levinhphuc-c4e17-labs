nums = [3, 4, 5, -99, 78, 4, -99, 3]
x = int(input("Enter an integer:"))
# found = False

# for num in nums:
#     if num == x:
#         print("Found")
#         found = True
#         break
# print("None")
for num in nums:
    if num == x:
        print("Found")
        break
else: 
    print("None")