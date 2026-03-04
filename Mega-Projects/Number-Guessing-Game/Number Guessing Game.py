import random

easy_lives = 10
hard_lives = 5


def check(choice, number, turns):
    if choice == number:
        print("You guessed it right !!!")
    elif choice > number:
        print("Too high")
        return turns - 1
    elif choice < number:
        print("Too Low")
        return turns - 1


def difficulty():
    lives = 0
    difficulty_choice = input("Choose your difficulty (Easy or Hard) :").lower
    if difficulty_choice == "easy":
        return easy_lives
    else:
        return hard_lives


def retry():
    do_over = input("Do you want to play again?(Y/N) :").lower()
    if do_over == "y":
        game()
    else:
        print("Thanks for playing!")


def game():

    answer = random.randint(1, 100)
    print("Welcome to Number Guessing Game")
    choice = 0
    turns = difficulty()
    while choice != answer:
        print(f"You have {turns} left to choose ur answer !")
        guess = int(input("Make a guess :"))
        turns = check(guess, answer, turns)
        if turns == 0:
            print(f"Game over! You ran out of lives the correct number was {answer}")
            return retry()
        elif guess != answer:
            print("Wrong answer Please Retry")


game()
