class Legolas:
    MAX_DEPTH = 4
    def __init__(self, color):
        self.color = color

    import random        

    def play(self, board):
        ret = self.minimax(self.MAX_DEPTH, -float("inf"), +float("inf"), board, self.color)
        #print ret[1]
        return ret[0]

    def minimax(self, depth, alpha, beta, board, playerColor):
        bestMove = 0
        if (playerColor == self.color): #max player
            #print "max: ", playerColor
            if depth == 0:
                return [None, self.getScore(board)]
            moves = board.valid_moves(playerColor)
            if (len(moves) == 0):
                if (len(board.valid_moves(board._opponent(playerColor))) == 0):
                    return [None, self.getScore(board)]
                return self.minimax(depth - 1, alpha, beta, board, board._opponent(playerColor))
            
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
                return [None, self.getScore(board)]
            moves = board.valid_moves(playerColor)
            if (len(moves) == 0):
                if (len(board.valid_moves(board._opponent(playerColor))) == 0):
                    return [None, self.getScore(board)]
                return self.minimax(depth - 1, alpha, beta, board, board._opponent(playerColor))
            
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

    def getScore(self, board):
        totalScore = 0
        totalScore += 25 * ((self.getPlayerScore(board) - self.getOpponentScore(board)) / float((self.getPlayerScore(board) + self.getOpponentScore(board))))

        playerValidMoves = board.valid_moves(self.color)
        opponentValidMoves = board.valid_moves(board._opponent(self.color))
        if (len(playerValidMoves) + len(opponentValidMoves) != 0):
            totalScore += 50 * ((len(playerValidMoves) - len(opponentValidMoves)) / float((len(playerValidMoves) + len(opponentValidMoves))))

        playerCorners = self.getNOfCorners(board, self.color)
        opponentCorners = self.getNOfCorners(board, board._opponent(self.color))
        if (playerCorners + opponentCorners != 0):
            totalScore += 30 * ((playerCorners - opponentCorners)/float((playerCorners + opponentCorners)))

        #print totalScore
        return totalScore


    def getPlayerScore(self, board):
        if (self.color == board.WHITE):
            return board.score()[0]
        else:
            return board.score()[1]
            
    def getOpponentScore(self, board):
        if (self.color == board.WHITE):
            return board.score()[1]
        else:
            return board.score()[0]

    def getNOfCorners(self, board, color):
        nOfCorners = 0
        if (board.board[1][1] == self.color):
            nOfCorners += 1
        if (board.board[1][8] == self.color):
            nOfCorners += 1
        if (board.board[8][1] == self.color):
            nOfCorners += 1
        if (board.board[8][8] == self.color):
            nOfCorners += 1
        return nOfCorners
