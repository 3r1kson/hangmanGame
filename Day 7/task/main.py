import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

# guess = input("Guess a letter: ").lower()

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
errors_available = 6
display = []
display_word = []
for i in range(0, len(chosen_word)):
    display.append("_")

for i in chosen_word:
    display_word.append(i)

def checkAlreadUserd(guess_letter):
    for i in bag_used_letters:
        if i == guess_letter:
            return False
    return True

def checkIfLetterExists(guess_letter):
    if guess_letter not in chosen_word:
        return False
    return True

bag_used_letters = []
while errors_available > 0:
    guess = input("Guess a letter: ").lower()
    if checkAlreadUserd(guess):
        if checkIfLetterExists(guess):
            bag_used_letters.append(guess)
            for i in range(0, len(chosen_word)):
                if chosen_word[i] == guess:
                    display[i] = guess
        else:
            if errors_available > 0:
                bag_used_letters.append(guess)
                errors_available -= 1
    else:
        print(f"\n You've already used the letter '{guess}'. ")

    print(f"{stages[errors_available]}.")

    print(f"Used letters: {bag_used_letters} \n ")
    print(display)

    print()

    if "_" not in display:
        print("Congratulations, you finished the game")
        break

    if errors_available == 0:
        print("Game over!")
        print(f"Correct word '{chosen_word}'")









