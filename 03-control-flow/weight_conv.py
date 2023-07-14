weight = int(input("Weight: "))
units = input("L or K: ")
if units.upper() == "L":
    weight1 = 10*weight
    print("Your weight is " + str(weight))
elif units.upper() == "L":
    weight1 = 0.1*weight
    print("Your weight is " + str(weight))
print("You are not Fat enough")


# weight = int(input("Weight: "))
# unit = input("(L)bs or (k)g: ")
# if unit.upper == "L":
#     conv = weight*.45
#     print("You are " + str(conv)+"in kg")
# else:
#     conv = weight/.45
#     print("You are " + str(conv)+"in kg")
