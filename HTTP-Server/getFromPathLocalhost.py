from http.server import HTTPServer,BaseHTTPRequestHandler

class echoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write(self.path[1:].encode())
def main():
    PORT=8000
    server=HTTPServer(('',PORT),echoHandler)
    print("Server Running on PORT 8000\n")
    server.serve_forever()

main()    
