a =int(input("enter a number: "))
length=len(str(a))
for x in range(length):
    b= a%10
    print(b,end="")
    a=a//10