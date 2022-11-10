'''
returns a list of Maximum  Frequent Character in String
string="welcometoknowit"
max frequency char :['o']

'''
strr = "welcometokmmmmmmmnowit"
dct = {}
maxx=0
val=0

for i in strr:
    if(i in dct):
        dct[i] = dct[i]+1
        if(dct[i]>maxx):
            maxx = dct[i]
    else:
        dct[i]=1
        

for j in dct:
    if dct[j]==maxx:
        val=j
print(dct)
print(maxx)
print(val)
