# mydict2.py

class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)
        #super：为了调用父类(超类)的方法或者属性的一个方法。


    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)


    def __setattr__(self, key, value): #self.key = value or setattr(obj,"y",16)
        #赋值的写法; d= Dict(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
        self[key] = value







if __name__=='__main__':
    import doctest

    doctest.testmod()



