import sys
import json

def centroid( cluster, clusters , queries , total_dim):
    c = {}
    count = len(clusters[cluster])
    for i in range(0,total_dim):
	s = 0
	for q in clusters[cluster]:
	    if queries[q].has_key(i):
		s = s + queries[q][i]
	s = s / count 
	if s != 0:
	    c[i]=s
    return c

#cluster here in this function is a set instead of a index
def diameter( cluster, queries, total_dim):
    dia = 0
    for q1 in cluster:
	for q2 in cluster:
	    dia+=pow(q_distance(queries[q1],queries[q2],queries,total_dim),2)
    dia = dia/len(cluster)
    dia = dia/(len(cluster)-1)
    dia = pow(dia,0.5)
    return dia

#distance between two queries 
#NOTE query is not a index each one is a dictionary 
def q_distance( q1, q2, queries, total_dim):
    dist=0
    for i in q1:
	if q2.has_key(i):
	    dist = dist + (( q1[i] - q2[i] ) * ( q1[i] - q2[i] ))
    dist = pow(dist, 0.5)
    return dist

def q_clus_distance( query, cluster, clusters, queries, total_dim ):
   centre = centroid( cluster, clusters, queries , total_dim)
    dist = q_distance( query, centre, queries, total_dim)
    return dist


queries = []
total_dim = 0
line_no = 1
print "Taking data input..."
for line in sys.stdin:
    if line_no == 1:
	total_dim = int(line.strip())	
    else:
        line = line.strip().split(' ')
        if len(line) != 0:
	    query = {}
	    for pair in line:
    	   	key_val=pair.split(',')
    	   	query[int(key_val[0])]=float(key_val[1])
	    queries.append(query)
    line_no = line_no + 1
print "Data input done... dimension-",total_dim

print "Starting clustering... "
#dimensional array - assists in doing clustering
#		     each entry is a set of cluster indices
dim_array = []
for i in range(0,total_dim):
    dim_array.append(set())

#clusters is a dictionary of clusters each identifed by index
#each entry is a set of query indices
clusters = {}
cluster_num = 0
query_num = 0
D_MAX = 8 

print "Doing clustering... "
#clustering done here
for query in queries:
    #identify cluster with atleast one dimesion matching with present
    c_set = set()
    for i in range(0,total_dim):
	if query.has_key(i):
	    c_set = set.union(c_set,dim_array[i])
    
    #find the cluster that has minimum dist to present query
    if( len(c_set) != 0 ):
	c = list(c_set)[0]
	min_d = q_clus_distance( query,c,clusters,queries,total_dim ) 
	for clus in c_set:
	    d = q_clus_distance(query,clus,clusters,queries,total_dim)
	    if d < min_d:
	        c = clus
    
        #check if cluster diameter remains within limit
        test_c = set()
	temp = set()
	temp.add(query_num)
        test_c = set.union(clusters[c],temp)
        cluster_toappend_to = 0
	dia=diameter( test_c, queries, total_dim)
        if dia <= D_MAX:
	   cluster_toappend_to = c
        else:
	   cluster_num=cluster_num+1
    	   clusters[cluster_num] = set()
    	   cluster_toappend_to = cluster_num
    else:
	#handling null sets 
	cluster_num=cluster_num+1
    	clusters[cluster_num] = set()
    	cluster_toappend_to = cluster_num
    
    temp = set()
    temp.add(query_num)
    clusters[cluster_toappend_to] = set.union(clusters[cluster_toappend_to],temp)
    
    #add the newly formed cluster back into the dimenson array
    for i in range(0,total_dim):
	if query.has_key(i):
	    temp = set()
	    temp.add(cluster_toappend_to)
	    dim_array[i] = set.union(dim_array[i],temp)
    
    query_num = query_num + 1
print "Clusterng done... "
print "Queries processed -",query_num
print "Clusters formed -",cluster_num
print "Creating json dumps... "
#creating data that can be json dumped
json_dim_array = []
for i in range(0,len(dim_array)):
    json_dim_array.append(list(dim_array[i]))

json_clusters = {}
for clusterKey in clusters:
    json_clusters[clusterKey]=list(clusters[clusterKey])

print "Writing into file... "
output1 = open("clusters.txt","w")
json.dump(json_dim_array,output1)
output1.write("\n")
json.dump(json_clusters,output1)
output1.close()
