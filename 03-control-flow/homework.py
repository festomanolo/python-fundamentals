   #creat a program that will validate a person for Voting
    #condtitions
    # 3 names
    # Male
    # +18
    # cheti cha from 4
name=input("Your Full name: ")
gender=input("Gender: ")
age=int(input("Age: "))
cert=input("CSEE Certificate, Y or N: ")
if gender=='M':
    if age>=18:
        if cert=='Y':
            print("\n\nYou can Vote")
        else:
            print("Please go for CSEE")
    else:
        print("You are not matured enough to vote")            
else:
    print("\n\n You're not a MAN, You cannot VOTE")            
