from pymongo import MongoClient
uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
client=MongoClient(uri)
db = client.get_default_database()
posts = db["posts"]
content ={
    "title": "Hôm nay Trần Duy Hưng khuyến mại",
    "author": "Nguyễn Quang Huy - giảng viên Techkids",
    "content": "Thứ 7, CN hàng tuần chỉ cần đến Trần Duy Hưng bạn có cơ hội được giảm giá lên đến 50 phần trăm các dịch vụ khi dùng mã code huydeptraivippro nha",
}
posts.insert_one(content)
