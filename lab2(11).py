def straightline():
    x1=int(input("enter the value of x1"))
    x2=int(input("enter the value of x2"))
    x3=int(input("enter the value of x3"))
    y1=int(input("enter the value of y1"))
    y2=int(input("enter the value of y2"))
    y3=int(input("enter the value of y3"))
    if y2-y1/x2-x1==y3-y2/x3-x2:
        print("all three points lie on same line")
    else:
        print("these 3 points do not lie on same line")
straightline()
