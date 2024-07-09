def is_sorted(lst):
    return lst == sorted(lst)

lst = [1, 2, 3, 4, 5]
print(is_sorted(lst))

lst = [5, 3, 4, 1, 2]
print(is_sorted(lst))
