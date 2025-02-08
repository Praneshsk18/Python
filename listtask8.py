import random
def func():
    x=random.randint(1,10)
    while(True):
        a=int(input("Enter a number(1-10):"))
        if x==a:
            print('Correct')
            break
        else:
            print('Wrong')
func()
while(True):
    v=input("Do you want to play the game again: ")
    if v!='yes'or'Yes'or'YES':
        print('Thank you')
        break
    if v=='yes'or'Yes'or'YES':
        func()
    
