char ='a'
vowels=['a','e','i','o','u']
def vowel(x):
    for i in vowels:
        if i==x:
            print("Yes")
            break
        print("No")    
vowel(char)
