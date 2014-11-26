import os
import sys
import json

query_dict = {}
url_dict = {}

query_index = {}
url_index = {}

count = {}

file_name = open(sys.argv[1],"r")
lines = file_name.readlines()

output1 = open("mappings.txt","w")
output2 = open("graph.txt","w")
output3 = open("query.txt","w")
output4 = open("url.txt","w")

qi = 0
ui = 0

lines.remove(lines[0])
for line in lines:
    data = line.split()
    if len(data) > 4:
	if not query_dict.has_key( data[1] ):
	    url = []
	    url.append(data[5])
	    query_dict[data[1]] = url
	    query_index[data[1]] = qi
	    qj = qi
	    qi = qi + 1
	else:
	    if data[5] not in query_dict[data[1]]:
		query_dict[data[1]].append( data[5] )
	    qj = query_index[data[1]]
	if not url_dict.has_key( data[5] ):
	    query = []
	    query.append(data[1])
	    url_dict[data[5]] = query
	    url_index[data[5]] = ui
	    uj = ui
	    ui = ui + 1
	else:
	    if data[5] not in query_dict[data[1]]:
		url_dict[data[5]].append( data[1] )
	    uj = url_index[data[5]]
	query_url = ( qj,uj )
	if count.has_key( query_url ):
	    count[query_url] = count[query_url] + 1
	else:
	    count[query_url] = 1

print "Writing query Mappings..."
json.dump(query_dict,output1)
output1.write("\n")
json.dump(url_dict,output1)

print "Building bipartite graph..."
graph = []
for i in range( len(query_index)) :
    temp = []
    for j in range( len(url_index)) :
	temp.append(0)
    graph.append(temp)

print "Adding edges..."

for item in query_dict:
    urls = query_dict[item]
    qi = query_index[item]
    for url in urls:
	ui = url_index[url]
	graph[qi][ui] = count[(qi,ui)]

print "Writing graph to file..."
for query in graph:
    s = ""
    for url in query:
	 s = s + str(url) + " "
    s = s.strip() + "\n" 
    output2.write(s)


query_index = sorted(query_index.items(),key = lambda x:x[1])
url_index = sorted(url_index.items(),key = lambda x:x[1])
print "Writing Query indices..."
for item in query_index:
    output3.write( str(item[1]) + " : " + item[0] + "\n")
print "Writing URL indices..."
for item in url_index:
    output4.write( str(item[1]) + " : " + item[0] + "\n")

output1.close()
output2.close()
output3.close()
output4.close()
