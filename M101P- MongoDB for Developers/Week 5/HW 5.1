
import pymongo

connection = pymongo.MongoClient()
db = connection.blog

result = db.posts.aggregate([
  {"$unwind":"$comments"},
  {"$group": {"_id":"$comments.author","count":{"$sum":1}}},
  {"$sort":{"count":-1}},
  {"$project": {"_id":0,"name":"$_id","count": 1}}])

for doc in result:
  print(doc)
