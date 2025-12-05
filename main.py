from read_board import read_board
from get_liberty import get_liberty


def main():
    filename = 'inputs/test3'

    # Read the board
    game = read_board(filename)
    if game is None:
        return

    # Find max liberty
    # Find max liberty for Black and White
    max_liberty_B = 0
    max_liberty_W = 1
    
    for y in range(game.size):
        for x in range(game.size):
            if game.board[y][x] != '*':
                liberty = get_liberty(game, x, y)
                if game.board[y][x] == 'B':
                    if liberty > max_liberty_B:
                        max_liberty_B = liberty
                elif game.board[y][x] == 'W':
                    if liberty > max_liberty_W:
                        max_liberty_W = liberty
    
    print(f"Max liberty for Black: {max_liberty_B}")
    print(f"Max liberty for White: {max_liberty_W}")
    
    if max_liberty_B > max_liberty_W:
        print("Black is more likely to win")
    elif max_liberty_W > max_liberty_B:
        print("White is more likely to win")
    else:
        print("Both are equally likely to win")
    
    return 0

if __name__ == "__main__":
    main()
