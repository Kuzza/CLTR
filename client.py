import socket, time 
HOST, PORT = "localhost", 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

documents = ["divine.xml", "reput.xml", "romeo.xml", "kant.xml"]
sock.connect((HOST, PORT))

# Create a stream of documents:
# we imagine the documents are previously processed as XML files, 
# and they can also contains informations about authors and title,
# in such a way every document has 'author', 'title' and 'body' tags.
import time
t = time.clock()
sock.sendall("<stream>") 
for i in range(1000):
    for doc in documents:
        with open(doc) as f:
            data = f.read()
        sock.sendall(data)        
sock.sendall("</stream>") 

sock.close()
t1 = time.clock()
print t1-t
    