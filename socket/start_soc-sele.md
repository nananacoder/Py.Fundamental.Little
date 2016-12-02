##python下的socket的select和eopll的接口开发

select模型目前几乎在所有的平台上支持，其良好跨平台支持也是它的一个优点，事实上从现在看来，这也是它所剩不多的优点之一，现在其实更多的人用epoll，在python下epoll文档有点少，epoll也是包含在import select库内的

select的一个缺点在于单个进程能够监视的文件描述符的数量存在最大限制，在Linux上一般为1024，不过可以通过修改宏定义甚至重新编译内核的方式提升这一限制。



###socket模块

套接字: 两个端点的程序之间的"信息通道"
    
服务器套接字 客户机套接字
   在创建一个服务器套接字后, 让它等待连接.这样它就在某个网络地址处(IP地址和一个端口号的组合)监听,直到有客户端套接字连接.连接完成后,两者就可以进行交互了.

一个套接字就是socket模块中的socket类的一个实例.
    它的实例化需要三个参数:
        (1)地址族(默认是socket.AF_INET)
        (2)流(socket.SOCK_STREAM, 默认值) 或 数据报(socket.SOCK_DGRAM)套接字
        (3)使用的协议(默认是0, 使用默认值即可)
    对于一个普通的套接字, 不需要提供任何参数.
    

###SocketServer

4个基本类: 针对TCP流式套接字的TCPServer; 针对UDP数据报套接字的UDPServer; 针对性不强的UnixStreamServer和UnixDatagramServer

请求处理程序request handler:
    每当服务器收到一个请求时,就会实例化一个请求处理程序,并且它的各种处理方法(handler method)会在处理请求时被调用.具体调用哪个方法取决于特定的服务器呵使用的处理程序类(handler class).
    还可以把它们子类化,使得服务器调用自定义的处理程序集.
    

