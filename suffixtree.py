import sys

def findNode(seq,tree):
    if len(seq) == 0:
	return tree[0]
    else:
	seq1 = seq[1:]
	pn = findNode(seq1,tree)
	cn = pn.children


class Node:
    suffix = ""
    freq = 0
    children = []

    def __init__(self,suf,count):
	self.suffix = suf
	self.freq = count
	self.children = []

    def addChild(self,obj):
	self.children.append(obj)

f = open(sys.argv[1],"r")
lines = f.readlines()
freq_concepts = set()

Tree = []
root = Node("",0)
Tree.append(root)
for line in lines:
    sequence = tuple(line.split(" "))
    if sequence in freq_concepts:
	continue
    else:
    freq_concepts = freq_concepts | sequence
