from collections import defaultdict

d = {'k1':1}
print(d)
print(d['k1'])



d = defaultdict(object)
d['one']
d['two'] = 2

for item in d:
    print(item)



o = {}
o['a'] = 1
o['b'] = 2
o['c'] = 3
o['d'] = 4
o['e'] = 5
print(o)

for k,v in d.items():
    print(k,v)

from collections import OrderedDict
o = OrderedDict
o = {}
o['a'] = 1
o['b'] = 2
o['c'] = 3
o['d'] = 4
o['e'] = 5


for k,v in d.items():
    print(k,v)

#NAMEDTUPLE

t = (1,2,3,4,5)
print(t[0])

from collections import namedtuple

Dog = namedtuple('Dog','age breed name')
sam = Dog(age=2,breed='Lab',name='Sam')
print(sam)
print(sam.age)
print(sam.breed)


