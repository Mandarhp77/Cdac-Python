def long_word(lst):
    l=lst[0]
    for i in range(len(lst)):
        if len(l)<len(lst[i]):
            l=lst[i]
    return(l)

app=["bbbb","aalesh","mandarlll","aaa"]
print(long_word(app))