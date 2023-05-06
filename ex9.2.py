fnand = input('Enter file: ')
try:
    lines = open(fnand)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()

for line in lines:
    if line.startswith('From '):
        line = line.split()
        day = line[2]
        if day not in counts:
            counts[day] = 1
        else:
            counts[day] += 1

print(counts)
