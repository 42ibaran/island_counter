import sys
import time
import argparse
from src.exceptions import FileLoadingError
from src.visualization import print_map

STEP_RANGE = range(-1, 2, 1)

def bfs(matrix, x, y, queue, dump):
    """
    BFS traversal checks if neighboring cells are land and adds them
    to exploration queue, then visits elements in the queue until
    queue is empty.
    """
    while len(queue) > 0:
        i, j = queue.pop()
        matrix[i][j] = -1
        if dump:
            print_map(matrix, x, y, i, j)
            time.sleep(1)
        for i_step in STEP_RANGE:
            for j_step in STEP_RANGE:
                next_i = i + i_step
                next_j = j + j_step
                if i_step == j_step == 0 or \
                        next_i < 0 or next_i >= y or \
                        next_j < 0 or next_j >= x:
                    continue
                if matrix[next_i][next_j] == 1 and \
                        (next_i, next_j) not in queue:
                    queue.append((next_i, next_j))


def count_islands(matrix, visu) -> int:
    """
    Function to iterate through the map. In case it encounters unvisited land,
    it initiates BFS traversal.
    """
    count = 0
    x = len(matrix[0])
    y = len(matrix)
    for i in range(y):
        for j in range(x):
            if matrix[i][j] == 1:
                count += 1
                bfs(matrix, x, y, [(i, j)], visu)
    return count


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str)
    parser.add_argument("-v", action='store_true',
                        help="display algorithm visualization")
    return parser.parse_args()


def load_file(filename):
    matrix = []
    try:
        with open(filename, "r") as file:
            for line in file:
                matrix.append([int(char) for char in line if char != '\n'])
    except ValueError:
        raise ValueError("Map file contains invalid characters.")
    except FileNotFoundError:
        raise FileLoadingError("Map file doesn't exist.")
    except:
        raise FileLoadingError("Couldn't open map file.")
    
    if any(any(value != 0 and value != 1 for value in row) for row in matrix):
        raise ValueError("Map file contains invalid characters.")
    
    if len(matrix) == 0:
        raise ValueError("Map cannot be empty.")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("Map contains uneven rows.")

    return matrix


if __name__ == '__main__':
    try:
        args = parse_arguments()
        matrix = load_file(args.filename)
        count = count_islands(matrix, args.v)
        print(count)
    except Exception as e:
        print(e, file=sys.stderr)
        exit(1)

    