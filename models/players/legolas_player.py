class Legolas:
    MAX_DEPTH = 4
    def __init__(self, color):
        self.color = color

    import random        

    def play(self, board):
        return self.minimax(self.MAX_DEPTH, -float("inf"), +float("inf"), board, self.color)[0]

    def minimax(self, depth, alpha, beta, board, playerColor):
        bestMove = 0
        if (playerColor == self.color): #max player
            #print "max: ", playerColor
            if depth == 0:
                if (playerColor == board.WHITE):
                    return [None, board.score()[0]]
                else:
                    return [None, board.score()[1]]
            moves = board.valid_moves(playerColor)
            if (len(moves) == 0):
                if (playerColor == board.WHITE):
                    return [None, board.score()[0]]
                else:
                    return [None, board.score()[1]]
            
            maxScore = -float("inf")
            for move in moves:
                newBoard = board.get_clone()
                newBoard.play(move, playerColor)
                newValue = self.minimax(depth - 1, alpha, beta, newBoard, board._opponent(playerColor))[1]
                if (maxScore < newValue):
                    maxScore = newValue
                    bestMove = move
                if (alpha < newValue):
                    alpha = newValue
                if (beta <= alpha):
                    break
            return [bestMove, alpha]
        else: #min player
            #print "min: ", playerColor
            if depth == 0:
                if (playerColor == board.WHITE):
                    return [None, board.score()[0]]
                else:
                    return [None, board.score()[1]]
            moves = board.valid_moves(playerColor)
            if (len(moves) == 0):
                if (playerColor == board.WHITE):
                    return [None, board.score()[0]]
                else:
                    return [None, board.score()[1]]
            
            minScore = float("inf")
            for move in moves:
                newBoard = board.get_clone()
                newBoard.play(move, playerColor)
                newValue = self.minimax(depth - 1, alpha, beta, newBoard, board._opponent(playerColor))[1]
                if (minScore > newValue):
                    minScore = newValue
                    bestMove = move
                if (beta > newValue):
                    beta = newValue
                if (beta <= alpha):
                    break
            return [bestMove, beta]
