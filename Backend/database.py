from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017")
db = client["devopsdb"]  # Название БД из docker-compose