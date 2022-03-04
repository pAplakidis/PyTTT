#!/usr/bin/env python3
from board import Board

if __name__ == '__main__':
  b = Board()

  # TODO: build a better game loop
  b.print_board()
  while True:
    b.print_board()
    print("Player1 give x, y of the tile you want to occupy: ")
    x1 = int(input("x: "))
    y1 = int(input("y: "))
    b.place_cross(x1, y1)

    if b.check() == 0:
      pass
    else:
      break

    b.print_board()
    print("Player2 give x, y of the tile you want to occupy: ")
    x2 = int(input("x: "))
    y2 = int(input("y: "))
    b.place_circle(x2, y2)

    if b.check() == 0:
      pass
    else:
      break

  b.print_board()

