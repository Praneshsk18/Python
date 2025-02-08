a=[1,2,2,3,4,1,6,7,4]
s=10000
l=0
for i in a:
    if i<s:
        s=i
    if i>l:
        l=i
print(s,l)
