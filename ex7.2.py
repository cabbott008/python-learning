file = input('Enter a file name:')
try:
    fhand = open(file)
except:
    print('Please enter the correct file name:')
    quit()
count = 0
tally = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        line = line[20:]
        count = count + 1
        line = float(line)
        tally = tally + line
        print(line)

print('Total count:', count)
print('Total tally:', tally)
print('Average spam confidence:', tally/count)
