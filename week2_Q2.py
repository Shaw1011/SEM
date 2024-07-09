def check_character_type(char):
    if char.isdigit():
        print(f"The character '{char}' is a digit.")
    elif char.islower():
        print(f"The character '{char}' is a lowercase character.")
    elif char.isupper():
        print(f"The character '{char}' is an uppercase character.")
    else:
        print(f"The character '{char}' is a special character.")

char = input("Enter a character: ")
check_character_type(char)
