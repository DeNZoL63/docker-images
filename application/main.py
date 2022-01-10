import http.server
import socketserver

PORT = 8000


class SimpleHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        self.send_response(200, 'Simple-Server-Response')
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello!\n')


with socketserver.TCPServer(("", PORT), SimpleHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
