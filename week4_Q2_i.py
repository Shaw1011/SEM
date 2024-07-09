def has_duplicates(lst):
    return len(lst) != len(set(lst))

lst = [1, 2, 3, 4, 5, 1]
print(has_duplicates(lst))

lst = [1, 2, 3, 4, 5]
print(has_duplicates(lst))
