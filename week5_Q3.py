def exception_handling_demo():
    try:
        result = 10 / 0
        print(f"Result: {result}")

    except ZeroDivisionError as e:
        print(f"Error: Division by zero! ({e})")

    try:
        num = int("not a number")
        print(f"Number: {num}")

    except ValueError as e:
        print(f"Error: Invalid conversion! ({e})")

    try:
        lst = [1, 2, 3]
        print(f"Element: {lst[5]}")

    except IndexError as e:
        print(f"Error: Index out of range! ({e})")

    try:
        d = {'a': 1, 'b': 2}
        print(f"Value: {d['c']}")

    except KeyError as e:
        print(f"Error: Key not found! ({e})")

    try:
        with open('non_existent_file.txt', 'r') as f:
            content = f.read()
            print(content)

    except FileNotFoundError as e:
        print(f"Error: File not found! ({e})")

exception_handling_demo()
