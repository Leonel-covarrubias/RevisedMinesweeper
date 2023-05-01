class Cell:

  def __init__(self):
    self.bombstatus = 0

  def SetBomb(self):
    self.bombstatus = 1
    return self.bombstatus

  def isBomb(self):
    return self.bombstatus

  def clone(self):
    return Cell()
