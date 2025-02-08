matrix=[[]*5 for _ in range(5)]
x=1
for i in range(4,-1,-1):
    matrix[i].append(x)
    x+=1
for i in range(1,5):
    matrix[i].append(x)
    x+=1
for i in range(4,1,-1):
    matrix[i].append(x)
    x+=1
for i in range(3,5):
    matrix[i].append(x)
    x+=1
matrix[4].append(x)
print(matrix)
for i in matrix:
    i.sort(reverse=True)
for row in matrix:
    print(" ".join(map(str, row)))
