#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket

HOST = 'localhost'    
# The remote host
PORT = 1024
# The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send('Hello, world')
data = s.recv(1024)
s.close()
print 'Received', repr(data)