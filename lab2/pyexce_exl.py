import pyexcel
data = [ 
    {
    "name": "huyen",
    "age": 23
    },
    {
    "name": "huyen",
    "age": 23
    },
    {
    "name": "huyen",
    "age": 23
    },
]
pyexcel.save_as(records=data, dest_file_name="test.xlsx")