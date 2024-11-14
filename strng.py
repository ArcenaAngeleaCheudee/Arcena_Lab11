words = []
length = []
num = 1

for user in range(10):
    word = input(f"Enter word {num}: ")
    words.append(word)
    num += 1

length1 = int(input("Enter a length/number: "))

for word in words:
    if len(word) >= length1:
        length.append(word)
    else:
        continue
print(f"Here are the words that have {length1} letters: {length}")