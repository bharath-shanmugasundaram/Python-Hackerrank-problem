n = int(input())
arr = map(int, input().split())

l=list(arr)
l.sort(reverse=True)
if l[0] == l[1]:
    for i in range(2, n):
        if l[i] != l[i - 1]:
            print(l[i])
            break
else:
    print(l[1])