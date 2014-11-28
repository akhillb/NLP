import os
import re

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
	    samayam = re.search("\d\d\d\d\-\d\d-\d\d \d\d\:\d\d\:\d\d",line)
	    if samayam != None:
		data = samayam.group(0).split()
		time = data[0].split('-')
		if time[2] == date[2] and time[1] == date[1]:
		    clock = data[1].split(":")
		    if int(clock[0]) < 1:
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
