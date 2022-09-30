
words = open("/Users/chenyujie/Repos/spelling-bee-crack/python_spelling_bee_crack/20k.txt").read().splitlines()

word_dict = []
for word in words:
    if len(word) >= 4:
        word_dict.append(word)

# print(word_dict, len(word_dict))
