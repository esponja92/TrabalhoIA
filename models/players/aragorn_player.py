class Aragorn:
	def __init__(self, color):
		self.color = color
	import random

	def getNearestCorner(self, moves):
		import math
		corners = [[1,1],[1,8], [8,1], [8,8]]
		minDist = 100
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

	def minEnemy(self, moves, board):
		best_moves = []
		minScore = 100
		cor_oponente = board._opponent(self.color)
		moves_oponente = board.valid_moves(cor_oponente)
		for move in moves:
			myboard = board.get_clone()
			myboard.play(move, self.color)	#jogador faz a jogada
			for move_oponente in moves_oponente:
				myboard2 = myboard.get_clone()
				myboard2.play(move_oponente, cor_oponente)
				if (cor_oponente == myboard2.WHITE):
					if ((myboard2.score()[0] < minScore)):
						best_moves = [move]
						minScore = myboard2.score()[0]
					elif ((myboard2.score()[0] == minScore)):
						best_moves.append(move)
				elif (cor_oponente == myboard2.BLACK):
					if ((myboard2.score()[1] < minScore)):
						best_moves = [move]
						minScore = myboard2.score()[1]
					elif ((myboard2.score()[1] == minScore)):
						best_moves.append(move)
		if(len(best_moves) == 1):
			return best_moves[0]
		else:
			return self.getNearestCorner(best_moves)

	def maxPlayer(self, board):
		moves = board.valid_moves(self.color)
		best_moves = []
		maxScore = 0
		for move in moves:
			myboard = board.get_clone()
			myboard.play(move, self.color)
			if (self.color == myboard.WHITE):
				if ((myboard.score()[0] > maxScore)):
					maxScore = myboard.score()[0]
					best_moves = [move]
				elif (myboard.score()[0] == maxScore):
					best_moves.append(move)
			elif (self.color == myboard.BLACK):
				if (myboard.score()[1] > maxScore):
					maxScore = myboard.score()[1]
					best_moves = [move]
				elif (myboard.score()[1] == maxScore):
					best_moves.append(move)
		if(len(best_moves) == 1):
			return best_moves[0]
			"""
			best_moves eh uma lista de moves, nesse caso best_moves so tem 1 elemento, entao eu retorno ele pegando o primeiro elemento de best_moves
			"""
		else:
			return self.minEnemy(best_moves, board)

	def play(self, board):
		return self.maxPlayer(board)
