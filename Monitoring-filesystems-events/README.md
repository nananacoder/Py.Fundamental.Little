#关于监控文件/文件夹操作的方法


##[pyinotify](https://github.com/seb-m/pyinotify)

这是首先想用到的,但是鉴于整个包(分python2/3)也就只有一个Python文件,而且虽然在django中也有被用到,但在代码质量不佳,在google中搜到的帖子却是被骂到不行.
而且,也已不再维护(github最后日期为2015年春,作者也不再在github上活跃).

虽然代码晦涩冗长,但仍有借鉴意义.

### 依赖

* Linux ≥ 2.6.13
* Python ≥ 2.4 (including Python 3.x)


==========
Installing
==========

Install via *pip*::

    # To install pip follow http://www.pip-installer.org/en/latest/installing.html
    $ sudo pip install pyinotify
    

==============================
common usage:Watch a directory
==============================

Install pyinotify and run this command from a shell:

    $ python -m pyinotify -v /my-dir-to-watch



##[inotify](https://pypi.python.org/pypi/inotify)

官方说明: An adapter to Linux kernel support for inotify directory-watching.

==========
Installing
==========

Install via *pip*::

    $ sudo pip install inotify
