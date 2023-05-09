import string

fnand = input('Enter file: ')
try:
    lines = open(fnand)
except:
    print('File cannot be opened')
    exit()

counts = dict()
totals = 0
average = 0

for line in lines:
    #line = line.translate(line.maketrans('', '', string.punctuation + string.digits))
    line = line.rstrip()
    #line = line.lower()
    line = line.split()
    for word in line:
        for letter in word:
            totals += 1
            if letter not in counts:
                counts[letter] = 1
            else:
                counts[letter] += 1

letters = list()

for key, val in list(counts.items()):
    letters.append((key, val))

letters.sort()
for key, val in letters:
    average = round(val / totals * 100, 2)
    print(key, 'shows up', average, 'percent or', val, 'times in', fnand)
print('Iterated though', totals, 'letters.')
