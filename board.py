class Board:
  def __init__(self, board=[[0 for i in range(3)] for i in range(3)]):
    self.board = board
    self.winner = None

  def get_board(self):
    for x in self.board:
      print(x)
    print()
    return self.board

  # 0: empty, 1: cross, 2: circle
  def initialize_board(self):
    for i in range(len(self.board)):
      self.board[i] = 0

  def place_cross(self, x, y):
    if self.board[x][y] == 0:
      self.board[x][y] = 1
    else:
      return None
    return self

  def place_circle(self, x, y):
    if self.board[x][y] == 0:
      self.board[x][y] = 2
    else:
      return None
    return self

  def check_win(self, player):
    # if player = 1 check if crosses win, else if 2 check circles
    # TODO: check all horizontals
    # TODO: check all verticals
    # TODO: check both diagonals
    return None

  def check_tie(self):
    for x in self.board:
      if x == 0:
        return False
    if self.winner is None:
      print("[+] It's a tie!")
      return True
"""
b = Board()
b.get_board()
b.place_cross(1, 1)
b.get_board()
b.place_circle(2, 2)
b.get_board()
"""

