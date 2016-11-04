#关于监控文件/文件夹操作的方法


##pyinotify
这是首先想用到的第三方,但是鉴于整个包(分python2/3)也就只有一个Python文件,而且虽然在django中也有被用到,但在代码质量不佳,在google中搜到的帖子却是被骂到不行.
而且,也已不再维护(github最后日期为2015年春,作者也不再在github上活跃).

研读这份代码很是费劲....



##[inotify](https://pypi.python.org/pypi/inotify)
官方说明: An adapter to Linux kernel support for inotify directory-watching.

