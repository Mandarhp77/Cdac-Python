while(1):
    try:
         a= int(input("Enter age"))
         h = int(input("Enter height"))
         w = int(input("Enter weight"))
         name = input("Enter name")
    except:
        print("enter currect input")
    else:
        print(f"age is {a} height is {h} weight is{w} name is {name}")
        break