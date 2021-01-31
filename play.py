#!/usr/bin/env python3
from board import Board

b = Board()
b.initialize_board()


while not b.check_win(1) and not b.check_win(2) and not b.check_tie():
  b.get_board()
  print("Player1 give x, y of the tile you want to occupy: ")
  x1 = int(input("x: "))
  y1 = int(input("y: "))
  b.place_cross(x1, y1)

  b.get_board()
  print("Player2 give x, y of the tile you want to occupy: ")
  x2 = int(input("x: "))
  y2 = int(input("y: "))
  b.place_circle(x2, y2)

b.get_board()

