# #if statements
# has_passed = False
# has_failed = False

# if has_passed:
#     print("Congrats you are elligible to next class 3")
# elif has_failed:
#     print("Opps please, go learn the previous class 2")
# else:
#     print("Unknown ERRR in the system")        


#Price of house
# price = 1000000
# good_credit = False

# if good_credit:
#     price = price*.1
# else:
#     price = price*.2
# print(f"You need to put $ {price}")  

#Logical opertaion

# high_marks = False
# pass_fizz = False

# if high_marks or not pass_fizz:  #not operator is used as an inveter
#     print("what a gorgiuos Genius")
# else:
#     print("Little genius")    




#weight convertor program

weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == 'L':
    weight = weight*10
    print(f"Your weight is {weight} in kilos")
elif unit.upper() == 'K':
    weight = weight/10
    print(f"Your weight is {weight} in lbs") 
else:
    print("ERR_R, Unknown Operation")
