person = {
    "name": "Quan",
    "age": "22",
    "gender": "undefined",
}
# if "name" in person:
# if "name" in person.keys():  # hai cau nay tuong duong
#     print("Yeah")
#print(person.keys()) # danh sach co tat ca cac key ben trong
print(person.values())
if "Quan" in person.values():
    print("we found him")