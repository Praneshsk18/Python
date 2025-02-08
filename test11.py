a,b,c=1,2,3
def large(*args):
    x=0
    for i in args:
        if i>x:
            x=i
    print(f"the largest number is {x}")
large(a,b,c)    
