from functools import reduce
a=[1,2,2,3,4,1,6,7,4]
v=[]
for i in range(len(a)):
    if a[i] in a[i+1:]:
        v.append(a[i])
print(v)
