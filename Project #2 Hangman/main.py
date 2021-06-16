from random import choice

ALLOWED_TURNS = 7
right = []
wrong = []
game_over = False

def draw_hangman(turn):
    if turn == ALLOWED_TURNS:
        print("      ---------")
        print("       |")
        print("       |")
        print("       |")
        print("       |")
        print("       |")
        print("-----------------")
    elif turn == ALLOWED_TURNS-1:
        print("      ---------")
        print("       |     |")
        print("       |     O")
        print("       |")
        print("       |")
        print("       |")
        print("-----------------")
    elif turn == ALLOWED_TURNS-2:
        print("      ---------")
        print("       |     |")
        print("       |     O")
        print("       |     |")
        print("       |")
        print("       |")
        print("-----------------")
    elif turn == ALLOWED_TURNS-3:
        print("      ---------")
        print("       |     |")
        print("       |     O")
        print("       |    /|")
        print("       |")
        print("       |")
        print("-----------------")
    elif turn == ALLOWED_TURNS-4:
        print("      ---------")
        print("       |     |")
        print("       |     O")
        print("       |    /|\\")
        print("       |")
        print("       |")
        print("-----------------")
    elif turn == ALLOWED_TURNS-5:
        print("      ---------")
        print("       |     |")
        print("       |     O")
        print("       |    /|\\")
        print("       |     |")
        print("       |")
        print("-----------------")
    elif turn == ALLOWED_TURNS-6:
        print("      ---------")
        print("       |     |")
        print("       |     O")
        print("       |    /|\\")
        print("       |     |")
        print("       |    /")
        print("-----------------")
    elif turn == ALLOWED_TURNS-7:
        print("      ---------")
        print("       |     |")
        print("       |     O")
        print("       |    /|\\")
        print("       |     |")
        print("       |    / \\")
        print("-----------------")

def draw_letter_space(word, turn):
    global game_over
    game_over = True
    print(chr(27) + "[2J")
    print("Guess the word!!!\n")
    for letter in word:
        if letter in right:
            print(letter.upper(), end=" ")
        else:
            print("_", end=" ")
            game_over = False
    print(f"\n\nWrong Choices -> {wrong}\n")
    draw_hangman(turn)

def check_word(word):
    word = word.lower()
    turn = ALLOWED_TURNS
    global game_over
    draw_letter_space(word,turn)
    while not game_over:
        guess = input("Enter the letter\n")
        if guess in word:
            right.append(guess.lower())
            draw_letter_space(word,turn)
        else:
            if guess.lower() not in wrong:
                wrong.append(guess.lower())
                turn -= 1
            else:
                print("You have already guessed this letter")
            draw_letter_space(word,turn)
            if turn == 0:
                game_over = True
                print(f"\nSorry you have lost the game. The word was {word}")
    if turn != 0:
        print(f"You have guessed the word correctly. It's {word}")

    
mode = input("Enter the mode you want to play the game\nA -> 1 Player\nB -> 2 Player\n")
if mode.lower() == "a":
    with open("words.txt") as file:
        list_words = file.readlines()
        word = choice(list_words)[:-1]
        check_word(word)
elif mode.lower() == "b":
    word = input("Player 1 enter the word to play the game\n")
    check_word(word)
else:
    print("You have entered wrong choice")
