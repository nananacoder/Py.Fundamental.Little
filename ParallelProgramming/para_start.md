The threads of the same process share the address space and other resources, while processes are independent of each other.


##Thread-based Parallelism

It can be stated that a thread is contain inside a process and that different threads in the same process conditions share some resources.
In contrast to this, different processes do not share their own resources with other processes.

 A typical application of a thread is certainly parallelization of an application software, especially, to take advantage of modern multi-core processors, where each core can run a single thread. 

Multithreaded programming prefers a communication method between threads using _the space of shared information_. 
This choice requires that the major problem that is to be addressed by programming with threads is related to **_the management of that space_**.

###implement a new thread using the threading module
* define a new subclass of the Thread class
* override the` __init__(self [,args])` method to add additional arguments
* override the `run(self [,args])`method to implement what the thread should do when it is started

Let's recap:
* Locks have two states: locked and unlocked
* We have two methods that are used to manipulate the locks: acquire() and release()

The following are the rules:
* If the state is unlocked, a call to acquire() changes the state to locked
* If the state is locked, a call to acquire() blocks until another thread calls release() 
* If the state is unlocked, a call to release() raises a RuntimeError exception
* If the state is locked, a call to release() changes the state to unlocked

the negative aspects of using locks:
Despite their theoretical smooth running, the locks are not only subject to harmful situations of deadlock, but also have many other negative aspects for the application as a whole. This is a conservative approach which, by its nature, often introduces unnecessary overhead; it also limits the scalability of the code and its readability. Furthermore, the use of a lock is decidedly in con ict with the possible need to impose the priority of access to the memory shared by the various processes. Finally, from a practical point of view, an application containing a lock presents considerable dif culties when searching for errors (debugging). In conclusion, it would be appropriate to use alternative methods to ensure synchronized access to shared memory and avoid race conditions.

RLock,Lock: RLock中出了状态locked和unlocked以外，还记录了当前lock和owner和递归层数，使得RLock可以被同一个线程多次acquire()

###semaphores信号
当很多线程共用资源时使用。Semaphore管理一个内置的计数器，每当调用acquire()时内置计数器-1；调用release时+1. 计数器不能小于0;当计数器为0时，acquire()将阻塞线程直到其他线程调用release()

当一个线程想要access一个和信号相关联的资源的时候，必须调用acquire(),然后他会减少信号的内置计数变量，如果这个变量不是负的就允许这个线程去占用这个资源。如果是负的，这个线程将会被延期。

# condition
一个线程等待一个特殊条件 ，同时另一个线程发一个提示说这个条件发生了。一旦这个条件发生，等待条件的线程就会acquire lock从而access到共用资源。
