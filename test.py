def split_and_join(line):
    new=[]
    lop =0
    line = line.split(" ")
    for i in range(len(line)):
        if i < len(line)-1 :
            new.append(line[i]+'-')
        else:
            new.append(line[i])
    print(new)
    print(lop)
    new=''.join(new)
    print(new)

line = input()
result = split_and_join(line)
print(result)