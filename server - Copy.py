import htttp.server
import socketserver
import configpaeser
PORT = 8890
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
print ("Server is running at", PORT)
print ("Server is running at", PORT)
httpd.serve.forever()
