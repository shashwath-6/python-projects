value1 = int(input("Enter the number"))
length = len(str(value1))
flag = 0
for i in range(2,value1):
    if value1 % i == 0:
        flag = 1
        break
    else:
        flag = 0

if flag == 0:
    print("Prime")
if flag == 1:
    print("Not prime")
