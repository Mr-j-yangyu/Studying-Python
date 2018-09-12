# -*- coding: utf-8 -*-
import socket
"""
    socket.AF_INET ：使用IPv4协议
    socket.SOCK_STREAM ：使用面向流的TCP协议
"""
def tcp_send():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    s.connect(('www.sina.com.cn', 80))
    s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')#\r\n 回车功能
    buffer = []
    while True:
        # 每次最多接收1k字节:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break

    byte_str = b''.join(buffer) #得到字节列
    # header, html = buffer.split(b'\r\n\r\n', 1)
    header, html = byte_str.split(b'\r\n\r\n', 1) #分割一次，分别得到字节
    print(html.decode('utf-8'))
    with open('sina.html', 'wb') as f:
        f.write(html)
    s.close()

if __name__ == '__main__':
    tcp_send()
