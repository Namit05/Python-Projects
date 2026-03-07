import random
import art
import game_data


def retry():
    do_over = input("Do you want to play again?(Y/N) :").lower()
    if do_over == "y":
        game()
    else:
        print("Thanks for playing!")


def game():
    print(art.logo)
    game_over = False
    score = 0

    random_celeb1 = random.randint(0, 49)
    random_celeb2 = random.randint(0, 49)
    while random_celeb1 == random_celeb2:
        random_celeb2 = random.randint(0, 49)
    while game_over == False:
        celeb_compare_1 = game_data.data[random_celeb1]["follower_count"]
        celeb_compare_2 = game_data.data[random_celeb2]["follower_count"]
        print(
            f"Compare A:{game_data.data[random_celeb1]['name']}, a {game_data.data[random_celeb1]['description']}, from {game_data.data[random_celeb1]['country']}"
        )
        print(art.vs)
        print(
            f"from b:{game_data.data[random_celeb2]['name']}, a {game_data.data[random_celeb2]['description']}, from {game_data.data[random_celeb2]['country']}"
        )

        guess = input("Who has more followers? Type 'A' or 'B' :").lower()
        if guess == "a" and (celeb_compare_1 > celeb_compare_2):
            score += 1
            print(f"You're Right! Current Score :{score}")
            random_celeb2 = random.randint(0, 49)
        elif guess == "b" and (celeb_compare_1 < celeb_compare_2):
            score += 1
            print(f"You're Right! Current Score :{score}")
            random_celeb1 = random_celeb2
            random_celeb2 = random.randint(0, 49)
        else:
            print(f"Sorry! That's Wrong, FinalScore :{score}")
            game_over = True
            retry()


game()
