'''
returns a list of Least Frequent Character in String
string="welcometoknowit"
least frequency char :['l','c','m', 'k', 'n', 'i']

'''
strr = "welcometoknowit"
dct = {}
lst = []
res = []

for i in strr:
    if(i in dct):
        dct[i] = dct[i]+1
        pass
    else:
        dct[i]=1

for j in dct:
    (lst.append(dct[j]))

lst = list(set(sorted(lst)))

for j in dct:
    if(dct[j]==lst[0]):
        (res.append(j))
print(res)



