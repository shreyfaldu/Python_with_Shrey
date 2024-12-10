set1 = {1,2,3,4,5}

print(set1)

set2 = set()
print(set2)

set2.add(3)
set2.add(5)
set2.add(7)
set2.add("Shrey")

print(set2)

set2.remove(3)

print(set2)

print(set2.pop())

set2.clear()
print(set2)

col1 = {1,2,3}
col2 = {3,4,5}

print(col1.union(col2))
print(col1.intersection(col2))

print(1 in col1)

print(col1.discard(4))


li = {1,2,3,4,5}

l2 = li.copy()
print(l2)

l2.add(8)
print(l2)
print(li)

l3 = {4,5,6,7}
l4 = frozenset(l3)
l3.add(9)
print(l4)

set1 = {1,2}
set2 = {3,4}

if set2 <= set1:
    print("Treu")
else:
    print("false")