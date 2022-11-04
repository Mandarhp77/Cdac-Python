def dictt(key,value,lst):
    try:
        print(lst[key])
    except:
        lst[key]=value
    else:
        if(lst[key]==value):
            print("already")
        else:
            print("not in")
    finally:
        print(f"key {key} value {lst[key]}")
        
        
dict1 = {10:100,20:200}       
dictt(10,200,dict1)