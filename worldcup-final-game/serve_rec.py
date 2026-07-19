# -*- coding: utf-8 -*-
"""静态文件 + 录像上传服务器: python serve_rec.py (端口 8321)"""
import http.server, socketserver, os, urllib.parse

os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs('recordings', exist_ok=True)

class H(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        q = urllib.parse.urlparse(self.path)
        if q.path == '/upload':
            name = urllib.parse.parse_qs(q.query).get('name', ['take.webm'])[0]
            name = os.path.basename(name)  # 防目录穿越
            ln = int(self.headers.get('Content-Length', 0))
            data = self.rfile.read(ln)
            with open(os.path.join('recordings', name), 'wb') as f:
                f.write(data)
            body = b'ok'
            self.send_response(200)
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            print('saved recordings/%s (%.1f MB)' % (name, ln / 1e6), flush=True)
        else:
            self.send_response(404)
            self.end_headers()

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(('127.0.0.1', 8321), H) as srv:
    print('serving on http://127.0.0.1:8321', flush=True)
    srv.serve_forever()
