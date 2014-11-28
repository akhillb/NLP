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
    if data[len(data)-1][0:4] == "http":
	link = data[len(data)-1]
	query = ""
	for i in range(1,len(data)-4):
	    query = query + data[i] + " "
	query = query.strip(" ")
	if not query_dict.has_key( query ):
	    url = []
	    url.append(link)
	    query_dict[query] = url
	    query_index[query] = qi
	    print query + " " + str(qi)
	    qj = qi
	    qi = qi + 1
	else:
	    if link not in query_dict[query]:
		query_dict[query].append( link )
	    qj = query_index[query]
	if not url_dict.has_key( link ):
	    q = []
	    q.append(query)
	    url_dict[link] = q
	    url_index[link] = ui
	    print link + " " + str(ui)
	    uj = ui
	    ui = ui + 1
	else:
	    if link not in query_dict[query]:
		url_dict[link].append( query )
	    uj = url_index[link]
	query_url = ( qj,uj )
	if count.has_key( query_url ):
	    count[query_url] = count[query_url] + 1
	else:
	    count[query_url] = 1

print "Writing query Mappings..."
json.dump(query_dict,output1)
output1.write("\n")
json.dump(url_dict,output1)

#graph = []
#for i in range( 0,len(query_index)) :
#    temp = []
#    for j in range( 0,len(url_index)) :
#	temp.append(0)
#    graph.append(temp)
#
#print "Adding edges..."
#
#print count
#for item in query_dict:
#    urls = query_dict[item]
#    qi = query_index[item]
#    for url in urls:
#	ui = url_index[url]
#	graph[qi][ui] = count[(qi,ui)]

#print "Writing graph to file..."
#for query in graph:
#    s = ""
#    for url in query:
#	 s = s + str(url) + " "
#    s = s.strip() + "\n" 
#    output2.write(s)

query_index = sorted(query_index.items(),key = lambda x:x[1])
url_index = sorted(url_index.items(),key = lambda x:x[1])
print "Writing Query indices..."
for item in query_index:
    output3.write( str(item[1]) + " : " + item[0] + "\n")
print "Writing URL indices..."
for item in url_index:
    output4.write( str(item[1]) + " : " + item[0] + "\n")

print "Building bipartite graph..."
for q in query_index:
    s = ""
    for u in url_index:
	h = (q[1],u[1])
	if count.has_key( h ):
	    s = s + str(h[1]) + "," +str(count[h]) + " "
    s = s.strip(" ") + "\n"
    print s
    output2.write(s)
output1.close()
output2.close()
output3.close()
output4.close()
