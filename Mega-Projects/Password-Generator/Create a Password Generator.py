import random

# Easy
letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "=", "-"]
pass_stuff = [letters, numbers, symbols]


print("Welcome to the Py Password Generator!")
pass_letters = int(input("How many letters would you like?\n :"))
pass_numbers = int(input("How many numbers would you like?\n :"))
pass_symbols = int(input("How many symbols would you like?\n :"))
password_list = []

for char in range(1, pass_letters + 1):
    letter = random.choice(letters)
    password_list.append (letter)
for char in range(1, pass_numbers + 1):
    number = random.choice(numbers)
    password_list.append(number)
for char in range(1, pass_symbols + 1):
    symbol = random.choice(symbols)
    password_list.append(symbol)
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your password is {password}")
