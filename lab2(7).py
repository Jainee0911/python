def leapyear():
    year=int(input("enter any number"))
    if year%400==0:
        if year%100==0:
            if year%4==0:
                print("it is a leap year")
    else:
        print("ït is not a leap year")
leapyear()
    
