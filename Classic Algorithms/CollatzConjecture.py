__author__ = 'barnett'
def CollatzConjecture(n):
    steps = 0
    while n > 1:
        steps += 1
        if n % 2 == 0:
            n = n/2
        else:
            n = (n*3)+1
    print steps
    return