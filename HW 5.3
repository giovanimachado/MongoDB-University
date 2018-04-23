import pymongo

connection = pymongo.MongoClient()
db = connection.test

result = db.grades.aggregate([
    {"$unwind": "$scores"},
    {"$match":{"scores.type":{"$in": ["homework","exam"]}}},
    {"$group":{"_id":{"class_id":"$class_id", "student_id":"$student_id"}, "average":{"$avg":"$scores.score"}}},
    {"$group":{"_id":"$_id.class_id", "average":{"$avg":"$average"}}},
    {"$sort": {"average":-1}}])

for doc in result:
	print(doc)
