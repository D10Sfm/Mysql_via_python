from ConnectorMongo import Connectormongo

db = Connectormongo("mongodb://localhost:27017/","Fasil","players")
db.executemongo()



























# import pymongo
# # db = Connectormongo("mongodb://localhost:27017/","Fasil","players")
# # db.executemongo()
# client = pymongo.MongoClient(
# "mongodb://localhost:27017/"
# )
# db = client["Fasil"]
# collection = db["students"]
# x = collection.find({"age":{"$gte":45}})
# for i in range
# for legend in x[1].values():
#     print(legend)