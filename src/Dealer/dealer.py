from random import randint
from Card.card import Card
from Human.human import Human


class Dealer(Human):
    played_cards = []
    card_num = 0

    def __init__(self, name):
        super().__init__()
        self.dealer_name = name

    def get_dealer_name(self):
        return self.dealer_name

    def deal_card(self, phase=None, player=None):
        if phase == 'initial':
            for i in range(0, 4):
                card_suit, card_value = get_card()

                num = Dealer.card_num + 1
                globals()['c{}'.format(num)] = Card(card_suit, card_value)
                if i % 2 == 0:
                    player.set_hand(globals()['c{}'.format(num)])
                else:
                    self.set_hand(globals()['c{}'.format(num)])
        else:
            num = Dealer.card_num + 1
            card_suit, card_value = get_card()
            globals()['c{}'.format(num)] = Card(card_suit, card_value)
            player.set_hand(globals()['c{}'.format(num)])

    def get_hand(self, phase=None):
        if phase == 'initial':
            return "| {} of {} | X of X |".\
                format(self.card_hand[0].face_value, Dealer.suit_name[self.card_hand[0].suit])
        else:
            print_hand = super().get_hand()
            return print_hand


def get_card():
    face_value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['H', 'S', 'C', 'D']

    while True:
        card_value = face_value[randint(0, 12)]
        card_suit = suits[randint(0, 3)]
        if str(card_value) + card_suit in Dealer.played_cards:
            continue
        else:
            Dealer.played_cards.append(str(card_value) + card_suit)
            break

    return card_suit, card_value
