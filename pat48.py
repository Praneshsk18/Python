x=1
l=0
matrix=[[]*5 for i in range(5)]
print(matrix)
for i in range(4,-1,-1):
    for j in range(i+1):
        matrix[j+l].append(x)
        x+=1
    l+=1
print(matrix)
for i in matrix:
    i.sort(reverse=True)
    print(i)
for row in matrix:
    print(" ".join(map(str, row)))
