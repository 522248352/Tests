# coding=utf-8
import requests
import json

a = 42
print("我的"+ `a`)

b = 4,
c = (4,)
print(type(c))

d = list(b)
print(type(d))


print('y' in 'python')
print(cmp(16,16))
print(min((1,5,6,9)))
print(max([1,2,5,9],(6,7)))

lis1 = ['1','4','5']
print('+'.join(lis1))


print('p+y+t+h+o+n'.split("+"))
print("+".join(["pyth","on"]))

dic1 = {1:2,2:3}
dict.fromkeys(["1","2"])
print(dict.fromkeys(["1","2"]))

for i in range(0,100):
    print(i)


for i in range(6):
    print(i)


resu = []
for x in range(3):
    for y in range(3):
        resu.append((x,y))
print(resu)


print(__name__)