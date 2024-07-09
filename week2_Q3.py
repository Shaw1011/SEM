def print_fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        print(a, end=' ')
        a, b = b, a + b
        count += 1
    print()

n = int(input("Enter the number of terms in the Fibonacci sequence: "))
print_fibonacci(n)
