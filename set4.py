def SeperateNames():
    s1={"anya","bhavi","arya","bhavya"}
    a1=set()
    b1=set()
    for i in s1:
        if i.startswith('a'):
            a1.add(i)
    print(a1)
    for i in s1:
        if i.startswith('b'):
            b1.add(i)
    print(b1)
    
SeperateNames()



        
