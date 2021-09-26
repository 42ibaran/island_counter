# Island counter
A program to count number of islands.

## Functionality
Given a file containing a matrix of numbers, where 1 represents land and 0 represents water, the program uses BFS to count the number of islands. Example:
```
000000000
010000000
111000100
110001110
000001100
001000000
110000000
000001100
```
This map contains 4 islands (pieces of land can be connected diagonally).

## Setup
### Locally
You can run the project locally. Make sure you have python installed. The project was tested with python v3.9, other versions might work as well. First, install the project module:
```
pip3 install .
```

To install dependencies run: 
```
pip3 install -r requirements.txt
```
These packages are used for tests and map generation script.

### With Docker
You can also use the project with Docker. First, build the image:
```
docker build -t island_counter .
```
Then, you can run the container like so:
```
docker run -it --rm island_counter
```

### With VSCode
There is `.devcontainer` directory with a setup for development using VSCode Remote Development extension. You can reopen the project directory using the extension, similarly to using Docker container but with more functionality.

## Usage
To run the script run:
```
./count_islands.sh [-v] MAP_FILENAME
```
`-v` option allows you to visualize the search algorithm.
 
There are test maps in `tests/maps`
You can also generate new map by running:
```
./generate_map.sh [-x X] [-y Y] [filename]
```
Map generation has been tried with 10000x10000 matrix.
