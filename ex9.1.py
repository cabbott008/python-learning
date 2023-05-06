fname = input('Enter file: ')
try:
    lines = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()

for line in lines:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

for key in counts:
    print(counts[key], key)
