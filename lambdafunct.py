x=lambda x,y,z:x+y+z
print(x(10,20,30))

gtr=lambda x,y:x if (x>y) else y
print(gtr(10,20))

a=(0,1,1,2,3,5,8,13,21,34)
f=(list(filter(lambda x:x%2,a)))
print(f)

#map
lst=(1,2,3,4)
z=(list(map(lambda x:x+5,lst)))
print(z)

from functools import reduce
p=reduce(lambda x,y:x+y,a)
print(p)

b=(1,1,1,1)
c=(list(map(lambda x,y:x+y,lst,b)))
print(c)

d=(list(map(lambda x,y:x*y,lst,b)))
print(d)

fruits=['mango','orange','apple','kiwi']
e=(list(filter(lambda x:'a' in x,fruits)))
print(e)


