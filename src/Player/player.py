from Human.human import Human


class Player(Human):

    def __init__(self, name, amount):
        super().__init__()
        self.player_name = name
        self.money_balance = amount

    def set_bet(self, amount):
        if amount <= self.money_balance:
            self.money_balance -= amount
            Human.bet_amount = amount
            return True
        else:
            return None

    def game_money(self):
        self.money_balance += (Human.bet_amount * 2)

    def push_money(self):
        self.money_balance += Human.bet_amount

    def __str__(self):
        return "Player Name: {} - Balance: {}".format(self.player_name, self.money_balance)
