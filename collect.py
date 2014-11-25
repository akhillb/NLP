import os
import sys

users = set()
query = set()
output = open("./new_collection.txt","w")
output.write("AnonId\tQuery\tQueryTime\tItemRank\tClickURL\n")
date = ['2006','03','01']
files = os.listdir("./AOL-user-ct-collection")
for f in files:
    if f[-3:] == "txt" and f != "U500k_README.txt":
	print "Reading " + f + "..." 
	print "Following searches fall within the required timeline"
	a = open("./AOL-user-ct-collection/" +f,"r")
	lines = a.readlines()
	for line in lines:
	    data = line.split()
	    time = data[2].split('-')
	    if time[:2] == date[:2]:
		if int(time[2]) < int(date[2]) + 1:
		    output.write(line)
		    if data[0] not in users:
			users.add( data[0] )
		    if data[1] not in query:
			query.add( data[1] )
		    print line
	a.close()
output.close()
print
print "Statistics:"
print str(len(users)) + " Unique users"
print str(len(query)) + " Unique queries"
