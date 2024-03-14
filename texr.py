n = input()
l = list(n)
nl=[]
for i in range(len(n)):
    if l[i] == 'a' or l[i] == 'e' or l[i] == 'i' or l[i] == 'o' or l[i] == 'u':
        continue
    else:
        nl.append(l[i])
nl=''.join(nl)
print(nl)