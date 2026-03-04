import random
import art


def blackjack():
    print(art.logo)

    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        card = random.choice(cards)
        return card

    def calculate_score(cards):
        if 11 in cards and 10 in cards and len(cards) == 2:
            return 0
        elif 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare(u_score, c_score):
        if u_score == c_score:
            return "Draw !"
        elif c_score == 0:
            return "Dealer's BlackJack! You Lost"
        elif u_score == 0:
            return "BlackJack! You Won!"
        elif u_score > 21:
            return "You lost"
        elif c_score > 21:
            return "You won"
        elif u_score > c_score:
            return "You won"
        else:
            return "You lost"

    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for x in range(2):
        computer_cards.append(deal_card())
        user_cards.append(deal_card())

    while is_game_over == False:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your Cards :{user_cards}, Your score :{user_score}")
        print(f"Computer Cards :{computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            draw_choice = input(
                "press 'y' to draw another card , 'n' to stand :"
            ).lower()
            if draw_choice == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Computer Cards :{computer_cards}, Computer Score :{computer_score}")
    print(compare(user_score, computer_score))
    restart = input(
        "Do you want to play again??? press 'y' for yes and 'n' for no :"
    ).lower()
    if restart == "y":
        blackjack()
    else:
        print("Thanks for playing!")


blackjack()
