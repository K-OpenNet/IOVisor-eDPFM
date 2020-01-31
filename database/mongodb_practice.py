from pymongo import MongoClient

try:
    conn = MongoClient()
    print('Mongodb connected succesfully\n')
except:
    print('Could not connect to MongoDB')

# database
db = conn.database

#Created or Switched to collection names : db_test

collection = db.db_test

emp_rec1 = {
    'name':'Mr.Geek',
    'eid':24,
    'location':'delhi'
}

emp_rec2 = {
    'name':'Mr.Sharuya',
    'eid':14,
    'location':'delhi'
}

rec_id1 = collection.insert_one(emp_rec1)
rec_id2 = collection.insert_one(emp_rec2)

print('data inserted with records ids', rec_id1, ' ', rec_id2)

# printing the data inserted

cursor = collection.find()
for record in cursor:
    print(record)
