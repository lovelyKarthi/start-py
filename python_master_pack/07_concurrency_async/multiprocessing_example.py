"""Multiprocessing example for CPU bound tasks"""
from multiprocessing import Pool
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    with Pool(4) as p:
        print(p.map(fib, [20,21]))
