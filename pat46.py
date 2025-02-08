x=1
for i in range(1,6):
    for j in range(i):
        print(x,end='')
        x+=i
    print()
    x=i+1
