def label(game, x, y, label_liberty, label_stone, color):
    n = game.size
    
    # Check bounds
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    
    # Check if already labeled
    if label_liberty[y][x] == 1 or label_stone[y][x] == 1:
        return
    
    if game.board[y][x] == color:
        label_stone[y][x] = 1
        label(game, x + 1, y, label_liberty, label_stone, color)
        label(game, x - 1, y, label_liberty, label_stone, color)
        label(game, x, y + 1, label_liberty, label_stone, color)
        label(game, x, y - 1, label_liberty, label_stone, color)
    elif game.board[y][x] == '*':
        label_liberty[y][x] = 1
