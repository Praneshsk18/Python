arr=['A','B','C','D','E','F','G','H','I']
x=0
for i in range(5):
    for j in range(5):
        print(arr[x+j],end='')
    print()
    x=i+1
