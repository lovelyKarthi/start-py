"""Custom exceptions and context managers examples"""
class AppError(Exception):
    pass

def divide(a,b):
    if b == 0:
        raise AppError('division by zero')
    return a/b

from contextlib import contextmanager

@contextmanager
def resource_manager(name):
    print('acquire', name)
    try:
        yield {'name':name}
    finally:
        print('release', name)

if __name__ == '__main__':
    try:
        print(divide(1,0))
    except AppError as e:
        print('caught', e)

    with resource_manager('demo') as r:
        print('using', r)
