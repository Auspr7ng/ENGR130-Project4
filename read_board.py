from go_game import GoGame

def read_board(filename):
    """Read board from file and create a GoGame structure"""
    try:
        with open(filename, 'r') as file:
            first_line = file.readline().strip()
            if not first_line.isdigit():
                print("Error: The first line of the file must be a board size (integer).")
                return None

            size = int(first_line)
            board = []

            for i in range(size):
                row = list(file.readline().strip())

                # Error Check: row length must match board size
                if len(row) != size:
                    print(f"Error: Row {i} does not match expected board size {size}.")
                    return None

                board.append(row)

            return GoGame(size, board)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
