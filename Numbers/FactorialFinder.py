__author__ = 'barnett'
'''
def factorial(n):
    i = n
    if n < 1:
        return 1
    while n > 1:
        n -= 1
        i = n * i
    return i
'''
#refactored factorial(n) for efficiency
def factorial(n):
    result = 1
    while n >= 1:
        result = result * n
        n -= 1
    return result


