__author__ = 'barnett'
def FibonacciSequence(n):
    sequence_max = n
    sequence_numA = 1
    sequence_numB = 0
    sequence_sum = 1
    while sequence_sum < sequence_max:
        sequence_numA = sequence_sum
        sequence_numB += sequence_numA
        sequence_sum = sequence_numA + sequence_numB
        print sequence_numA
        print sequence_numB
    print sequence_sum
    return