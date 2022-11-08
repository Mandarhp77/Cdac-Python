def ReverseMyString(a):
    st=""
    b=a[::-1]
    c=""
    vow = "aeiouAEIOU"
    count=0
    
    for char in range(0,len(b),2):
        c=b[char].lower()
        st=st+c
        c=""
    for char in vow:
        if(char in b):
            count = count+1

    return st , count

str = "CoRonaVIRUS_is_dangerous"
print(ReverseMyString(str))
