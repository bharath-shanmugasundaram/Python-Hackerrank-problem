n = int(input())
red = n
for i in range(1,n+1):
    for j in range(1,red+1):
        print(j,end=" ")
    red = red-1    
    print()