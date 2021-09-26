BLUE = '\u001b[44m'
GREEN = '\u001b[42m'
YELLOW = '\u001b[43m'
RED = '\u001b[41m'
DEFAULT = '\u001b[0m'

def print_map(matrix, x, y, i, j):
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
    for i_p in range(y):
        for j_p in range(x):
            color = DEFAULT
            if matrix[i_p][j_p] == -1:
                color = RED
            elif matrix[i_p][j_p] == 0:
                color = BLUE
            elif matrix[i_p][j_p] == 1:
                color = GREEN
            if i_p == i and j_p == j:
                color = YELLOW
            print(color + "  " + DEFAULT, end="")
        print()