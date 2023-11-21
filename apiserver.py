import http.server

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # 设置响应头
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()

        # # 生成小于1MB大小的响应内容
        # response = "A" * (1024 * 100)
        # 生成1MB大小的响应内容
        # response = "A" * (1024 * 340)
        # # 生成大于1MB大小的响应内容
        # response = "A" * (1024 * 1024)
        # # 生成等于2MB大小的响应内容
        response = "A" * (2048 * 1023)
        # # 生成小于2MB大小的响应内容
        # response = "A" * (2048 * 1023)

        # 发送响应内容
        self.wfile.write(response.encode('utf-8'))

if __name__ == "__main__":
    # 启动HTTP服务器
    server_address = ("", 8000)
    httpd = http.server.HTTPServer(server_address, MyHandler)
    print("Server running at http://localhost:8000")
    httpd.serve_forever()
