import sys
import math
import cmath
from itertools import product

def gen_sum_spiral(threshold):
    MAX = 500
    spiral = [[0] * MAX for _ in range(MAX)]
    offset = MAX // 2

    spiral[offset][offset] = 1

    for value in range(2, threshold + 1):
        coords = inverse_coords(value)

        total = 0
        for i, j in product(range(-1, 2), range(-1, 2)):
            if i != 0 or j != 0:
                x = coords[0] + offset + i
                y = coords[1] + offset + j

                if x < len(spiral) and y >= 0 and x < len(spiral[x]) and y >= 0:
                    total += spiral[x][y]

        if total > threshold:
            return total
        else:
            spiral[coords[0] + offset][coords[1] + offset] = total

        print(value, coords, (coords[0] + offset, coords[1] + offset), spiral[coords[0] + offset][coords[1] + offset])

    return 1


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
        print(line, gen_sum_spiral(int(line)))