import sys

def centroid( cluster , queries ):
    c = []
    total_dim = len( queries[0] )
    count = len(cluster)
    for i in range(0,total_dim):
	s = 0
	for q in cluster:
	    s = s + queries[q][i]
	s = s / count 
	c.append(s)
    return c

def diameter( cluster, queries ):
    dia = 0
    for q1 in cluster:
	for q2 in cluster:
    return dia

def q_clus_distance( query, cluster, queries, total_dim ):
    centre = centroid( cluster, queries )
    dist = 0
    for i in range(0,total_dim):
	dist = dist + ( query[i] - cluster[i] ) * ( query[i] - cluster[i] )
    dist = pow(dist, 0.5)
    return dis

graph = sys.argv[1]

f = open(graph,"r")
queries = f.readlines()
total_dim = len(queries[0])

dim_array = set()
for i in range(0,total_dim):
    dim_array[i] = set()

clusters = {}
query_num = 0
for query in queries:
    c_set = set()
    for i in range(0,total_dim):
	if query[i] != 0:
	    c_set = set.union(c_set,dim_array[i])
    c = list(c_set)[0]
    min_d = q_clus_distance( query,c,queries,total_dim ) 
    for clus in c_set:
	d = distance(query,clus,queries,total_dim)
	if d < min_d:
	    c = clus
    query_num = query_num + 1
f.close()    
