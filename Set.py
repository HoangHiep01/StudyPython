#Set: unordered, mutable, not allow duplicate

# Declare
myset = {1,3,4,2,1,4,"4"}
print(myset)

myset2 = set("Hello")
print(myset2)

# Only set() method can declare empty set
# Take string or list

# Common method

# add()
myset = set()
print(myset)
myset.add(2)
print(myset)
myset.add(1)
print(myset)
myset.add(2)
print(myset)

# remove() raise KeyError if have no an element
myset.remove(2)
print(myset)

# discard() same remove but do nothing if element is not a member
myset.discard(3)

# clear() remove all element
myset.clear()
print(myset)

# pop() remove and return first value in set
myset = set("Hello")
print(myset)
print(myset.pop())
print(myset)

# union() combine both set
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
num = evens.union(odds)
print(num)

# interdection() find elements inside both set
set1 = {1,2,4,7}
set2 = {2,7,9,10}
set3 = set1.intersection(set2)
print(set3)

# difference() find elements inside set A but not inside set B
diff = set1.difference(set2)
print(diff)

# symmetric_difference() find elements not inside both set
diff = set1.symmetric_difference(set2)
print(diff)

# update() update set with the union of itself and others
set1 = {1,2,4,7}
set2 = {2,7,9,10}

set1.update(set2)
print(set1)

# intersection_update() update set with the intersection of itself and others
set1 = {1,2,4,7}
set2 = {2,7,9,10}

set1.intersection_update(set2)
print(set1)

# update will change itself with other methods

# issubset() check setA is inside setB
set1 = {1,2}
set2 = {1,2,7,9,10}
print(set1.issubset(set2))

# issuperset() report this set contains another set
print(set2.issuperset(set1))

# isdisjoint() check both set has no same elements
print(set1.isdisjoint(set2))

# copy() duplicate set, diff when use "="
set3 = set1.copy()
# also do: set3 = set(set1)
print(set3)

# frozenset() is set but immutable, add, remove, update are not allowed
fzset = frozenset()