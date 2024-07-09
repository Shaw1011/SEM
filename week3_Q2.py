def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

result = gcd(a, b)
print(f"The greatest common divisor of {a} and {b} is: {result}")
