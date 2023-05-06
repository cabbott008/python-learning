fhand = input('Enter file: ')
lines = open(fhand)
count = 0

for line in lines:
    if line.startswith('From '):
        line = line.split()
        line = line[1]
        count = count + 1
        print(line)

print('There were', count, 'lines in the file with From as the first word')
