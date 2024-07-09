import numpy as np

def convert_to_arrays(lst, tpl):
    array_from_list = np.array(lst)
    array_from_tuple = np.array(tpl)
    return array_from_list, array_from_tuple

lst = [1, 2, 3, 4, 5]
tpl = (6, 7, 8, 9, 10)

array_from_list, array_from_tuple = convert_to_arrays(lst, tpl)
print("Array from list:", array_from_list)
print("Array from tuple:", array_from_tuple)
