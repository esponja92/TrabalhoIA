class Aragorn:
	def __init__(self, color):
		self.color = color
	import random

	def getNearestCorner(self, moves):
		import math
		corners = [[1,1],[1,8], [8,1], [8,8]]
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

	def play(self, board):
		return self.bestPlay(board)

	def bestPlay(self, board):
		moves = board.valid_moves(self.color)
		best_moves = []
		myscore = 0
		for move in moves:
			myboard = board.get_clone()
			myboard.play(move, self.color)
			if (self.color == myboard.WHITE):
				if (myboard.score()[0] > myscore):
					myscore = myboard.score()[0]
					best_moves = [move]
				elif (myboard.score()[0] == myscore):
					best_moves.append(move)
			elif (self.color == myboard.BLACK):
				if (myboard.score()[1] > myscore):
					myscore = myboard.score()[1]
					best_moves = [move]
				elif (myboard.score()[1] == myscore):
					best_moves.append(move)
		if(len(best_moves) == 1):
			return best_moves[0]
			"""
			best_moves eh uma lista de moves, nesse caso best_moves so tem 1 elemento, entao eu retorno ele pegando o primeiro elemento de best_moves
			"""
		else:
			return self.getNearestCorner(best_moves)

