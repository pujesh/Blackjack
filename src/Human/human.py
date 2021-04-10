class Human:
    suit_name = {'H': 'Heart', 'S': 'Spade', 'C': 'Club', 'D': 'Diamond'}

    def __init__(self):
        self.card_hand = []
        self.bet_amount = 0

    def set_bet(self, amount):
        self.bet_amount = amount

    def set_hand(self, card):
        self.card_hand.append(card)

    def get_hand(self):
        print_hand = '|'
        for i in self.card_hand:
            print_hand += " {} of {} |".format(i.face_value, self.suit_name[i.suit])

        return print_hand

    def clear_hand(self):
        self.card_hand = []
