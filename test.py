BOARD_SIZE = 19
EMPTY_CELL = 0
WIN_NUMBER = 5
def check_line(board, row, col, drow, dcol, player):
    count = 1
    for i in range(1, 5):
        next_row = row + i * drow
        next_col = col + i * dcol
        if 0 <= next_row < BOARD_SIZE and 0 <= next_col < BOARD_SIZE and board[next_row][next_col] == player:
            count += 1
        else:
            break
    return count

def check_horizontal(board, row, col, player):
    return check_line(board, row, col, 0, 1, player)

def check_vertical(board, row, col, player):
    return check_line(board, row, col, 1, 0, player)

def check_diagonal(board, row, col, player):
    return max(check_line(board, row, col, 1, 1, player),
               check_line(board, row, col, 1, -1, player))

def check_win_condition(board, row, col):
    player = board[row][col]
    if player == EMPTY_CELL:
        return False
    return (check_horizontal(board, row, col, player) >= WIN_NUMBER or 
            check_vertical(board, row, col, player) >= WIN_NUMBER or 
            check_diagonal(board, row, col, player) >= WIN_NUMBER)

def check_winner(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if check_win_condition(board, row, col):
                return (1 if board[row][col] == 1 else 2), (row, col)
    return 0, None

def read_board(file):
    count = int(file.readline())
    if not (1 <= count <= 11):
        raise ValueError("Number of test cases is too high")

    boards = []
    for _ in range(count):
        board = []
        for _ in range(BOARD_SIZE):
            row = [int(num) for num in file.readline().strip()]
            board.append(row)
        boards.append(board)
    return boards

def main():
    try:
        with open('data.txt', 'r') as file:
            boards = read_board(file)
            for board in boards:
                winner, win_pos = check_winner(board)
                if winner != 0:
                    print(winner)
                    print(win_pos[0] + 1, win_pos[1] + 1)
                else:
                    print(0)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
