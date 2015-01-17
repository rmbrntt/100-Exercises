__author__ = 'ryan@barnett.io'
import math


def prime_factorization(n):
    prime_list = []
    num_list = []
    for num in range(2, int(math.sqrt(n))+2):
        if n % num == 0:
            for nums in range(1, num+1):
                if num % nums == 0:
                    num_list.extend([nums])
            if len(num_list) == 2:
                prime_list.extend([num])
            num_list = []
    if prime_list > 0:
        return 'Prime factors:', prime_list
    else:
        return 'Already Prime'

print prime_factorization(25)