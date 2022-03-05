from board import Board

class State:
  def __init__(self, board=None):
    if board is None:
      self.b = Board()

  def serialize(self):
    pass

  def deserialize(self):
    pass

  def actions(self):
    pass

  def value(self):
    # TODO: take the number of remaining empty squares and add 1
    # then multiply it by 1 or -1 depending on the winner (or 0 if draw)
    pass

