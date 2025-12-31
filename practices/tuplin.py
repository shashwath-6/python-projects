tup =tuple(x for x in range(10))
print(tup)

tup_1 = (1,2,3)
a,b,c = tup_1
print(a," ", b," ", c)

def return_func(tup : tuple) -> tuple :
    return tup

print(return_func(tup))

a=(1,2,3)
b=(1,2,3,4)
c=(1,3,5)
print(a)