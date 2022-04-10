from ConnectorMongo import Connectormongo

db = Connectormongo("mongodb://localhost:27017/","Fasil","players")
db.executemongo()

