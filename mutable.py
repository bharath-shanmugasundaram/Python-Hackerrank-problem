def mutate_string(s, i, c):
    l = list(s)
    l[i] = c
    string = ''.join(l)
    return string
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)