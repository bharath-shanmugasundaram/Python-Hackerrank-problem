n = input()
l = list(n)
leng = len(n)

for i in range(leng-1):
    if l[i] == 'a' or l[i] == 'e' or l[i] == 'i' or l[i] == 'o' or l[i] == 'u':
        empty=l[i]
        ste =0
        for j in range(leng-1):
            if l[j]==empty  :
                ste+=1
            else :
                continue
        if (ste>=2):
            continue
        else :
            l.remove(l[i])
    else :
        continue
    
strin =''.join(l)
print(strin)