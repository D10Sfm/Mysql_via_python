import pymongo
myclient = pymongo.MongoClient(
    "mongodb://localhost:27017/"
)
# db = myclient["Milwaukee-Bucks"]
# document = db["Players"]
db = myclient["Fasil"]
document = db["players"]

# record = {
#     "name":"Jeremy Mathieu",
#     "age":30,
#     "pos":"LB",
#     "NAT":"France"
# }
x = document.find_one()
y = document.find({})
j = document.find({'name':'Lionel Messi'})
for player in x.values():
    print(player)
for player in x.keys():
    print(player)
for player in j[0].values():
    print(player)
for (i,s) in zip(x.keys(),x.values()):
    print(i,":",s)
for (i,s) in zip(j[0].keys(),j[0].values()):
    print(i,":",s)
for (i,s) in zip(y[0].keys(),y[0].values()):
    print(i,":",s)