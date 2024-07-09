def invert_dictionary(d):
    return {v: k for k, v in d.items()}

d = {'a': 1, 'b': 2, 'c': 3}
inverted_d = invert_dictionary(d)
print(inverted_d)
