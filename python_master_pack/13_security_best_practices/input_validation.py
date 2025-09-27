"""Simple input validation examples to avoid injection"""
import re

def safe_username(u):
    if re.match(r'^[a-zA-Z0-9_\-]{3,30}$', u):
        return True
    return False

if __name__ == '__main__':
    print(safe_username('karthi_1'))
    print(safe_username('drop table;'))
