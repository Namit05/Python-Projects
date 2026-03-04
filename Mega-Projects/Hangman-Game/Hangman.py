import random
from hangman_words import word_list
from hangman_images import images
from hangman_logo import logo

chosen_word = random.choice(word_list)
lives = 6
blank = ""
guessed_letters = []
print(logo)
for i in chosen_word:
    blank += "_ "
print(blank)
game_over = False
correct_letters = []
while game_over == False:
    print(f"**************YOU HAVE {lives} LIVES LEFT**************")
    guess = input("Guess a Letter :").lower()

    if guess not in guessed_letters:
        guessed_letters.append(guess)
    else:
        print("*******This letter has already been guessed*******")

    if guess not in chosen_word :
        print(f"{guess} is not in the chosen word!")
    display = ""

    for char in chosen_word:
        if char == guess:
            display += char
            correct_letters.append(guess)
        elif char in correct_letters:
            display += char
        else:
            display += "_ "
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("You lost!")
            game_over = True

    print("Word to guess :" + display)
    print(images[lives])
    if "_" not in display:
        game_over = True
        print("Yay you won!")
