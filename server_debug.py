from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from mimetypes import guess_type

host_name = "localhost"
server_port = 8080
index_html = "index.html"
BASE_DIR = Path(__file__).resolve().parent

class WebServerClass(BaseHTTPRequestHandler):
    def do_GET(self):
        self.write_html_code()

    def write_html_code(self):
        path = f"/{index_html}" if self.path == "/" else self.path
        mimetype, _ = guess_type(path)

        self.send_response(200)
        self.send_header("Content-type", mimetype)
        self.end_headers()

        mimetype = mimetype.split("/")
        if mimetype[0] == "image":
            self.load_image(path)
        else:
            self.load_any(path)

    def load_image(self, path):
        with open(f'{BASE_DIR}{path}', "rb") as lines:
            self.wfile.write(lines.read())

    def load_any(self, path):
        with open(f'{BASE_DIR}{path}', "r") as lines:
            self.wfile.write(bytes(lines.read(), "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((host_name, server_port), WebServerClass)
    print(f"Server started http://{host_name}:{server_port}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")