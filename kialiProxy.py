import socketserver
import http.server
import urllib.request
import shutil
import io

PORT = 9097
URL = 'http://localhost:20001/'
PROXY_ADDRESS = "localhost:9097"

class MyProxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        url = self.path[1:]
        self.send_response(200)
        self.end_headers()
        if url.startswith('http'):
            shutil.copyfileobj(urllib.request.urlopen(url), self.wfile)
        else:
            shutil.copyfileobj(urllib.request.urlopen(URL+url), self.wfile)


httpd = socketserver.ForkingTCPServer(('', PORT), MyProxy)
print("serving at port", str(PORT))
httpd.serve_forever()
