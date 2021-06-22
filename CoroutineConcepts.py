def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)

'''
理解如下：
由于等号右边先运算，所以yield运算，返回1.然后等待输入。下次一次进入while循环yield a并再次等待。

>>> def num():
        a = yield 1
        while True:
            a = yield a
       
>>> c = num()
>>> c.send(None)
1
>>> c.send(5)
5
>>> c.send(100)
100
'''