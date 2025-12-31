a= int(input("enter a number: "))
value=0
value1=a
length=len(str(a))
while a>0:
    temp = a%10
    value+=temp**length
    a=a//10
if value==value1:
    print("armstrong")
else:
    print("not armstrong")