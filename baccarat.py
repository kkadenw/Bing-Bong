import random

CARDS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
VALUE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]
OUTCOME = ['Player wins', 'Banker wins', 'Tie']

def compute_score(hand):
    """Compute the score of a hand"""
    total_value = 0
    for card in hand:
        total_value += VALUE[CARDS.index(card)]
    return total_value % 10
