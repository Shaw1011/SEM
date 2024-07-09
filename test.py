def has_duplicates(input_list):
    return len(input_list) != len(set(input_list))
my_list = input("Enter the values: ").split()
print(has_duplicates(my_list))