weight=float(input("Enter your weight please! :"))
unit = input("Is your weight is in kilograms or pounds? (K/P)")

if unit=="K":
    weight=weight*2.205
    unit="L"

elif unit=="P" :
    weight=weight/2.205
    unit="Kgs"

else :
    print ("Invalid weight")

print(f"Your weight is {weight} {unit}")
