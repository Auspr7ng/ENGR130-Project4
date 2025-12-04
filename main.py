from read_board import read_board
from get_liberty import get_liberty


def main():
    filename = 'inputs/test3'

    # Read the board
    game = read_board(filename)
    if game is None:
        return

    # Find max liberty
    max_liberty = 0
    for y in range(game.size):
        for x in range(game.size):
            if game.board[y][x] != '*':
                liberty = get_liberty(game, x, y)
                if liberty > max_liberty:
                    max_liberty = liberty
    
    # Print max liberty
    print(f"The biggist liberty in this broad is {max_liberty}")
    
    return 0


if __name__ == "__main__":
    main()
