from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['blogdb']
blogs = db['blogposts']
users = db['users']