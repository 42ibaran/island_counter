import sys
import argparse
import numpy as np

ISLAND_P = 0.3

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, nargs='?', default='map.txt')
    parser.add_argument("-x", type=int, default=10)
    parser.add_argument("-y", type=int, default=10)
    return parser.parse_args()

if __name__ == '__main__':
    try:
        args = parse_arguments()
    except Exception as e:
        print(e, file=sys.stderr)
        exit(1)

    gen = np.random.default_rng()
    matrix = np.random.choice([0, 1], size=(args.y, args.x),
                              p=[1-ISLAND_P, ISLAND_P])
    map = '\n'.join([''.join(map(str, row)) for row in matrix])

    try:
        with open(args.filename, "w") as file:
            file.write(map)
    except Exception as e:
        print(e, file=sys.stderr)
        exit(1)