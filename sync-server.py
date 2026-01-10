#!/usr/bin/env python3
import http.server
import json
import time
import ssl
from http import HTTPStatus

class SyncHandler(http.server.BaseHTTPRequestHandler):
    emergency_state = {"active": False, "message": None}
    
    def do_GET(self):
        if self.path == "/api/time":
            # Send precise server time in milliseconds
            response = {
                "timestamp": int(time.time() * 1000),
                "status": "ok"
            }
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
        elif self.path == "/api/emergency":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(self.emergency_state).encode())
        else:
            self.send_response(HTTPStatus.NOT_FOUND)
            self.end_headers()
    
    def do_POST(self):
        if self.path == "/api/emergency":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode()
            data = json.loads(body)
            self.emergency_state = data
            
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"success": True}).encode())
        else:
            self.send_response(HTTPStatus.NOT_FOUND)
            self.end_headers()
    
    def do_OPTIONS(self):
        self.send_response(HTTPStatus.OK)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.end_headers()
    
    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {format % args}")

if __name__ == "__main__":
    server = http.server.HTTPServer(("0.0.0.0", 3000), SyncHandler)
    
    # Enable HTTPS using self-signed certificate
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain("server.crt", "server.key")
    server.socket = context.wrap_socket(server.socket, server_side=True)
    
    print("🔒 Sync Server running on https://0.0.0.0:3000")
    print("Endpoints: /api/time (GET), /api/emergency (GET/POST)")
    print("Press Ctrl+C to stop")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")
