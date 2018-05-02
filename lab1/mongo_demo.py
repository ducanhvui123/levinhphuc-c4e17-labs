from pymongo import MongoClient
# connect to database server
uri = "mongodb://master:dkmchau123@ds155699.mlab.com:55699/c4e17"
client = MongoClient(uri)
# get default database
db = client.get_default_database()
# get blog collection
blog = db["blog"]
# Write a new blog
post = {
    'title': "Hôm nay tôi thất tình",
    'content': "tôi ở nhà code"
}
# blog.insert_one(post)

all_posts = blog.find()
for post in all_posts:
    print(post)
