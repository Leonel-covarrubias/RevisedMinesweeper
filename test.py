import unittest
from Board import Board
from Cell import Cell 

class Testgame(unittest.TestCase):

  #unit tests 
  
  def test_set_bomb_cell_class(self): 
    temp = Cell()
    self.assertEqual(1, temp.SetBomb())

  def test_is_Bomb_cell_true(self): 
    temp = Cell()
    temp.bombstatus = 1
    self.assertTrue(temp.isBomb())
    
  def test_is_Bomb_cell_false(self): 
    temp = Cell()
    self.assertFalse(temp.isBomb())
    
  def test_mark_square_Edge_case(self):
    board = Board()
    self.assertFalse(board.mark_square(55,12))

  #Integration tests 
  
  def test_mark_square_when_bomb(self):
    board = Board()
    board.cells[0].bombstatus = 1 
    self.assertTrue(board.mark_square(1,16))
    
  def test_mark_square_when_not_bomb(self): 
    board = Board() 
    self.assertTrue(board.mark_square(1,16))
    
  def test_set_bomb_board(self):
    board = Board()
    self.assertTrue(board.set_bomb())
    
  def test_check_loss_condition_True(self):
    board = Board()
    board.cells[0].bombstatus = 1 
    self.assertTrue(board.Check_loss_condition(1))
    
  def test_check_loss_condition_false(self):
    board = Board()
    self.assertFalse(board.Check_loss_condition(1))
