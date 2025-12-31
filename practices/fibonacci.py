from idlelib.outwin import file_line_pats


def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)

def iter_fibo(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b

n = int(input("Enter the number: "))
for i in range(0,n):
    print(fibonacci(i))
print("-"*60)
print("Iterative Fibonacci sequence:")
iter_fibo(n)


