def swap_case(s):
    elop =""
    for i in range(0,len(s)):
        if s[i].isupper():
            elop=elop+s[i].lower()
        elif s[i].islower():
            elop=elop+s[i].upper()
        else :
            elop=elop+s[i]
    return elop

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)