import string

# fnand = input('Enter file: ')
try:
    lines = open('mbox-short.txt')
except:
    print('File cannot be opened')
    exit()

counts = dict()

for line in lines:
    # line = line.rsplit()
    line = line.split()
    for word in line:
        word = word.split()
        word =word.translate(word.maketrans('', '', string.punctuation))
        for ch in word:
            ch = ch.lower()
            if ch not in counts:
                counts[ch] = 1
            else:
                counts[ch] += 1

lst = list()

for key, val in list(counts.items()):
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key, val)
