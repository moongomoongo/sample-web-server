import http.server
import socketserver
import json
from urllib.parse import urlparse, parse_qs
import os

PORT = 8000
HANDLER = None

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        if path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html_content = '''
            <!DOCTYPE html>
            <html>
            <head>
                <title>Sample Web Server</title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 40px; }
                    h1 { color: #333; }
                    .endpoint { background: #f0f0f0; padding: 10px; margin: 10px 0; border-radius: 5px; }
                </style>
            </head>
            <body>
                <h1>Welcome to Sample Python Web Server</h1>
                <p>This is a simple HTTP server built with Python's http.server module.</p>
                <h2>Available Endpoints:</h2>
                <div class="endpoint"><strong>GET /</strong> - This home page</div>
                <div class="endpoint"><strong>GET /api/hello</strong> - Returns a greeting (optional: ?name=YourName)</div>
                <div class="endpoint"><strong>GET /api/info</strong> - Returns server information</div>
                <h2>Examples:</h2>
                <ul>
                    <li><a href="/api/hello">/api/hello</a></li>
                    <li><a href="/api/hello?name=World">/api/hello?name=World</a></li>
                    <li><a href="/api/info">/api/info</a></li>
                </ul>
            </body>
            </html>
            '''
            self.wfile.write(html_content.encode())
        
        elif path == '/api/hello':
            query_params = parse_qs(parsed_path.query)
            name = query_params.get('name', ['Guest'])[0]
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({'message': f'Hello, {name}!'})
            self.wfile.write(response.encode())
        
        elif path == '/api/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({
                'server': 'Sample Python HTTP Server',
                'version': '1.0',
                'port': PORT,
                'status': 'running'
            })
            self.wfile.write(response.encode())
        
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({'error': 'Endpoint not found'})
            self.wfile.write(response.encode())
    
    def log_message(self, format, *args):
        print(f'[{self.log_date_time_string()}] {format % args}')

def start_server():
    with socketserver.TCPServer(('', PORT), RequestHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}/")
        print("Press Ctrl+C to stop the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == '__main__':
    start_server()