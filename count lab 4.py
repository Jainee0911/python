def count():
    string=str(input("enter any string"))
    count1=0
    count2=0
    for i in string:
        if 'a'<=i<='z'or 'A'<=i<='Z':
            count1+=1
    print("the number of alphabets is",count1)
    for i in string:
        if i in '1234567890':
            count2+=1
    print("the number of numbers is",count2)
count()

