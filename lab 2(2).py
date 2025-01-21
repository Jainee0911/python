a=int(input("enter the number a"))
b=int(input("enter the number b"))
c=int(input("enter the number c"))
if a>b:
    if a>c:
        print("a is greater than b and c")
    else:
        print("c is greater than a and b")
elif a<b:
    if b<c:
        print("c is greater than a and b")
    else:
        print("b is greatert than a and c")
else:
    if a<c:
        print("c is greater than a and b and a and b are equal")
    else:
        print("a or b is greater than c")
if a>b:
    if b>c:
        print("c is smaller than b and a")
    else:
        print("b is smaller than a and c")
else:
    if a<c:
        print("a is smaller than c and b")
    else:
        print("c is smaller than a and b")
