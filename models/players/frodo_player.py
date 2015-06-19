class FrodoPlayer:
  def __init__(self, color):
    self.color = color

  def play(self, board):
    return self.getNearestCorner(board.valid_moves(self.color))

  def getNearestCorner(self, moves):
    import math
    corners = [[1,1],[2,2], [3,3], [4,4], [5,5], [6,6], [7,7], [8,8],[1,8],[2,7], [3,6], [4,5], [5,4], [6,3], [7,2], [8,1]]
    minDist = 10
    retMove = None
    for move in moves:
      for corner in corners:
        distX = abs(corner[0] - move.x)
        distY = abs(corner[1] - move.y)
        dist  = math.sqrt(distX*distX + distY*distY)
        if dist < minDist:
          minDist = dist
          retMove = move

    return retMove
