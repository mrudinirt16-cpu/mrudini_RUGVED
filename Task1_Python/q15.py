n=int(input("Enter size of matrix: "))
matrix=[]
for i in range(n):
    row=list(map(int,input().split()))
    matrix.append(row)
rotated=[]
for j in range(n):
    row=[]
    for i in range(n-1,-1,-1):
        row.append(matrix[i][j])
    rotated.append(row)
print("Rotated matrix:")
for row in rotated:
    print(*row)
spiral=[]
t=0
b=n-1
l=0
r=n-1
while t<=b and l<=r:
    for j in range(l,r+1):
        spiral.append(rotated[t][j])
    t+=1
    for i in range(t,b+1):
        spiral.append(rotated[i][r])
    r-=1
    if t<=b:
        for j in range(r,l-1,-1):
            spiral.append(rotated[b][j])
        b-=1
    if l<=r:
        for i in range(b,t-1,-1):
            spiral.append(rotated[i][l])
        l+=1
print("Spiral order:")
print(*spiral)