from Cell import Cell
import random

class Board:

  def __init__(self):
    self.squares = [] 
    self.cells = []
    a = Cell()
    for i in range(16):
      self.squares.append(' ')
      self.cells.append(a.clone())

  def print_board(self):
    print("|" + '-' * 7 + "|")

    for row in range(4):
      for square in range(4):

        print('|' + self.squares[square * 4 + row], end='')
      print('|')
    print("|" + '-' * 7 + "|")
    
    
  def mark_square(self, square, range):
    square = int(square)
    if square > range or square < 0: 
      print ("invalid choice") 
      return 0
    if (self.cells[square - 1].isBomb()) == True:
      symbol = 'X' 
    elif (self.cells[square - 1].isBomb()) == False: 
      symbol = "o"
    else: 
      return 0
    self.squares[square - 1] = symbol 
    return 1

  def set_bomb(self): 
    temp = random.randint(0,15)
    self.cells[temp].SetBomb()
    if self.cells[temp].SetBomb():
      return 1
    return 0

  def Check_loss_condition(self, square):
    square = int(square)
    if (self.cells[square - 1].isBomb()) == True:
      return 1
    else:
      return 0
    
