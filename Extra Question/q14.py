'''
returns a list of  Odd Frequency Characters
string="welcometoknowit"
odd frequency char :[ 'l', 'c', 'o', 'm', 'k', 'n', 'i']
'''
strr = "welcometoknowit"
dct = {}

lst = []

for i in strr:
    if(i in dct):
        dct[i] = dct[i]+1
    else:
        dct[i]=1

for j in dct:
    if dct[j]%2==1:
        lst.append(j)
print(lst)