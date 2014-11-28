f = open("./data/graph.txt","r")

l = f.readlines()

graph = []
for line in l:
    graph.append(map(int,line.split()))
