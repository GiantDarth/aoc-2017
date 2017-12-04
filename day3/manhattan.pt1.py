import sys
import math
import cmath
from collections import deque


def manhattan_dist(src, dest = (0, 0)):
    return sum(abs(a - b) for a, b in zip(src, dest))


def inverse_coords(value):
    # Make it 1-based intead of 0-based
    value -= 1
    p = math.floor(math.sqrt(4 * value + 1))
    q = value - ((p**2) // 4)

    z = (q * 1j**p) + (((p + 2) // 4) - ((p + 1) // 4) * 1j) * 1j**(p - 1)
    z *= -1j

    # Return the real & imaginary components as a x-y tuple
    return (round(z.real), round(z.imag))


if __name__ == '__main__':
    input = []
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as input_fd:
            input = [line.strip() for line in input_fd.readlines()]
    else:
        input = [line.strip() for line in sys.stdin.readlines()]
    
    for line in input:
        coords = inverse_coords(int(line))
        print(line, coords, manhattan_dist(coords))