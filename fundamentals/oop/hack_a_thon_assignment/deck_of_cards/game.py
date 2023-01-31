from classes.deck import Deck

def game_round(player_1, player_2):
    player_1_card = Deck.deal_card()
    player_2_card = Deck.deal_card()
    if player_1_card == player_2_card:
        print('Draw!')
    elif player_1_card > player_2_card:
        print(f'{player_1} Wins!')
    else:
        print(f'{player_2} Wins!')


game_round('Drake', 'Josh')