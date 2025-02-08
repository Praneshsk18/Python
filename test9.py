num=22
def multi(num):
    if(num%3==0) and (num%7==0):
        print(f"{num} is a multiple of 3 and 7".format(num))
    else:
        print(f"{num} is not a multiple of 3 and 7".format(num))
multi(num)
