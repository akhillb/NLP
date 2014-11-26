import os
import sys

users = set()
urls = set()
query = set()

name = open(sys.argv[1],"r")
lines = name.readlines()
print "Reading file contents..."
lines.remove(lines[0])
for line in lines:
    data = line.split()
    if data[0] not in users:
	users.add(data[0])
    if data[1] not in query:
	query.add(data[1])
    if len(data) > 4:
	if data[5] not in urls:
	    urls.add(data[5])
print "Statistics:"
print "Unique queries: " + str(len(query))
print "Unique users: " + str(len(users))
print "Unique Click through urls: " + str(len(urls))
