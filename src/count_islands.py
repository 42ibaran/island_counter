import sys
import argparse
from src.exceptions import *

STEP_RANGE = range(-1, 2, 1)

def bfs(matrix, i, j, x, y, queue=[]):
    """
    BFS traversal checks if neighboring cells are land and adds them
    to exploration queue, then recursively visits elements in the queue.
    """
    matrix[i][j] = -1
    for i_step in STEP_RANGE:
        for j_step in STEP_RANGE:
            next_i = i + i_step
            next_j = j + j_step
            if i_step == j_step == 0 or \
                    next_i < 0 or next_i >= y or \
                    next_j < 0 or next_j >= x:
                continue
            if matrix[next_i][next_j] == 1 and (next_i, next_j) not in queue:
                queue.append((next_i, next_j))
    while len(queue) > 0:
        i, j = queue.pop()
        bfs(matrix, i, j, x, y, queue)


def count_islands(matrix) -> int:
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
                bfs(matrix, i, j, x, y)
    return count


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str)
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
        count = count_islands(matrix)
        print(count)
    except Exception as e:
        print(e, file=sys.stderr)
        exit(1)

    