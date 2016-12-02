#!/usr/bin/env python
# -*-coding:utf-8-*-

# 一个基于SocketServer的小型服务器
# 与14-2.py中客户机协同工作
# StreamRequestHandler在连接被处理完后负责关闭连接.


from SocketServer import TCPServer, StreamRequestHandler

class Handler(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()
        print 'Got connection from', addr
        self.wfile.write('Thank you for connecting')

server = TCPServer(('', 1234), Handler) # ''表示的是服务器正在其上运行的机器的主机名.
server.serve_forever()