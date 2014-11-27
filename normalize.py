import os
import sys

file_name = open(sys.argv[1],"r")
output = open("normalised.txt","w")
print "Starting normalizing..." 
i = 0
for line in file_name:
    norm_sum = 0
    index = []
    data = line.strip().split()
    length = len(data)
    for i in range(0,length):
	item = int(data[i])
	if item > 0:
	    norm_sum = norm_sum + item * item
	    index.append(i)
    m = len(index)
    norm_sum = pow(norm_sum,0.5)
    for i in range(0,m):
	data[index[i]] = str( float(data[index[i]]) / norm_sum )
    s = ""
    for i in range(0,length):
	s = s + str(data[i]) + " "
    s = s.strip() + "\n"
    output.write(s)
file_name.close()
output.close()
