import pymongo
class Connectormongo:
    def __init__(self,client,db,document):
        self.client = client
        self.db = db
        self.document = document
    def connectmongo(self):
        connect = pymongo.MongoClient(str(self.client))
        db = connect[str(self.db)]
        document = db[str(self.document)]
        return document
    def executemongo(self,x=""):
        client = self.connectmongo()
        document = client.find({str(x)})
        keys = []
        values = []
        for (i,j) in zip(document[0].keys(),document[0].values()):
            keys.append(i)
            values.append(i)
        return keys,values

# myclient = pymongo.MongoClient(
#     "mongodb://localhost:27017/"
# )
# # db = myclient["Milwaukee-Bucks"]
# # document = db["Players"]
# db = myclient["Fasil"]
# document = db["players"]
# new_document = db["students"]
#
# record = {
#     "name":"Jeremy Mathieu",
#     "age":30,
#     "pos":"LB",
#     "NAT":"France"
# }
# document.insert_one(record)
# x = document.find_one()
# y = document.find({})
# j = document.find({'name':'Jeremy Mathieu'})
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
# for player in document.find({'pos':{'$in':['CM','ATM']}}):
#     print(player.items())
# from dictMongo import legends
# new_document.insert_many(legends)
# player_gt_50 = new_document.find({'age':{'$gte':50}})
# player_ste_45 = new_document.find({'age':{'$ste':45}})
# for legend in player_gt_50:
#     print(legend.)
#     print(legend.values())