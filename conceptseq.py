import sys
import re
import datetime
import json

f = open(sys.argv[1],"r")

cluster_data_file = open("clusters.txt","r")
cluster_data_file.readline()
clusters = json.loads(cluster_data_file.readline()) 

mapping_data_file = open("mappings.txt","r")
mapping_data_file.readline()
mapping_data_file.readline()
query_map = json.loads(mapping_data_file.readline())

output = open("conceptseq.txt","w")

lines = f.readlines()
line_no = 1
user_sessions = {}

def parse_date_from_log_line(line):
    t_pat = re.compile(r"\d\d\d\d\-\d\d-\d\d \d\d\:\d\d\:\d\d")
    date_string = t_pat.search(line).group(0)
    format = '%Y-%m-%d %H:%M:%S'
    return datetime.datetime.strptime(date_string, format)

def parse_date(line):
    t_pat = re.compile(r"\d\d\d\d\-\d\d-\d\d \d\d\:\d\d\:\d\d")
    #t_pat = re.compile(r".*\[\s?(\d+/\D+?/.*?)\]")
    date_string = t_pat.search(line).group(0)
    format = '%Y-%m-%d %H:%M:%S'
    return datetime.datetime.strptime(date_string, format).date()

def find_in_cluster(query_no):
    for cluster in clusters:
	if query_no in clusters[cluster]:
	    return cluster
    return -1
	
print "Creating user sessions"
for line in lines:
    if line_no != 1:
	samayam = re.search("\d\d\d\d\-\d\d-\d\d \d\d\:\d\d\:\d\d",line)
	if samayam != None:
	    data = line.strip().split()
	    if query_map.has_key(data[1]):
		if not user_sessions.has_key(data[0]):
		    user_sessions[data[0]]=[]
		user_sessions[data[0]].append(str(query_map[data[1]])+' '+samayam.group(0))
    line_no = line_no + 1

print "Parsing through user sessions "
for user in user_sessions:
    user_sessions[user].sort(key=parse_date_from_log_line)
    concept_seq=""
    prev_concept=-1
    star_date = parse_date(user_sessions[user][0])
    for log in user_sessions[user]:
	new_date = parse_date(log)
	if ((new_date - star_date).total_seconds()/60) < 30:
	    #appending to sequence so far
	    data = log.split(' ')[0]
	    a = find_in_cluster(int(data))
	    if prev_concept != a:
		concept_seq+=" "+str(a)
	    prev_concept = a
	else:
	    #starting new concept sequence
	    output.write(concept_seq+"\n")
	    concept_seq=""
	    star_date = new_date
	    prev_concept = -1
	    data = log.split(' ')[0]
	    a = find_in_cluster(int(data))
	    if prev_concept != a:
		concept_seq+=" "+str(a)
	    prev_concept = a
    output.write(concept_seq+"\n")
	
output.close()
mapping_data_file.close()
cluster_data_file.close()
f.close()
