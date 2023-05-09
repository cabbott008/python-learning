import re
# searcher = input('Please enter RegEx: ')
x = open('mbox.txt')
count = 0
totals = 0
lst = None

for line in x:
    line = line.strip()
    lst = re.findall('New Revision: ([0-9.]+)', line)
    if len(lst) > 0:
        totals = totals + int(lst[0])
        count += 1
print(int(totals / count))
