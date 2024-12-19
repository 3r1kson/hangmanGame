import random

import art

def blackjack():
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ")
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    deck_control = cards.copy()
    user_cards = []
    computer_cards = []

    user_card1 = random.choice(deck_control)
    user_cards.append(user_card1)
    deck_control.remove(user_card1)
    user_card2 = random.choice(deck_control)
    user_cards.append(user_card2)
    deck_control.remove(user_card2)

    user_total = sum(user_cards)

    computer_card1 = random.choice(deck_control)
    deck_control.remove(computer_card1)
    computer_cards.append(computer_card1)
    computer_total = sum(computer_cards)

    def getNewCard():
        new_one = 0
        new_one = random.choice(deck_control)
        user_cards.append(new_one)
        deck_control.remove(new_one)

    def getNewCardComputer():
        new_one = 0
        new_one = random.choice(deck_control)
        computer_cards.append(new_one)
        deck_control.remove(new_one)
        print(computer_cards)

    def printInitialData():
        print(f"Your cards: {user_cards}, current score: {user_total}")
        print(f"Computer's first card: {computer_cards}")

    def gameOverFlooded():
        printInitialData()
        print(f"Your final hand: {user_cards}, current score: {user_total}")
        print(f"Computer's final hand: {computer_cards}")
        print("You went over. You lose 😭")
        blackjack()

    def gameFinalResult():
        print(f"Your final hand: {user_cards}, current score: {user_total}")
        print(f"Computer's final hand: {computer_cards}, final score {computer_total}")
        if user_total > computer_total:
            print("You win 😃")
        elif user_total < computer_total and computer_total < 22:
            print("You lose 😤")
        elif computer_total > 21:
            print("Opponent went over. You win 😁")
        else:
            print("It's a draw! 🤝")
        blackjack()

    if want_to_play == 'y':
        print(art.logo)
        printInitialData()
        check_new = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        while check_new == 'y':
            getNewCard()
            user_total = sum(user_cards)
            if user_total > 21:
                gameOverFlooded()
                break
            printInitialData()
            check_new = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if check_new == 'n':
            getNewCardComputer()
            computer_total = sum(computer_cards)
            print(computer_total <16 and computer_total < 22)
            while computer_total < 16:
                getNewCardComputer()
                computer_total = sum(computer_cards)


        gameFinalResult()

    else:
        blackjack()

blackjack()