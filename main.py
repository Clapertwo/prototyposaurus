import os
import http.server
import socketserver
import urllib.request

EXTERNAL_IP = urllib.request.urlopen('https://ident.me').read().decode('utf8')
DOWNLOADS_PATH = os.path.join(os.path.dirname(__file__), "downloads")
PORT = 6969

if __name__ == "__main__":
    os.chdir(DOWNLOADS_PATH)
    with socketserver.TCPServer(
        ("", PORT), http.server.SimpleHTTPRequestHandler
    ) as httpd:
        print(f"Server started at localhost:{PORT}")
        print(EXTERNAL_IP)
        httpd.serve_forever()
