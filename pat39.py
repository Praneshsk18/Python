x=5
for i in range(1,6):
    for j in range(i):
        print(x,end='')
        x+=1
    print()
    x=5-i
