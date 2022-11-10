'''
Given a String list, extract frequency of specific characters in the whole strings list.
Input : test_list = [“geeksforgeeks is best for geeks”], chr_list = [‘e’, ‘b’, ‘g’, ‘f’] 
Output : {‘g’: 3, ‘e’: 7, ‘b’: 1, ‘f’ : 2} 
'''

ip = "geeksforgeeks is best for geeks"
char = ["e", "b", "g", "f"]
dct = {}
dct2={}

for i in ip:
    if(i in dct):
        dct[i]=dct[i]+1
        
    else:
        dct[i]=1
#print(dct)

for i,j in dct.items():
    if i in char:
        dct2[i]=j
print(dct2)
