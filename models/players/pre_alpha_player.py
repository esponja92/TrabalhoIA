class PreAlphaPlayer:
  def __init__(self, color):
    self.color = color
    self.weight = [ 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0,
                    0, 120, -20,  20,   5,   5,  20, -20, 120, 0,
                    0, -20, -40,  -5,  -5,  -5,  -5, -40, -20, 0,
                    0, 20,  -5,  15,   3,   3,  15,  -5,  20, 0,
                    0, 5,  -5,   3,   3,   3,   3,  -5,   5, 0,
                    0, 5,  -5,   3,   3,   3,   3,  -5,   5, 0,
                    0, 20,  -5,  15,   3,   3,  15,  -5,  20, 0,
                    0, -20, -40,  -5,  -5,  -5,  -5, -40, -20, 0,
                    0, 120, -20,  20,   5,   5,  20, -20, 120, 0,
                    0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0
                  ]
    self.knownBoards = {}

  def play(self, board):
    return self.minimax(board)

  def minimax(self, board):
    maxTime = 29.99
    #startTime = time.clock()
    move = self.max_value(board, 4, -float('inf'), float('inf'), 0, maxTime)[1]
    #print "Total elapsed time: ", time.clock() - startTime
    return move

  def max_value(self, board, depth, alpha, beta, startTime, maxTime):
    moves = board.valid_moves(self.color)
    if depth == 0:
      return self.get_score_weight(board), None
    if moves.__len__() == 0:
      if board.valid_moves(board._opponent(self.color)).__len__() == 0:
        return self.get_score_weight(board), None
      return self.min_value(board, depth-1, alpha, beta, startTime, maxTime)
    ret_move = moves[0]
    for move in moves:
      if alpha >= beta:
        break
      #elapsedTime = (time.clock() - startTime)
      #if elapsedTime >= maxTime:
        #break
      test_board = board.get_clone()
      test_board.play(move, self.color)
      v = self.min_value(test_board, depth-1, alpha, beta, startTime, maxTime)[0]
      if v > alpha:
        alpha = v
        ret_move = move
    return alpha, ret_move

  def min_value(self, board, depth, alpha, beta, startTime, maxTime):
    moves = board.valid_moves(board._opponent(self.color))
    if depth == 0:
      return self.get_score_weight(board), None
    if moves.__len__() == 0:
      if board.valid_moves(self.color).__len__() == 0:
        return self.get_score_weight(board), None
      return self.max_value(board, depth-1, alpha, beta, startTime, maxTime)
    ret_move = moves[0]
    for move in moves:
      if alpha >= beta:
        break
      #elapsedTime = (time.clock() - startTime)
      #if elapsedTime >= maxTime:
        #break
      test_board = board.get_clone()
      test_board.play(move, board._opponent(self.color))
      v = self.max_value(test_board, depth-1, alpha, beta, startTime, maxTime)[0]
      if v < beta:
        beta = v
        ret_move = move
    return beta, ret_move



  def get_score_weight(self, board):
    corners = [[1,1],[1,8],[8,1],[8,8]]  
    corners_adjacent_1 = [[1,2], [2,2], [2,1]] 
    corners_adjacent_2 = [[1,7], [2,7], [2,8]]
    corners_adjacent_3 = [[7,1], [7,2], [8,2]] 
    corners_adjacent_4 = [[8,7], [7,7], [7,8]] 
    self_pieces = 0
    opponent_pieces = 0
    self_pieces_corners = 0
    opponent_pieces_corners = 0
    self_pieces_near_corners = 0
    opponent_pieces_near_corners = 0
    self_valid_moves = 0
    opponet_valid_moves = 0
    p_factor = 0
    c_factor = 0
    ca_factor = 0
    mo_factor = 0
    weight_factor = 0

    self_valid_moves = board.valid_moves(self.color).__len__()
    opponet_valid_moves = board.valid_moves(board._opponent(self.color)).__len__()
    
    if self_valid_moves > opponet_valid_moves: 
      mo_factor = 100*(self_valid_moves/(self_valid_moves + opponet_valid_moves))
    elif self_valid_moves < opponet_valid_moves:
      mo_factor = -100*(opponet_valid_moves/(self_valid_moves + opponet_valid_moves))
    else:
      mo_factor = 0

    for sq in board._squares():
        if board.get_square_color(sq/10, sq%10) == self.color:
          self_pieces += 1
          weight_factor += self.weight[sq]
          if [sq/10, sq%10] in corners:
            self_pieces_corners += 1
          elif [sq/10, sq%10] in corners_adjacent_1 and board.get_square_color(1, 1) == '.':
            self_pieces_near_corners += 1
          elif [sq/10, sq%10] in corners_adjacent_2 and board.get_square_color(1, 8) == '.':
            self_pieces_near_corners += 1
          elif [sq/10, sq%10] in corners_adjacent_3 and board.get_square_color(8, 1) == '.':
            self_pieces_near_corners += 1
          elif [sq/10, sq%10] in corners_adjacent_4 and board.get_square_color(8, 8) == '.':
            self_pieces_near_corners += 1
        elif board.get_square_color(sq/10, sq%10) == board._opponent(self.color):
          opponent_pieces += 1
          weight_factor -= self.weight[sq]
          if [sq/10, sq%10] in corners:
            opponent_pieces_corners += 1
          elif [sq/10, sq%10] in corners_adjacent_1 and board.get_square_color(1, 1) == '.':
            opponent_pieces_near_corners += 1
          elif [sq/10, sq%10] in corners_adjacent_2 and board.get_square_color(1, 8) == '.':
            opponent_pieces_near_corners += 1
          elif [sq/10, sq%10] in corners_adjacent_3 and board.get_square_color(8, 1) == '.':
            opponent_pieces_near_corners += 1
          elif [sq/10, sq%10] in corners_adjacent_4 and board.get_square_color(8, 8) == '.':
            opponent_pieces_near_corners += 1
    
    c_factor = 75*self_pieces_corners - 75*opponent_pieces_corners
    ca_factor = -50*self_pieces_near_corners + 50*opponent_pieces_near_corners

    if self_pieces > opponent_pieces:
      p_factor = 100*(self_pieces/(self_pieces + opponent_pieces))
    elif self_pieces < opponent_pieces:
      p_factor = -100*(opponent_pieces/(self_pieces + opponent_pieces))
    else:
      p_factor = 0

    total = p_factor + c_factor + ca_factor + mo_factor + weight_factor
    return total

  def print_moves(self, board, color):
    for move in board.valid_moves(color):
      print str(move.x) + " " + str(move.y)
