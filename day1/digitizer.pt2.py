import sys


def digitize(digits):
    counts = []
    step_size = len(digits) // 2
    
    for i in range(len(digits)):
        if digits[i] == digits[(i + step_size) % len(digits)]:
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
