from pymongo import MongoClient
import pprint

def grap_time(input_str):
    return input_str[-15:-2]

client = MongoClient() # Use default host and port
#default host and port : mongodb://localhost:27017
db = client.packetmonitor
collection = db.bpf2

# grab time from the databases
for value in collection.find():
    print(grap_time(str(value)))
'''
for post in collection.find():
    print(post)
'''
