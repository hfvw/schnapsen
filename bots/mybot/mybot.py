"""
Mybot - Always play the highest ranked card and follow suit.
"""

# Import the API objects
from api import State, util
from api import Deck


class Bot:

	def __init__(self):
		pass

	def get_move(self, state):
		# type: (State) -> tuple[int, int]
		"""
		Function that gets called every turn. This is where to implement the strategies.
		Be sure to make a legal move. Illegal moves, like giving an index of a card you
		don't own or proposing an illegal mariage, will lose you the game.
		TODO: add some more explanation
		:param State state: An object representing the gamestate. This includes a link to
			the states of all the cards, the trick and the points.
		:return: A tuple of integers or a tuple of an integer and None,
			indicating a move; the first indicates the card played in the trick, the second a
			potential spouse.
		"""
		# All legal moves
		moves = state.moves()
		chosen_move = moves[0]

		if state.get_phase() == 2:
			chosen_move = moves[len(moves) - 1]

		# If the opponent has played a card
		if state.get_opponents_played_card() is not None:
			moves_same_suit = []

			# Get all moves of the same suit as the opponent's played card
			for index, move in enumerate(moves):
				if move[0] is not None and Deck.get_suit(move[0]) == Deck.get_suit(state.get_opponents_played_card()):
					moves_same_suit.append(move)

			# Play the cheapest card in phase two if you cant beat the trick, else play the highest card
			if len(moves_same_suit) > 0:
				if state.get_phase() == 2 and (state.get_opponents_played_card() % 5 < moves_same_suit[0][0]):
					return moves_same_suit[len(moves_same_suit) - 1]
				chosen_move = moves_same_suit[0]
				return chosen_move

		return chosen_move
