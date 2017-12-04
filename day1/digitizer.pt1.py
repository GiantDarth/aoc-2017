import itertools
import sys


def rotate(l, n):
    return l[-n:] + l[:-n]


def digitize(digits):
    counts = []

    for i in range(len(digits)):
        if digits[i] == digits[(i + 1) % len(digits)]:
            counts.append(int(digits[i]))

    return counts

if __name__ == '__main__':
    input = []
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as input_fd:
            input = [line.strip() for line in input_fd.readlines()]
    else:
        input = [line.strip() for line in sys.stdin.readlines()]
    
    for line in input:
        counts = digitize(line)
        print(line, sum(counts))
