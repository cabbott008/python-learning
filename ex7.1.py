file = input('Enter a file name:')
try:
    fhand = open(file)
except:
    print('Please enter the correct file name:')
    quit()
for line in fhand:
    line = line.upper()
    line = line.rstrip()
    print(line)
