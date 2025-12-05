# Go Game Liberty Calculator

This program calculates the maximum liberty of any stone group on a Go board.

## Description

The program reads a Go board configuration from an input file, identifies connected groups of stones, calculates the liberties for each group, and finds the maximum liberty value among all groups.

## Files

- `main.py`: The main entry point of the program. It reads the board, iterates through all stones, calculates their liberties, and prints the maximum liberty found.
- `read_board.py`: Contains the `read_board` function which reads the board size and layout from a file and returns a `GoGame` object.
- `go_game.py`: Defines the `GoGame` class which stores the board size and the board grid.
- `get_liberty.py`: Contains the `get_liberty` function which calculates the number of liberties for a stone at a given position.
- `label.py`: Contains the `label` function, a recursive helper used by `get_liberty` to identify connected stones and their liberties.

## Usage

1.  Ensure you have Python installed.
2.  The input file is hardcoded as `inputs/test3` in `main.py`. You can modify `main.py` to change the input file.
3.  Run the program:
    ```bash
    python3 main.py
    ```
4.  The program will output the maximum liberty found on the board.

## Input Format

The input file should be formatted as follows:
- The first line contains an integer representing the board size (N).
- The following N lines represent the board rows.
- Each row contains N characters.
- `*` represents an empty intersection.
- Other characters (e.g., `1`, `2`, `B`, `W`) represent stones.

## Example

Input (`inputs/test3`):
```
5
**1**
*111*
**1**
*****
*****
```

Output:
```
The biggist liberty in this broad is 8
```
