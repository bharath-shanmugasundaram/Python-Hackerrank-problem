x=int(input("x"))
y=int(input("y"))
z=int(input("z"))
n=int(input("n"))


final =[]
for i in range(0,x+1) :
    for j in range(0,y+1) :
        for k in range(0,z+1) :
            l=[i,j,k]
            total = sum(l)
            if l==n :
                continue
            else :
                final.append(l)
print(final)