x=1
for i in range(5):
    for j in range(5):
        if i%2==0:
            print(x,end='')
            if x==0:
                x=1
            else:
                x=0
        else:
            print(0,end='')
    print()        
