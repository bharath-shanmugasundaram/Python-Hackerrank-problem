n,odd,even=input().split(','),[],[]
for i in range(len(n)):
    r=int(n[i])
    if r%2==0:even.append(n[i])  
    else:odd.append(n[i])
even,odd,fin,evenum,oddnum=sorted(even),sorted(odd,reverse=True),[],0,0
for j in range(0,len(n)):
    if j%2==0: 
        fin.append(odd[evenum])
        evenum+=1
    elif j%2!=0:
        fin.append(even[oddnum])
        oddnum+=1
fin=','.join(str(num) for num in fin)
print(fin)