BLUE = '\u001b[44m'
GREEN = '\u001b[42m'
YELLOW = '\u001b[43m'
RED = '\u001b[41m'
DEFAULT = '\u001b[0m'

def print_map(matrix, i, j, x, y) -> None:
    """
    Prints the map with current, visited and unvisited positions.

    Parameters:
        matrix (list): 2D array
        i (int): coordinate of current position on y-axis
        j (int): coordinate of current position on x-axis
        x (int): width of the matrix
        y (int): height of the matrix
    """
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

    output = ""
    color = DEFAULT
    for k in range(y):
        for l in range(x):
            if matrix[k][l] == -1:
                color = RED
            elif matrix[k][l] == 0:
                color = BLUE
            elif matrix[k][l] == 1:
                color = GREEN
            if k == i and l == j:
                color = YELLOW
            output += color + "  " + DEFAULT
        output += "\n"
    print(output)
