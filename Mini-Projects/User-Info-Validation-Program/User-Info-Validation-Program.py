#Username no more than 12 characters
#No space or digits

username=input("Enter a username :")
if len(username) > 12:
    print("Your username cant be more than 12 characters")
elif not username.find(" ")==-1 :
    print("Your username cant contain spaces")
elif not username.isalpha():
    print("Your username cant have digits")
else:
    [print(f"Welcome!{username}")]