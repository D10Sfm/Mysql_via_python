import pymongo
class Connectormongo:
    def __init__(self,client,db,collection):
        self.client = client
        self.db = db
        self.collection = collection
    def connectmongo(self):
        connect = pymongo.MongoClient(str(self.client))
        db = connect[str(self.db)]
        collection = db[str(self.collection)]
        return collection

    def executemongo(self,key="",value=""):
            client = self.connectmongo()
            if len(key) > 1 and len(value) > 1:
                collection = client.find({key:value})
            else:
                collection = client.find({})
            keys = []
            values = []
            for i in  collection:
                keys.append(i.keys())
                values.append(i.values())
            try:
                for (i,j) in zip(keys,values):
                    print(' '.join(map(str,i)),' '.join(map(str,j)))
            except IndexError:
                pass





















# myclient = pymongo.MongoClient(
#     "mongodb://localhost:27017/"
# )
# # db = myclient["Milwaukee-Bucks"]
# # collection = db["Players"]
# db = myclient["Fasil"]
# collection = db["players"]
# new_collection = db["students"]
#
# record = {
#     "name":"Jeremy Mathieu",
#     "age":30,
#     "pos":"LB",
#     "NAT":"France"
# }
# collection.insert_one(record)
# x = collection.find_one()
# y = collection.find({})
# j = collection.find({'name':'Jeremy Mathieu'})
# for player in x.values():
#     print(player)
# for player in x.keys():
#     print(player)
# for player in j[0].values():
#     print(player)
# for (i,s) in zip(x.keys(),x.values()):
#     print(i,":",s)
# for (i,s) in zip(j[0].keys(),j[0].values()):
#     print(i,":",s)
# for (i,s) in zip(y[0].keys(),y[0].values()):
#     print(i,":",s)
# for player in collection.find({'pos':{'$in':['CM','ATM']}}):
#     print(player.items())
# from dictMongo import legends
# new_collection.insert_many(legends)
# player_gt_50 = new_collection.find({'age':{'$gte':50}})
# player_ste_45 = new_collection.find({'age':{'$ste':45}})
# for legend in player_gt_50:
#     print(legend.)
#     print(legend.values())