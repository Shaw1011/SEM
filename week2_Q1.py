def print_triangle():
    num = int(input("enter a number:"))
    for i in range(num, 0, -1):
        print((str(i) + ' ') * (num - i))

print_triangle()
