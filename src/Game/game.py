from Player.player import Player
from Dealer.dealer import Dealer
from Game.utility import sum_cards, game_winner, get_yes_or_no_ans
import time

d1 = Dealer("Shark")


def game_setup():
    player_name = ''
    player_balance = 0
    
    while True:
        try:
            player_name = input("Please enter your name: ")
            player_balance = int(input("Please enter your balance: "))
            break
        except ValueError:
            print("Enter your balance in number!")
            continue

    p1 = Player(player_name.capitalize(), player_balance)

    print("Thank you for the details.\nYour dealer for the game will be: {}. \n"
          "The balance for {} is USD {}. "
          "Let us begin!".format(d1.get_dealer_name(), p1.player_name, p1.money_balance))

    start_game(p1)


def start_game(p1):
    sufficient_balance = None
    bet_amount = 0
    next_game = True

    while next_game:
        while True:
            try:
                while True:
                    bet_amount = int(input("Enter the bet amount: [$50, $100, $200, $500]: "))
                    if bet_amount not in [50, 100, 200, 500]:
                        print("Please enter a valid amount!! ")
                        continue
                    else:
                        adjust_bet = 'N'
                        sufficient_balance = p1.set_bet(bet_amount)

                        if sufficient_balance is None:
                            print("Your Balance: ", p1.money_balance)
                            adjust_bet = get_yes_or_no_ans("Would you like to adjust your bet? [Y/N]: ")
                        if adjust_bet == 'Y':
                            continue
                        else:
                            break
                break
            except ValueError:
                print("Enter the amount in numbers!")
                continue

        if sufficient_balance is None:
            print("Game terminated due to Insufficient Balance!!")
            return
        else:
            d1.clear_hand()
            p1.clear_hand()
            print("Bet amount $: {}".format(bet_amount))
            d1.set_bet(bet_amount)
            d1.deal_card('initial', p1)

            print("Dealer hand: {}".format(d1.get_hand('initial')))

            while True:
                time.sleep(1)
                player_card_value = sum_cards(p1.card_hand)
                print("Player hand: {} -- Value - {}".format(p1.get_hand(), sum_cards(p1.card_hand)))
                if player_card_value == 21:
                    print("$$BLACKJACK$$")
                    break
                elif player_card_value > 21:
                    print("Player - BUST!")
                    break
                else:
                    hit_or_stand = get_yes_or_no_ans("Hit or Stand? [H/S]: ", 'H', 'S')
                    if hit_or_stand.upper() == 'H':
                        d1.deal_card(player=p1)
                    else:
                        break

            print("Player hand: {} -- Value - {}".format(p1.get_hand(), sum_cards(p1.card_hand)))

            while True:
                time.sleep(1)
                dealer_card_value = sum_cards(d1.card_hand)
                print("Dealer hand: {} -- Value - {}".format(d1.get_hand(), dealer_card_value))
                if dealer_card_value <= 16:
                    d1.deal_card(player=d1)
                else:
                    break

            dealer_card_value = sum_cards(d1.card_hand)
            if dealer_card_value > 21:
                time.sleep(1)
                # print("Dealer hand: {} -- Value - {}".format(d1.get_hand(), dealer_card_value))
                print("Dealer - BUST!")
                if player_card_value > 21:
                    print(game_winner(d1))
                else:
                    print(game_winner(p1))
            else:
                time.sleep(1)
                # print("Dealer hand: {} -- Value - {}".format(d1.get_hand(), dealer_card_value))
                if player_card_value > 21:
                    print(game_winner(d1))
                elif player_card_value > dealer_card_value:
                    print(game_winner(p1))
                elif player_card_value == dealer_card_value:
                    print(game_winner(p1, True))
                else:
                    print(game_winner(d1))

            print("Player Balance: ", p1.money_balance)

        play_another = get_yes_or_no_ans("Would you like to place a new bet? [Y/N]: ")
        if play_another == 'Y':
            continue
        else:
            next_game = False
        # play_another = input("Would you like to place a new bet? [Y/N]: ")
        # if play_another.upper() in ['Y', 'N']:
        #     if play_another.upper() == 'Y':
        #         break
        #     else:
        #         next_game = False
        #         break
        # else:
        #     print("Please enter [Y] for Yes or [N] for No! ")
        #     continue

    print("Thank you for playing BlackJack!! Hope to see you soon!!")
