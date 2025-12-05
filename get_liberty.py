from label import label

def get_liberty(game, x, y):
    n = game.size
    color = game.board[y][x]
    
    # Create label arrays initialized to 0
    label_liberty = [[0 for _ in range(n)] for _ in range(n)]
    label_stone = [[0 for _ in range(n)] for _ in range(n)]
    
    # Label the group and liberties
    label(game, x, y, label_liberty, label_stone, color)
    
    # Count liberties
    count = 0
    for i in range(n):
        for j in range(n):
            if label_liberty[i][j] == 1:
                count += 1
    
    return count
