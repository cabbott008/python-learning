def computepay(h, r):
    h = float(h)
    r = float(r)
    if h <= 40 :
        pay = h * r
    if h > 40 :
        pp = 40 * r
        op = (h - 40) * (r * 1.5)
        pay = pp + op
    print('Pay:',pay)

computepay(45, 10.5)
