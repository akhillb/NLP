import os
import sys

file_name = open(sys.argv[1],"r")
output = open("normalised.txt","w")
print "Starting normalizing..." 
i = 0
for line in file_name:
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
file_name.close()
output.close()
