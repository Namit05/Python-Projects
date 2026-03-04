import random
rock=("""
      Rock!
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper=("""
       Paper!
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors=("""
          Scissor
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


choice=[rock,paper,scissors]
user_choice=int(input("What do you want tc choose?(Type 0 for rock , 1 for paper , 2 for scissors) :"))
if user_choice>=0 and user_choice<=2 :
    print("You chose :")
    print(choice[user_choice])

computer_choice=random.randint(0,2)
print("Computer chose :")
print(choice[computer_choice])

if user_choice>2 or user_choice<0 :
    print("Invalid Number chosen , You lost!")
elif user_choice==0 and computer_choice==2 :
    print("You win!")

elif computer_choice==0 and user_choice==2 :
    print("You lose!")

elif user_choice>computer_choice :
    print("You win!")

elif user_choice<computer_choice:
    print("You lose!")

elif user_choice==computer_choice :
    print("Its a Draw!")
