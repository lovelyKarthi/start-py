"""Lists, dicts, sets, tuples, and advanced collections"""
from collections import Counter, defaultdict, deque, namedtuple

# list
nums = [1,2,3]
nums.append(4)

# tuple unpacking
a, b, *rest = [1,2,3,4]
print(a,b,rest)

# set
s = set([1,2,2,3])

# Counter
words = ['a','b','a','c','b','a']
print('most common', Counter(words).most_common(2))

# defaultdict
d = defaultdict(list)
d['k'].append(1)

# deque as queue
q = deque()
q.append(1); q.append(2)
q.popleft()

# namedtuple usage
Point = namedtuple('Point','x y')
p = Point(3,4)
print('point', p.x, p.y)
