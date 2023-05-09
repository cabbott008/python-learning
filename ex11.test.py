import re
# searcher = input('Please enter RegEx: ')
x = open('regex2.txt')
count = 0
totals = 0
lst = None

for line in x:
    line = line.strip()
    lst = re.findall('([0-9]+)', line)
    if len(lst) > 0:
        totals = totals + float(lst[0])
        count += 1
print(totals)
print(count)
