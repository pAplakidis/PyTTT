#!/usr/bin/env python3
from board import Board

def main_loop(b):
  idx = 0
  while True:
    b.print_board()
    print("Player%d give x, y of the tile you want to occupy: " % ((idx%2)+1))
    x = int(input("x: "))
    y = int(input("y: "))

    if idx % 2 == 0:
      if not b.move(x, y, 1):
        print("[-] Illegal Move")
        exit(1)
    else:
      if not b.move(x, y, 2):
        print("[-] Illegal Move")
        exit(1)

    if b.check() == 0:
      pass
    else:
      break
    idx += 1


if __name__ == '__main__':
  b = Board()
  main_loop(b)
  b.print_board()

