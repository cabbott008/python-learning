fhand = input('Enter file: ')
lines = open(fhand)
unique = list()

for line in lines:
    words = line.split()
    for word in words:
        # word = word.lower()
        if word not in unique:
            unique.append(word)
unique.sort()
print(unique)
