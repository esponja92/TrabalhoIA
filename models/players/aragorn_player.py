class Aragorn:
	def __init__(self, color):
		self.color = color

	import random

	def play(self, board):
		return self.bestPlay(board)

	def bestPlay(self, board):
		moves = board.valid_moves(self.color)
		myscore = 0
		bestMove = moves[0]
		for move in moves:
			myboard = board.get_clone()
			myboard.play(move, self.color)
			if (self.color == myboard.WHITE):
				if (myboard.score()[0] > myscore):
					myscore = myboard.score()[0]
					bestMove = move
			elif (self.color == myboard.BLACK):
				if (myboard.score()[1] > myscore):
					myscore = myboard.score()[1]
					bestMove = move
		return bestMove


