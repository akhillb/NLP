import os
import sys

file_name = open(sys.argv[1],"r")
output = open("normalised.txt","w")
print "Starting normalizing..." 
i = 0
line_no = 1
total_dim = 0
for line in file_name:
    if line_no == 1:
	total_dim = int(line.strip())
	output.write(str(total_dim)+"\n")
    else:
	edges = line.strip().split(" ")
    	norm_sum = 0
    	for edge in edges:
    	    	a = edge.split(",")[1]
    	    	norm_sum = norm_sum + int( a ) * int( a)
    	norm_sum = pow(norm_sum,0.5)
    	s = ""
    	for edge in edges:
    	    a = edge.split(",")
    	    s = s + a[0] + "," + str(float(a[1])/norm_sum) + " "
    	s = s.strip() + "\n"
    	output.write(s)
    line_no = line_no + 1
file_name.close()
output.close()
