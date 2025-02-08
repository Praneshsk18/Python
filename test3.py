def compare_larger(a,b):
    if a>b:
        return a
    else:
        return b
a=int(input("Enter the Input 1: "))
b=int(input("Enter the Input 2: "))
print("The Largest Element is "+str(compare_larger(a,b)))
