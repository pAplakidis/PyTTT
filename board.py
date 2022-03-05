import numpy as np

class Board:
  def __init__(self, board=[[0 for i in range(3)] for i in range(3)]):
    self.board = board
    self.winner = None

  # for debugging
  def get_board(self):
    for x in self.board:
      print(x)
    print()
    return self.board

  # prettier way of printing the board
  def print_board(self):
    print(self.board)
    for row in self.board:
      for x in row:
        if x == 0:
          print("| |", end="")
        elif x == 1:
          print("|x|", end="")
        elif x == 2:
          print("|o|", end="")
      print()

  # 0: empty, 1: cross, 2: circle
  def reset_board(self):
    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        self.board[i][j] = 0

  def move(self, x, y, p):
    x -= 1
    y -= 1
    if x < 0 or x > 2 or y < 0 or y > 2:
      return None
    
    if self.board[x][y] == 0:
      if p == 1:
        self.board[x][y] = 1
      elif p == 2:
        self.board[x][y] = 2
    else:
      return None
    return self

  # 1: crosses win, 2: circles win
  def check_win(self):
    # check all horizontals
    for row in self.board:
      if row == [1, 1, 1]:
        return 1
      elif row == [2, 2, 2]:
        return 2

    # check all verticals
    tmp = np.array(self.board)
    for i in range(len(self.board)):
      if np.array_equal(tmp[:, i], [1, 1, 1]):
        return 1
      elif np.array_equal(tmp[:, i], [2, 2, 2]):
        return 2

    # check right diagonal
    tmp = []
    for i in range(len(self.board)):
      tmp.append(self.board[i][i])
    if tmp == [1, 1, 1]:
      return 1
    elif tmp == [2, 2, 2]:
      return 2

    # check left diagonal
    tmp = []
    bd = np.flip(np.array(self.board), axis=1)
    for i in range(len(bd)):
      tmp.append(bd[i][i])
    if tmp == [1, 1, 1]:
      return 1
    elif tmp == [2, 2, 2]:
      return 2

    return 0

  def check(self):
    full = True
    for row in self.board:
      if 0 in row:
        full = False
        break

    if not full:
      if self.check_win() == 1:
        print("[+] Cross wins")
        return 1
      elif self.check_win() == 2:
        print("[+] Cross wins")
        return 2
    else:
      if self.check_win() == 0:
        print("[+] It's a tie")
        return 3

    return 0

