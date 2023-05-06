import string

fname = input('Enter file: ')
try:
    lines = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()

for line in lines:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

for key in counts:
    print(counts[key], key)
