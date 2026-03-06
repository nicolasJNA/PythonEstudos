# count é um iterador sem fim

from itertools import count

c1 = count(10,2)
r1 = range(10,100,2)

print(hasattr(c1,'__iter__'))
print(hasattr(c1,'__next__'))

print(hasattr(r1,'__iter__'))
print(hasattr(r1,'__next__'))

print('c1')
for i in c1:
    if(i > 100):
        break
    print(i)
print()
print('r1')
for i in r1:
    print(i)