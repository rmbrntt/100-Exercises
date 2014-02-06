__author__ = 'barnett'
#refactored factorial(n) for efficiency
def factorial(n):
    result = 1
    while n >= 1:
        result = result * n
        n -= 1
    return result


