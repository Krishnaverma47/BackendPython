from pymongo import MongoClient
import setting

client = MongoClient(setting.mongodb_uri)

db = client['Attendence']

admin_collection = db['admin_database']
student_collection = db['student_database']
book_collection = db['book_database']