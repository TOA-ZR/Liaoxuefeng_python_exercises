# -*- coding: utf-8 -*-def fact(n):

from functools import reduce
def mymulti(x,y):
    return x*y
multi=reduce(mymulti,list(range(1,11)))
#print(multi)

def mymultiple(x,y):
    return x*y


def fact(n):
    '''
    Calculate 1*2*...*n

    >>> fact(1)
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
    ...
    ValueError
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)


#一定要写这个，import doctest才能进行文本测试
if __name__ == '__main__':
    import doctest
    doctest.testmod()


