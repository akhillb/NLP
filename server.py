import sys
import SocketServer
import json

sufixtree_file = open(sys.argv[1],'r')
root = json.loads(sufixtree_file.readline())
sufixtree_file.close()

class MyTCPHandler(SocketServer.StreamRequestHandler):
        def handle(self):
	    # self.rfile is a file-like object created by the handler;
	    # we can now use e.g. readline() instead of raw recv() calls
	    self.data = self.rfile.readline().strip()
	    print "{} wrote:".format(self.client_address[0])
	    print self.data
	    self.concepts = self.data.split(' ')	       
	    
	    ret=""
	    parent_prev = root
	    parent = root
	    for concept in self.concepts:
		children = parent["children"] 
		if children.has_key(concept):
		    temp = children[concept]
		    parent_prev = parent
		    parent = temp
	    
	    if len(parent["children"]) > 0:
		items = sorted(parent["children"].items(),key = lambda x:x[1],reverse=True)
		for tup in items:
		    ret+=tup[0]+" "
	    else:
		items = sorted(parent_prev["children"].items(),key = lambda x:x[1],reverse=True)
		for i in range(0,len(items)):
		    if i > 4:
			break
		    ret+=items[i][0]+" "

	    # Likewise, self.wfile is a file-like object used to write back
	    # to the client
	    self.wfile.write(ret)

if __name__ == "__main__":
        HOST, PORT = "localhost", int(sys.argv[2])
	# Create the server, binding to localhost on port 9999
	server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
	# Activate the server; this will keep running until you
	# interrupt the program with Ctrl-C
	server.serve_forever()
