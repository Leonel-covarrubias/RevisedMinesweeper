import unittest
from Board import Board
from Cell import Cell


def main():
  
  userChoice = 0 
  turn = 0
  
  print("MINESWEEPER")
  print("Options: 1-16")
  print("Enter 0 to Exit")
  board = Board()
  board.set_bomb()
  board.print_board()
  
  

  while userChoice != "0": 
    turn +=1
    userChoice = input("Make selection: ")
    if board.mark_square(userChoice,16) == 0: 
      continue
    board.print_board()
    if board.Check_loss_condition(userChoice) == 1:
      print ("You lose!!")
      return 0
    if turn == 15: 
      print('You Win!!')
      return 0
    
    
    

if __name__ == "__main__":
  main()
