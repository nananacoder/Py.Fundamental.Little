#!/usr/bin/env python
# -*-coding:utf-8-*-

#使用了分叉技术(forking)的服务器

from SocketServer import TCPServer, ForkingMixIn, StreamRequestHandler

class Server(ForkingMixIn, TCPServer):
    pass

class Handler(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()
        print 'Got connection from', addr
        self.wfile.write('Thank u for connecting')


server = Server(('', 1234), Handler)
server.serve_forever()
