from pymongo import MongoClient
client = MongoClient()

db = client.packetmonitor

collection = db.bpf2

# db.bpf2.find({'time':{'$lt':'20200223012953'})
for post in collection.find({'time':{'$lt':'20200223012953'}}):
    print(post)
