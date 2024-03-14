n = input()
l = list(n)
lftpar =0
rgtpar =0
for i in range(len(n)):
    if l[i]=='(':
        lftpar+=1
    elif l[i]==')':
        rgtpar+=1
if rgtpar == lftpar :
    print(0)
else:
    print(1)