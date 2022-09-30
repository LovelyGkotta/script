import dict

# print(dict.word_dict)
words = dict.word_dict
center_letter = input("enter the center letter: ")
other_letters = []

for i in range(1, 7):
    letter = input("enter other letter " + str(i) + ": ")
    while letter in other_letters or letter == center_letter:
        print("letter has been used ")
        print("center letter:  ", center_letter)
        print("other letters:  ", other_letters)
        letter = input("enter other letter " + str(i) + ": ")
    other_letters.append(letter)

layer1 = []
for word in words:
    if center_letter in word:
        layer1.append(word)

layer2 = []
for word in layer1:
    breaker = True
    for letter in word:
        if letter not in other_letters and letter != center_letter:
            breaker = False
            break
    if breaker:
        layer2.append(word)

print(layer2)
print(len(layer2), "words has been founded")
