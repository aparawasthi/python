from random import shuffle
from player import Player

#
# The function is expected to return a list of 52 cards.
# The function accepts following parameters:
#  1. Boolean shuffled (Retruns a shuffled deck of cards)
#  
def create_deck(shuffled = False):
    deck = []
    face_cards = ["Ace", "Jack", "Queen", "King"]
    suits = ["club", "diamond", "heart", "spade"]
    for suit in suits:
        deck.append([suit,face_cards[0]])
        for number_card in range(2,11):
            deck.append([suit,str(number_card)])
        for face_card in face_cards[1:]:
            deck.append([suit,face_card])
    if shuffled:
        shuffle(deck)
    return deck

#
# The function prints the trick passed to it.
# The function accepts following parameters:
#  1. list trick (cards played by the players)
#  
def print_trick(trick):
    cards_symbol = {"heart" : chr(3), "diamond" : chr(4), "club" : chr(5), "spade" : chr(6)}
    print(chr(27) + "[2J")
    print("Card on table - [ ",end="")
    for card in trick:
        if not card == trick[-1]:
            print(f"{cards_symbol[card[0]]} {card[1]}",end=" | ")
        else:
            print(f"{cards_symbol[card[0]]} {card[1]}",end=" ]")
    print("\n")

#
# The function distributes 13 cards each to 4 players.
# The function accepts following parameters:
#  1. list deck (list of cards to be distributed among players)
#  2. Integers start (0 to 3 representing player 1 to player 4 respectively, represents player number from which card distribution should start)
#  
def distribute_cards(deck,start):
    for x in range(0,52,4):
        players[start-4].hand.append(deck[x])
        players[start+1-4].hand.append(deck[x+1])
        players[start+2-4].hand.append(deck[x+2])
        players[start+3-4].hand.append(deck[x+3])

def calculate_players_scores():
    round_winner = 0
    round_max = 0
    for player in players:
        player.calculate_score()
        if round_max < player.round_score:
            round_max = player.round_score
            round_winner = player.id
    return round_winner

def ask_bets():
    for player in players:
        player.print_hands()
        bet = ask_input(f"{player.name} please enter your bet ", True)
        player.set_bet(bet)
#
# The function check for the winning player in a trick
# The function accepts following parameters:
#  1. list trick
#
def check_winning_card(trick):
    card_value = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10,"Jack" : 11, "Queen" : 12, "King" : 13,"Ace" : 14}
    winner_player = 0
    max = 0
    has_spade = False
    if trick[0][0] != "spade":
        for x in range(4):
            if trick[x][0] == "spade" and card_value[trick[x][1]] > max:
                max = card_value[trick[x][1]]
                winner_player = trick[x][2]
                has_spade = True
        if has_spade:
            return winner_player
    for i in range(4):
        if trick[i][0] == trick[0][0] and card_value[trick[i][1]] > max:
            max = card_value[trick[i][1]]
            winner_player = trick[i][2]
    return winner_player

def ask_input(message,integer = False):
    while True:
        flag = True
        user_response = input("Type '--help' to read the rules of the game and instructions for how to play. You can type '--resume' to go back to the game.\n\n"+message)
        if user_response == "--help":
            flag = False
            with open("rules.txt") as rules:
                for rule in rules:
                    print(rule,end="")
                print("")
                rules.close()
            while True:
                user_res = input("You can enter '--resume' to go back to the game.")
                if user_res == "--resume":
                    break
        if integer:
            try:
                user_response = int(user_response)
                break
            except ValueError:
                print("Entered input is not a number please enter a number.")
            except Exception:
                print("Exception raised please enter the proper input")
            continue
        if flag:
            break
    return user_response

def reset_players():
    for pl in players:
        pl.reset()

def display_score():
    for pl in players:
        print(f"Name - {pl.name}\tRound Score - {pl.round_score}\tTotal Scorre - {pl.score}\tTricks - {len(pl.trick)}")

players = []
for player_number in range(4):
    player_name = ask_input(f"Enter player {player_number+1} name ")
    players.append(Player(player_number, player_name))

round = 5
start, turn = 0, 0
while round != 0:
    deck = create_deck(True)
    distribute_cards(deck,start)
    turn = start
    ask_bets()
    for x in range(13):
        trick = []
        for y in range(4):
            player = players[turn]
            player.print_hands()
            card_index = ask_input(f"{player.name}. Please select the index card you want to choose. ", True)
            card = player.hand.pop(card_index-1)
            card.append(player.id)
            trick.append(card)
            print_trick(trick)
            if turn == 3:
                turn = 0
            else:
                turn += 1
        turn = check_winning_card(trick)
        winner = players[turn]
        print(f"{winner.name} won this trick")
        winner.add_to_trick(trick)
    start = calculate_players_scores()
    display_score()
    reset_players()
    round -= 1