def sub_string(a,b):
    for i in range(len(a)-len(b)):
        if b==a[i:len(b)+i]:
            return True
    return False
a=input("Enter the String: ")
b=input("Enter the Sub String: ")
if (sub_string(a,b)):
    print("Yes")
else:
    print("NO")


