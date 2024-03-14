if __name__ == '__main__':
    l=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        listk=[name,score]
        l.append(listk)
l.sort(key=lambda x: x[1])
if l[1][1] == l[2][1]:
    for i in range(1, len(l)):
        if l[i][0] == l[i - 1][0]:
            print(l[i][0])
            break
else:
    print(l[1][0])