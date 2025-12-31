def avg(tup : tuple) -> float:
    total = sum(tup)
    return total / len(tup)

test= []
upto = int(input("Enter the total amount of student "))
for i in range(upto):
    mark = int(input("Enter your mark: "))
    if mark%100 == mark:
        test.append(mark)

test_tup = tuple(test)
print("The highest mark: ",avg(test_tup))
maximum = test_tup[0]
max_index = test_tup.index(maximum)
for i in test_tup:
    if i > maximum :
        maximum = i
print("The highest mark: ",maximum)

val = list(test_tup)
del val[max_index]
print(val)