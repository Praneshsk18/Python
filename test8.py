year=2000
def leapyear(x):
    if x%4==0 or x%1000==0:
        print("Leap Year")
    else:
        print("Not a Leap Year")
leapyear(year)
