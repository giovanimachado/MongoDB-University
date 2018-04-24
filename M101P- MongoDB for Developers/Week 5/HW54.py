import pymongo

connection = pymongo.MongoClient()
db = connection.test

result = db.zips.aggregate([
	{"$project": { "firstChar": {"$substr" : ["$city",0,1]}, "population": "$pop" }},
	{"$match": { "firstChar": {"$in":["B", "D", "O", "G", "N" , "M" ]}}},
	{"$group": { "_id": "1", "total": { "$sum":"$population" }}}
])

for doc in result:
	print(doc)
