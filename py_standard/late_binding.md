###late binding后期绑定
# python3

    >>def test():
        return(foo)
    >>foo = 1
    >>test()
    1
    >>foo = 13
    >>test()
    13

你定义一个函数，函数内的变量并不是立刻就把值绑定了，而是等调用的时候再查找这个变量。
如图，定义函数的时候没有 foo 变量，但是仍然可以，只要调用的时候环境里有就行。


    lst = [lambda x: x*i for i in range(4)]
    for func in lst:
        print func(2)

一个道理，在 for 里面 i 的值是不断改写的，但是 lambda 里面只是储存了 i 的符号，调用的时候再查找。这就是后期绑定。

为什么加了默认参数就成功了呢？因为在创建函数的时候就要获取默认参数的值，放到 lambda 的环境中，所以这里相当于存在一个赋值，从而 lambda 函数环境中有了一个独立的 i。


最普遍的解决方案是创建一个闭包，通过使用默认参数立即绑定它的参数。例如：

    def multipliers():
        return [lambda x, i=i : i * x for i in range(4)]

优雅的写法是用生成器：
    
    for multiplier in (lambda x : i * x for i in range(5)):
        print(multiplier(2))

这样惰性求值就可以避免 i 的改写。或者：def create_multipliers():
    
    for i in range(5):
        yield lambda x: i * x

    for multiplier in create_multipliers():
       print(multiplier(2))
