def circle():
    r=int(input("enter the radius of the circle"))
    x=int(input("enter the x coordinate of the centre of the circle"))
    y=int(input("enter the y coordinate of the centre of th circle"))
    x1=int(input("enter any x coordinate"))
    y1=int(input("enter any y coordinate"))
    if x1*x1+y1*y1==r*r:
        print("the point lies on the circle")
    elif x1*x1+y1*y1<r*r:
        print("the point lies inside the circle")
    else:
        print("the point lies outside the circle")
circle()
