

fnand = input('Enter file:')
try:
    lines = open(fnand)
except:
    print('File cannot be opened')
    exit()

counts = dict()

for line in lines:
    line = line.split()
    # line = line.rstrip()
    # line = line.translate(line.maketrans(' ', ' ', string.punctuation))
    # line = line.lower()
    for word in line:
        word = line.split()
        for ch in word:
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
