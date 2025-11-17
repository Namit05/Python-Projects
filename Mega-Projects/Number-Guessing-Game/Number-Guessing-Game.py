import random

low_num=1
high_num=100
answer=random.randint(low_num,high_num)
guesses=0
is_running=True

print("-----NUMBER GUESSING GAME-----")
print(f"select a number between {low_num} and {high_num} ")

while is_running :

    guess=input("enter your guess :")

    if guess.isdigit():
        guess=int(guess)
        guesses+=1

        if guess <low_num or guess >high_num :
            print("That number is out of range")
            print(f"select a number between {low_num} and {high_num} ")
        elif guess<answer :
                         print("Too low try again")

        elif guess>answer :
            print("Too high try again")

                
        else :
         print("Correct")
         print(f"Number of guesses {guesses}")
        


    else:
        print("Invalid guess")
        print(f"select a number between {low_num} and {high_num} ")