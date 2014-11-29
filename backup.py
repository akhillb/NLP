def update_into_tree(index, data):
    parent = root
    for i in range(index,len(data)):
	child = parent["children"]
	if child.has_key(data[i]):
	    child[data[i]]["count"] = child[data[i]]["count"] + 1
	    if i+1 != len(data):
		child[data[i]]["suggestions"].append(data[i+1])
	else:
	    child[data[i]]={}
	    child[data[i]]["count"]=1
	    child[data[i]]["suggestins"]=[]
	    if i+1 != len(data):
		child[data[i]]["suggestions"].append(data[i+1])
	    child[data[i]]["children"]={}
	parent = child[data[i]] 


