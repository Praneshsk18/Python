arr=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']
x=4
for i in range(4,-1,-1):
    for j in range(5):
        print(arr[x],end='')
        x+=5
    print()
    x=i-1
