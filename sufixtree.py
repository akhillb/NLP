import sys

#creating suffix tree as a nexted dictionary list
root = {}
root["children"] = {}
root["count"] = -1

f = open(sys.argv[1],"r")
lines = f.readlines()

def update_into_tree(index, data, root):
    parent = root
    for i in range(index,len(data)):
	child = parent["children"]
	if child.has_key(data[i]):
	    child[data[i]]["count"] = child[data[i]]["count"] + 1
	else:
	    child[data[i]]={}
	    child[data[i]]["count"]=1
	    child[data[i]]["suggestins"]=[]
	    child[data[i]]["children"]={}
	parent = child[data[i]] 


for line in lines:
    data = line.strip().split()
    for i in range(0,len(data)):
	update_into_tree(i,data,root)

print root
