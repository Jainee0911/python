def rectangle():
    a=int(input("enter the length of rectangle"))
    b=int(input("enter the breadth of rectangle"))
    area=a*b
    perimeter=2*a+2*b
    print("area=",area)
    print("perimeter =",perimeter) 
    if area>perimeter:
        print("area is greater than perimeter")
    else:
        print("perimeter is greater than area")
rectangle()
