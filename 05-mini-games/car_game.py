while True:
    command=input("> ")
    if command=="help":
        print("start- Car started...Ready to Go! \nstop- Car stopped \nquit- exit the car")
    elif command=="start":
        print("Car started...Ready to Go!")
        if command=="start":
            print("car is already")
    elif command=="stop":
        print("car stoped")
    elif command=="quit": 
        break
    else:
        print("Ummm..I don't Understand that")       
                 
