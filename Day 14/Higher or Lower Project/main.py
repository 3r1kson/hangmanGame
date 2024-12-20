import random

import art
import game_data

game_over = False
points = 0

randomA = random.choice(game_data.data)
while not game_over:
    print(art.logo)
    randomA = random.choice(game_data.data)
    randomB = random.choice(game_data.data)

    if points > 0:
        print(f"You're right! Current score: {points}.")

    if randomA != randomB:
        print(f"Compare A: {randomA['name']}, {randomA['description']}, from {randomA['country']}")
        print(art.vs)
        print(f"Compare B: {randomB['name']}, {randomB['description']}, from {randomB['country']}")
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if choice == 'a':
            if int(randomA['follower_count']) > int(randomB['follower_count']):
                points += 1
            else:
                game_over = True
        else:
            if int(randomA['follower_count']) < int(randomB['follower_count']):
                points += 1
            else:
                game_over = True



print(art.logo)
print(f"Sorry, that's wrong. Final score: {points}")