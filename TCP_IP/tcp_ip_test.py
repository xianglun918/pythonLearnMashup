# 导入socket库
import socket
import ssl

# 创建一个socket: (AF_INET6 -> 指定IPv6, SOCK_STREAM指定面向流的TCP)
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 百度连接HTTPS,端口为443,加了一层SSL(Secure Socket Layer)协议

s = ssl.wrap_socket(socket.socket())

# 建立连接,1024以下是Internet标准服务端口
s.connect(('www.baidu.com', 443))
# 发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
# 接收数据
buffer = []
while True:
    # 每次最多接受1k字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
# 关闭连接
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件：
with open('baidu.html', 'wb') as f:
    f.write(html)

    



