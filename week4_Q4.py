def generate_binary_strings(n):
    def generate(n, current):
        if n == 0:
            print(current)
        else:
            generate(n - 1, current + '0')
            generate(n - 1, current + '1')

    generate(n, '')

n = 3
generate_binary_strings(n)
