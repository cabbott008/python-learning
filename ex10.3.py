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
    line = line.translate(line.maketrans('', '', string.punctuation + string.digits))
    line = line.rstrip()
    line = line.lower()
    line = line.split()
    for word in line:
        for ch in word:
            totals +=1
            if ch not in counts:
                counts[ch] = 1
            else:
                counts[ch] += 1

lst = list()

for key, val in list(counts.items()):
    lst.append((key, val))

lst.sort()
for key, val in lst:
    average = round(val / totals * 100, 2)
    print(key, 'shows up', average, 'percent or', val, 'times in', fnand)