import pymongo
from pymongo import collection
from setting import *
import time

start_time = time.time()
try:
    myclient = pymongo.MongoClient(f"mongodb+srv://{CONNECT['user']}:{CONNECT['password']}@shop.rpgea.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    print("Connect success")
except NameError:
    print("Connect error: ", NameError)
    exit()

mydatabase = myclient['mydatabase']
collection = mydatabase["customers"]
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]
# insert data
# collection.insert_many(mylist)
# for x in collection.find({},{ "name": 1, "address": 1 }):
#   print(x)

# find regex
# myquery = { "address": { "$regex": "M.*n" } }
# mydoc = collection.find(myquery)
# for x in mydoc:
#     print(x)

# Sort
# mydoc = collection.find().sort("name")
# for x in mydoc:
#     print(x)

# delete
# myquery = { "address": {"$regex": "^O"} }
# collection.delete_many(myquery)
# mydoc = collection.find()
# for x in mydoc:
#     print(x)

# Update
# myquery = { "address": { "$regex": "^S" } }
# newvalues = { "$set": { "name": "Minnie" } }
# x = collection.update_many(myquery, newvalues)
# print(x.modified_count, "documents updated.")
# mydoc = collection.find()
# for x in mydoc:
#     print(x)

# Limit
mydoc = collection.find().limit(5)
for x in mydoc:
    print(x)

print("--- %s ms ---" % (time.time() - start_time))

