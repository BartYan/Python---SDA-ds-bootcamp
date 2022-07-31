import unittest

from gra_w_wojne import determine_the_winner


class TestWinningCard(unittest.TestCase):

    def test_the_winner(self):
        card_1 = "8"
        card_2 = "J"
        winner = determine_the_winner(card_1, card_2)

        self.assertEqual(winner, 2)

    def test_the_winner2(self):
        card_1 = "J"
        card_2 = "8"
        winner = determine_the_winner(card_1, card_2)

        self.assertEqual(winner, 1)
