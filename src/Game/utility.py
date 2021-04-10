def sum_cards(card_list):
    sum_value, num_of_ace = 0, 0
    for i in card_list:
        if i.face_value == 'A':
            sum_value += 11
            num_of_ace += 1
        elif i.face_value in ['J', 'Q', 'K']:
            sum_value += 10
        else:
            sum_value += int(i.face_value)

    # Adjust Ace Value
    if sum_value > 21 and num_of_ace > 0:
        sum_value -= (10 * num_of_ace)

    return sum_value


def game_winner(winner=None, push=False):
    print_asterisk = '#####################'
    if push:
        winner.push_money()
        return "{}\nThe winner - {}!!\n{}".format(print_asterisk, "PUSH", print_asterisk)
    else:
        winner_type = winner.__class__.__name__
        if winner_type.upper() == "PLAYER":
            winner.game_money()
        return "{}\nThe winner - {}!!\n{}".format(print_asterisk, winner_type, print_asterisk)


def get_yes_or_no_ans(question, option1='Y', option2='N'):
    while True:
        get_answer = input(question)
        if get_answer.upper() in [option1, option2]:
            if get_answer.upper() == option1:
                return option1
            else:
                return option2
        else:
            print("Please enter [{}] or [{}]! ".format(option1, option2))
            continue
