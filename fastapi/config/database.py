from pymongo import MongoClient




client = pymongo.MongoClient("mongodb+srv://cuong:1234@shop.rpgea.mongodb.net")
db = client.test1
collection = db["test1"]

data = {"id": 1, "name": "duy", "age": 22}
collection.insert_one(data)

print(db)


