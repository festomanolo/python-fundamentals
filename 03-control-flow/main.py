# if 2<3:
#     print("Yes it is True")
#     if 4>2:
#         print("It is True again")

# else:
#     print("No, it is NOt True")

    #creat a program that will validate a person for Voting
    #condtitions
    # 3 names
    # Male
    # +18
    # cheti cha from 4
name1=input("Person First Name: ")
name2=input("Person Middle Name: ")
name3=input("Person Surname: ")
name=f"{name1}\t{name2}\t{name3}"
age=int(input("Person Age: "))
gender=str(input("Gender F/M: "))
csee=input(" CSEE certificate, Y-for Yes  or N-for No: ")
if age>=18:
    len1=len(name1)
    len2=len(name2)
    len3=len(name3)
    if len1>0:
        if len2>0:
            if len3>0:
                if gender=='M':
                    if csee=='Y':
                        print(f"{name} You are validate to vote")
else:
    print(name+" Oops! Sorry,You are Too young to Vote")     
