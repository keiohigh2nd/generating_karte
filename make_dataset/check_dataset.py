import json


f = open("make_dataset/sample/json_time_series_patient.json", 'r')
jsonData = json.load(f)

for p in xrange(len(jsonData)):
	print "------------Patient %s------------"%p
	for t in xrange(len(jsonData["%s"%p])):
		print "Time %s"%t
		text = jsonData["%s"%p]["%s"%t]["MDcomments"]
		text = text.split(" ")
		print len(text)
