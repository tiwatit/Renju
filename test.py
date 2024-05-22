BOARD_SIZE = 19
EMPTY_CELL = 0

def check_line(board, row, col, drow, dcol, color):
  """Checks a line in a given direction for a sequence of a specific color.

  Args:
      board: A 2D list representing the game board.
      row: The starting row index.
      col: The starting column index.
      drow: The row direction (1 for down, -1 for up).
      dcol: The column direction (1 for right, -1 for left).
      color: The color to check for.

  Returns:
      The length of the sequence if found, otherwise 0.
  """
  count = 1
  for i in range(1, 5):
    next_row = row + i * drow
    next_col = col + i * dcol
    if 0 <= next_row < BOARD_SIZE and 0 <= next_col < BOARD_SIZE and board[next_row][next_col] == color:
      count += 1
    else:
      break
  return count

def check_horizontal(board, row, col, color):
  """Checks the horizontal line for a sequence of a specific color."""
  return check_line(board, row, col, 0, 1, color)

def check_vertical(board, row, col, color):
  """Checks the vertical line for a sequence of a specific color."""
  return check_line(board, row, col, 1, 0, color)

def check_diagonal(board, row, col, color):
  """Checks both diagonals for a sequence of a specific color."""
  return max(check_line(board, row, col, 1, 1, color),
             check_line(board, row, col, 1, -1, color))

def check_five(board, row, col):
  """Checks if there is a sequence of five in any direction for a specific color."""
  color = board[row][col]
  if color == EMPTY_CELL:
    return False

  return any(check(board, row, col, color) == 5 for check in [check_horizontal, check_vertical, check_diagonal])

def check_winner(board):
  """Checks the board for a winner."""
  for row in range(BOARD_SIZE):
    for col in range(BOARD_SIZE):
      if check_five(board, row, col):
        return (1 if board[row][col] == 1 else 2), (row, col)
  return 0, None

def read_board(file):
  """Reads the game board from a file."""
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
  """Reads the input file, processes the test cases, and prints the results."""
  try:
    with open('data.txt', 'r') as file:
      boards = read_board(file)
      for board in boards:
        winner, win_pos = check_winner(board)
        print(winner)
        if winner != 0:
          print(win_pos[0] + 1, win_pos[1] + 1)
  except ValueError as e:
    print(e)

if __name__ == "__main__":
  main()