from hearts.hearts import Card
from hearts.hearts import Hand
from hearts.hearts import Player
from hearts.hearts import Round
from hearts.hearts import Trick


def players(names='Lauren,Erin,Jeremy,Daniel'):
    return [Player(x) for x in names.split(',')]


def new_round(players):
    return Round(players=players)


def hand(cards='Ah,7d,6h,2s'):
    return Hand([Card.deserialize(c) for c in cards.split(',')])


def trick(players, cards='5h,3h,Jh,Qs'):
    return Trick([(p, Card.deserialize(c)) for (p, c) in zip(players, cards)])


'''
def play_full_round():
    # randomize the hand
    while round_is_not_over:
        player = get_next_player()
        for card in player.hand:
            try:
                round.play_card(card)
            except:
                pass
'''
