import pymongo

connection = pymongo.MongoClient()
db = connection.test

result = db.zips.aggregate([
	{"$match":{"$or":[{"state":"NY"},{"state":"CA"}]}},
	{"$group":{"_id":{"city":"$city","state":"$state"}, "total":{"$sum":"$pop"}}},
	{"$match":{"total":{"$gt":25000}}},
	{"$group":{"_id":"1", "media":{"$avg":"$total"}}}])

for doc in result:
	print(doc)
