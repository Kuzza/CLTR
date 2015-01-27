import json, SocketServer
from text_handlers import DocumentHandler
from xml import sax

Handler = DocumentHandler()

class StreamHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        sax.parse(self.rfile, Handler)         
        
        
if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = SocketServer.TCPServer((HOST, PORT), StreamHandler)
    server.serve_forever()        