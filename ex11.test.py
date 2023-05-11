import re
# searcher = input('Please enter RegEx: ')
x = open('regex2.txt')
#totals = 0

#for line in x:
#    line = line.strip()
#    line = re.findall('([0-9]+)', line)
#    for word in line:
#        if len(word) > 0:
#            totals = totals +int(word)
#print(totals)

print( sum( [int(i) for i in re.findall('[0-9]+', x.read())]))

#lst = re.findall('[0-9]+', x.read())
#ilst = [int(i) for i in lst]
#print(sum(ilst))