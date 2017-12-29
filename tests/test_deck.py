from unittest import TestCase
from api import Deck

class TestDeck(TestCase):

    def test_generate(self):
        d = Deck.generate()

        stock = d.getCardState().count("Stock")
        self.assertEqual(stock,10,"The value should be 10")

        player1 = d.getCardState().count("P1Hand")
        self.assertEqual(player1, 5,"The value should be 5")

        player2 = d.getCardState().count("P2Hand")
        self.assertEqual(player2, 5,"The value should be 5")