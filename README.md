# Go Game Liberty Calculator

This program calculates the maximum liberty of any stone group on a Go board.

## Description

The program reads a Go board configuration from an input file, identifies connected groups of stones, calculates the liberties for each group, and finds the maximum liberty value among all groups.

## Files

- `main.py`: The main entry point of the program. It reads the board, iterates through all stones, calculates their liberties, prints the maximum liberty found for both Black and White, and predicts the winner based on who has the higher maximum liberty.
- `read_board.py`: Contains the `read_board` function which reads the board size and layout from a file and returns a `GoGame` object. It also validates that the board dimensions (rows and columns) match the specified size.
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
4.  The program will output the maximum liberty found for each player and predict the winner.

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
9
*********
*********
***B*****
*********
*******W*
*********
**WWW****
*********
********B
```

Output:
```
Max liberty for Black: 4
Max liberty for White: 8
White is more likely to win
```
