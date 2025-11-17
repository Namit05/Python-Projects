operator=input("Enter your input (+ - * /) :")
num1=float(input("Enter your number! :"))
num2=float(input("Enter your number! :"))
if operator=="+" :
    print(num1+num2)
elif operator=="-" :
    print(num1-num2)
elif operator =="*" :
    print(num1*num2)
elif operator =="/" :
    print (num1/num2)
else :
    print ("Operator invalid please retry!")