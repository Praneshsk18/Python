from functools import reduce
a=[1,2,3,4,5,6,7,8,9,0]
v=1
for i in a:
    if i==0:
        continue
    v*=i
print(v)
