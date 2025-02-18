def count():
    l1=[('darshit','ashit','devang'),'ragi','ashna','darshini',('darshil',)]
    boys=0
    girls=0
    for i in l1:
        if isinstance(i,tuple):
            boys+=len(i)
        
        else:
            girls+=1
    print("no of boys= ",boys)
    print("no of girls= ",girls)
            
count()

        
    

