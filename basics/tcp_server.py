# -*- coding: utf-8 -*-
"""
    socket.AF_INET ：使用IPv4协议
    socket.SOCK_STREAM ：使用面向流的TCP协议
"""
import socket
import threading
import time

def rcp_accept():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9999))
    s.listen(5) #等待连接的最大数量：
    print('Waiting for connection...')
    while True:
        sock, addr = s.accept()
        t = threading.Thread(target=handle, args=(sock, addr))
        t.start()

def handle(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

if __name__ == '__main__':
    rcp_accept()