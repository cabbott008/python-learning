fname = input('Enter file: ')
try:
    lines = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()

for line in lines:
    if line.startswith('From '):
        line = line.split()
        sender = line[1]
        atpos = sender.find('@')
        sender = sender[atpos+1:]
        if sender not in counts:
            counts[sender] = 1
        else:
            counts[sender] += 1

# print(max(counts.items(), key=lambda k: k[1]))
print(counts)
