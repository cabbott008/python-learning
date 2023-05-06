# fnand = input('Enter file: ')
try:
    lines = open('mbox-short.txt')
except:
    print('File cannot be opened')
    exit()

counts = dict()

for line in lines:
    if line.startswith('From '):
        line = line.split()
        hour = line[5]
        hour = hour[0:2]
        if hour not in counts:
            counts[hour] = 1
        else:
            counts[hour] += 1

lst = list()

for key, val in list(counts.items()):
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key, val)
