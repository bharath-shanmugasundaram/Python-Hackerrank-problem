n=input()
l=list(n)
al=[]
nu=[]
for i in range(len(n)-1):
    if l[i].isnumeric:
        for j in range(1,3):
            if l[i+j].isnumeric:
                nu.append(l[i]+l[i+j])
            else:
                nu.append(l[i])
    elif l[i].isalpha:
        al.append(l[i])
print(al)
        