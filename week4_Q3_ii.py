def remove_word(s, word):
    return s.replace(word, '')

s = "This is an example. This example is simple."
word = "example"
print(remove_word(s, word))
