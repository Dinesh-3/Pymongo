                        # https://pymongo.readthedocs.io/en/stable/tutorial.html

# Prerequisites
import pymongo
from pymongo import MongoClient
import datetime
import pprint

# Making a Connection with MongoClient
client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')

# Getting a Database
db = client.test_database # db = client['test-database'] Same (Database)

# Getting a Collection
collection = db.test_collection # collection = db['test-collection'] Same (create one collection in a database)

# Documents
post = {"author": "Dinesh",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

# Inserting a Document
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)
print( db.list_collection_names())

# Getting a Single Document With find_one()
pprint.pprint(posts.find_one())
pprint.pprint(posts.find_one({"author": "Mike"}))
posts.find_one({"author": "Eliot"}) #Searching an data that is not inserted

# Querying By ObjectId
pprint.pprint(posts.find_one({"_id": post_id}))

# convert the ObjectId from a string 
from bson.objectid import ObjectId

# The web framework gets post_id from the URL and passes it as a string
def get(post_id):
    # Convert from string to ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})

# Bulk Inserts
new_posts = [{"author": "Mike",
               "text": "Another post!",
               "tags": ["bulk", "insert"],
               "date": datetime.datetime(2009, 11, 12, 11, 14)},
              {"author": "Eliot",
               "title": "MongoDB is fun",
               "text": "and pretty easy too!",
               "date": datetime.datetime(2009, 11, 10, 10, 45)}]
result = posts.insert_many(new_posts)
print(result.inserted_ids)

# Querying for More Than One Document
for post in posts.find():
   pprint.pprint(post)

for post in posts.find({"author": "Mike"}):
   pprint.pprint(post)

# Querying for More Than One Document
print(posts.count_documents({})) #to count total
print(posts.count_documents({"author": "Mike"}))
# Range Queries
d = datetime.datetime(2009, 11, 12, 12)
for post in posts.find({"date": {"$lt": d}}).sort("author"):
   pprint.pprint(post)

# Indexing
result = db.profiles.create_index([('user_id', pymongo.ASCENDING)],unique=True)
print(sorted(list(db.profiles.index_information())))

user_profiles = [
     {'user_id': 211, 'name': 'Luke'},
     {'user_id': 212, 'name': 'Ziltoid'}]
result = db.profiles.insert_many(user_profiles)

# The index prevents us from inserting a document whose user_id is already in the collection:
new_profile = {'user_id': 213, 'name': 'Drew'}
duplicate_profile = {'user_id': 212, 'name': 'Tommy'}
result = db.profiles.insert_one(new_profile)  # This is fine.
result = db.profiles.insert_one(duplicate_profile) 
print(result) # Throws error











