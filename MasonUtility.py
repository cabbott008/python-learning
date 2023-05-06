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
        email = line[1]
        if email not in counts:
            counts[email] = 1
        else:
            counts[email] += 1

email_counts = list()

for key, val in counts.items():
    email_counts.append( (val, key) )

email_counts.sort(reverse=True)

x = email_counts[0]
y = x[1]
print(y)
