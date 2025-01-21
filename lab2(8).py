def triangle():
    angleA=int(input("enter the 1st angle in degree"))
    angleB=int(input("enter the 2nd angle in degree"))
    angleC=int(input("enter the third angle in degree"))
    if angleA+angleB+angleC==180:
        print("it is a valid triangle")
    else:
        print("it is not a valid triangle")
triangle()
