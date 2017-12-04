import sys


def checksum(rows):
    result = 0

    for row in rows:
        values = [int(value) for value in row.split()]
        result += max(values) - min(values)
   
    return result


if __name__ == '__main__':
    lines = []
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as input_fd:
            lines = [line.strip() for line in input_fd.readlines()]
    else:
        lines = [line.strip() for line in sys.stdin.readlines()]
    
    for line in lines:
        print(line)

    print()
    print(checksum(lines))
