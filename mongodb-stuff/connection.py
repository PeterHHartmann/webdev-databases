from pymongo import MongoClient

CONNECTION_STR = "mongodb://localhost:27017"
DB_NAME = "webdev"

client = MongoClient(CONNECTION_STR)
db = client[DB_NAME]