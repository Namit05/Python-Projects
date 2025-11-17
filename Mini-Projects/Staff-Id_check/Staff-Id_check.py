role=("admin","staff")
username=input(f"Enter your role :")
if len (username) >5 :
    print("Role cant be bigger than 5 characters")
elif not username.find(" ")==-1 :
    print("Role cant have space! ")
elif not username.isalpha() :
    print ("Role cant have digits!")
elif username not in role :
    print("Invalid role!")
else :
    print(f"Welcome {username}")

    name=input("Enter your Name :").lower()
    if username=="admin" :
        print(f"Welcome Admin {name}")
        if name=="namit" :
            print("Your Clearence level is level 3")
        
        else :
            print("Your Clearence level is level 2")
    
    elif username=="staff" :
        print(f"Welcome Staff {name}")
        print("Your clearence level is level 1")
    
    while username=="admin" :

        while name=="namit" :
            print("What area are you trying to access?")
            print("1.Main Control System")
            print("2.Security System")
            print("3.Operations System")
            print("4.Chemical Facility")
            print("5.EXIT")
            

            choice=int(input("Enter a choice 1-4 :"))

            if choice==1 :
                print("You may proceed to the main controls!")
                
            elif choice==2 :
                print("You may proceed to the security systems!")
                
            elif choice==3 :
                print("You may proceed to the operation table!")
                
            elif choice==4 :
                print("You may proceed to the chemical facility!")
            
            elif choice==5 :
                print("EXITING")
                break
            else :
                ("INVALID CHOICE!")


            
    while not name=="namit" :
            print("What area are you trying to access?")
            print("1.Main Control System")
            print("2.Security System")
            print("3.Operations System")
            print("4.Chemical Facility")
            print("5.EXIT")

            choice=int(input("Enter a choice 1-4 :"))

            if choice==1 :
                print("Sorry you require access level 3!")
               
            elif choice==2 :
                print("Sorry you require access level 3!")
               
            elif choice==3 :
                print("You may proceed to the operation table!")
                
            elif choice==4 :
                print("You may proceed to the chemical facility!")
            elif choice==5 :
                print("EXITING")
                break
            else :
                ("INVALID CHOICE!")

                

            
    
    while username=="staff" :
            print("What area are you trying to access?")
            print("1.Main Control System")
            print("2.Security System")
            print("3.Operations System")
            print("4.Chemical Facility")
            print("5.EXIT")

            choice=int(input("Enter a choice 1-4 :"))

            if choice==1 :
                print("Sorry you require access level 3!")
                
            elif choice==2 :
                print("Sorry you require access level 3!")
                
            elif choice==3 :
                print("Sorry you require access level 2 or above!")
              
            elif choice==4 :
                print("You may proceed to the chemical facility!")
            
            elif choice==5 :
                print("EXITING")
                break
            else :
                ("INVALID CHOICE!")


for Unit in range (1-5) :
    input(f"Enter your {Unit} :")
    if Unit=="1" :
        print("Report to The Emergency room")