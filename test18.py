num=5
def prime(x):
    for i in range(2,x-1):
        if x%i==0:
            print(f"{x} is not a prime number")
            return 0
    print(f"{x} is a prime number")    
prime(num)        
        
