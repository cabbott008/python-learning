score = input("Enter Score: ")

fs = float(score)
if fs < 0.0 or fs > 1.0:
    print('Please enter a score between 0.0 and 1.0')
elif fs >= 0.9:
    print('A')
elif fs >= 0.8:
    print('B')
elif fs >= 0.7:
    print('C')
elif fs >= 0.6:
    print('D')
elif fs < 0.6:
    print('F')
