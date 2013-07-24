#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

HOST = 'localhost'                 
# Symbolic name meaning all available interfaces
PORT = 1024  
# Arbitrary non-privileged port

# サーバではsocket(), bind(), listen(), accept()はセット
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

# listen()の引数は接続キューの最大の長さ
s.listen(1)
conn, addr = s.accept()

print 'Connected by', addr
print conn

# 受け取るデータがなくなるまでループ
while 1:
    data = conn.recv(1024)
    if not data: break
    conn.send(data)
conn.close()