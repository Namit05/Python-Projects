questions=("How many Elements are there in the preiodic table? :",
           "Which animal lays the largest egg? :",
           "Which is the most abundant gas in the atmosphere ? :",
           "How many bones are in the human body? :",
           "Which is the hottest planet in the solar system? :")

options=(("A. 116","B. 117","C. 118","D. 122"),
         ("A. Whale","B. Crocodile","C. Ostrich","D. Penguin"),
         ("A. Nitrogen","B. Oxygen","C. Helium","D. Hydrogen"),
         ("A. 206","B. 207","C. 208 ","D. 209"),
         ("A. Mercury","B. Venus ","C. Earth","D. Mars"))

answers=("C","C","A","A","B")
guesses=[]
score=0
question_num=0

for question in questions:
    print("------------")
    print(question)
    for option in options[question_num]:
        print(option)


    guess=input("Enter (A,B,C,D):").upper()
    guesses.append(guess)
    if guess ==answers[question_num]:
        score+=1
        print("Correct!")

    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer")
    question_num+=1

print("-------------")
print("    RESULTS   ")
print("-------------")

print("answers: ",end="")
for answer in answers:
    print(answer,end="")
print()

print("guesses: ",end="")
for guess in guesses:
    print(guess,end="")
print()

score=int(score/len(questions)*100)
print(f"Your score is {score}%")