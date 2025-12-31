list1 = ["Apple",1,1.1,True, ["Hello"]]
for item in list1:
    print(type(item))

index =0
a1=True
while a1:
    choice =int(input("Enter the choice: "))
    if(choice==1):
        val= int(input("Enter the number: "))
        val1=int(input("Enter the string: "))
        index= int(input("Enter the index: "))
        if val:
            list1.insert(index,val)
        if val1:
            list1.insert(index,val1)
    elif (choice==2):
        val= input("Enter the number: ")
        val1=int(input("Enter the string: "))
        index= int(input("Enter the index: "))
        if val:
            list1.remove(val)
        if index:
            del list1[index]
        if val1:
            list1.remove(val1)
    elif (choice==3):
        for item in list1:
            print(item)
    elif(choice==4):
        a1=False
    else:
        print("Invalid choice")

a=list1.copy()

a[0]="Banana"
print(a)

print(list1)

value = [10,20,30]
index =0
#list1.extend(value)

for i in value:
    list1.insert(index,i)
    index+=1

print(list1)

numbers = [x for x in a if isinstance(x, (int, float))]
strings = [x for x in a if isinstance(x, str)]

sorted_numbers = sorted(numbers)
sorted_strings = sorted(strings)

sorted_list = sorted_numbers + sorted_strings
print(sorted_list)
