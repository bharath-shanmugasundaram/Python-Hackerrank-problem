i1= input().split()
i2= input().split()

lent1 = len(i1)
lent2 = len(i2)

estr1=""
estr2=""

for i in range(lent1):
    estr1+=i1[i]

for j in range(lent2):
    estr2+=i2[j]

if estr1 == estr2:
    print("True")
else:
    print("fales")