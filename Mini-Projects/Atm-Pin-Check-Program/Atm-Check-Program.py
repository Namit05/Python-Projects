correct_pin="1234"
attempts=0

while attempts<3:
    user_pin=input("Enter your pin to use the machine ! :")
    if user_pin == correct_pin :
        print("Access granted!")
        break

    else :
        attempts+=1
        print(f"Invalid pin try again!attempts left :{3 - attempts}")

if attempts==3:
    print("TRY AGAIN LATER !!!!")
