#!/usr/bin/env python
# -*-coding:utf-8-*-

import socket

# 一个小型服务器

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()  # (client, address)
    print  'Got connection from', addr
    c.send('Thank you for connecting')
    c.close()


