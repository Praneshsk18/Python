matrix=[[]*5 for _ in range(5)]
x=1
for i in range(5):
    matrix[i].append(x)
    x+=1
for i in range(4,0,-1):
    matrix[i].append(x)
    x+=1
for i in range(2,5):
    matrix[i].append(x)
    x+=1
for i in range(4,2,-1):
    matrix[i].append(x)
    x+=1
matrix[4].append(x)    
for i in matrix:
    i.sort(reverse=True)
for row in matrix:
    print(" ".join(map(str, row)))
