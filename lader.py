n = int (input("num : "))
num=1
for i in range(1,n+1):
    if(i%2!=0):
        for j in range(1,num+1):
            print(i,end=" ")
        num+=1
        print()
    else:
        continue

