import re
x = open('mbox.txt')
count = 0
for line in x:
    line = line.strip()
    lst = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(lst) > 0:
    y = re.findall('^From .* ([0-9][0-9]):', line)
    if len(y) > 0:
        count += 1
        print(y)
print(count)