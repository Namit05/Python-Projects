unit=input("Is this temprature in farenheit or Celcius(C/F)")
temp=float(input("Enter The Temprature !! :"))
if unit =="C":
    temp= round((9*temp)/5+32 , 1)
    print(f"The temprature is in Farenheit :{temp}")

elif unit=="F":
    temp=round((temp-32)*5/9 ,1)
    print(f"The temprature is in celcius :{temp}")

else:
    print(f"{unit} is invalid")