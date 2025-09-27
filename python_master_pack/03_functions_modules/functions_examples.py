"""Functions, defaults, args, kwargs, lambda, closures, modules"""
from typing import Callable

def greet(name='Guest'):
    return f'Hello, {name}'

def variadic(*args, **kwargs):
    return args, kwargs

# closure
def make_multiplier(n):
    def mul(x):
        return x * n
    return mul

double = make_multiplier(2)

# decorator example
def simple_logger(fn):
    def wrapper(*a, **kw):
        print('calling', fn.__name__)
        return fn(*a, **kw)
    return wrapper

@simple_logger
def add(a,b):
    return a+b

if __name__ == '__main__':
    print(greet('Karthi'))
    print(variadic(1,2,three=3))
    print('double 5 ->', double(5))
    print('add ->', add(2,3))
