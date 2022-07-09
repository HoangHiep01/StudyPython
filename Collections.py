# collections: Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter

mystring = "aabababdceec"
mycounter = Counter(mystring)
print(mycounter) # Counter({'a': 4, 'b': 3, 'c': 2, 'e': 2, 'd': 1})
print(mycounter.items()) # dict_items([('a', 4), ('b', 3), ('d', 1), ('c', 2), ('e', 2)])
print(mycounter.keys()) # dict_keys(['a', 'b', 'd', 'c', 'e'])
print(mycounter.values()) # dict_values([4, 3, 1, 2, 2])
print(mycounter.most_common(1)) # [('a', 4)]
print(mycounter.most_common(1)[0]) # ('a', 4)
print(mycounter.most_common(1)[0][0]) # a
print(list(mycounter.elements())) # print list elements

from collections import namedtuple

Point = namedtuple("Point", "x,y")
pt = Point(1,-2) # Point(x=1, y=-2)
print(pt)
print(pt.x, pt.y) # 1 -2

from collections import OrderedDict

ordereddict = OrderedDict()
ordereddict["a"] = 1
ordereddict["b"] = 2
ordereddict["d"] = 4
ordereddict["c"] = 3
print(ordereddict) # OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

from collections import defaultdict

dedict = defaultdict(int)

dedict["a"] = 1
dedict["b"] = 2
print(dedict["a"]) # 1
print(dedict["b"]) # 2
print(dedict["c"]) # 0 default by int type

from collections import deque

deck = deque() # deque([])

deck.append(1) # deque([1])
deck.append(2) # deque([1, 2])
deck.appendleft(3) # deque([3, 1, 2])
deck.pop() # deque([3, 1])
deck.popleft() # deque([1])
deck.clear() # deque([]) remove all elements
deck.extend([1,2,3]) # deque([1,2,3])
deck.extend([4,5]) # deque([1,2,3,4,5])
deck.extendleft([6,7,8]) # deque([6,7,8,1,2,3,4,5])
deck.rotate(1) # deque([5,6,7,8,1,2,3,4])
deck.rotate(2) # deque([3,4,5,6,7,8,1,2])
deck.rotate(-1) # deque([4,5,6,7,8,1,2,3])