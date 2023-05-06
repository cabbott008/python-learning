sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)
if fh <= 40 :
    pay = fh * fr
if fh > 40 :
    pp = 40 * fr
    op = (fh - 40) * (fr * 1.5)
    pay = pp + op
print('Pay:',pay)
