def add_single_letter_words(word_list):
    single_letter_words = ["I", "a", ""]
    return word_list + single_letter_words

word_list = ["hello", "world"]
updated_word_list = add_single_letter_words(word_list)
print(updated_word_list)
