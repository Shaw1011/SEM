def capitalize_sentence(sentence):
    words = sentence.split()
    capitalized_words = [word[0].upper() + word[1:].lower() for word in words]
    return ' '.join(capitalized_words)

sentence = "this is an example sentence."
print(capitalize_sentence(sentence))
