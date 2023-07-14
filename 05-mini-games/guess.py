qn=1
score=0
while qn<=2:
    guess=1
    while guess<=3:
        guess_no=int(input("Guess: "))
        guess=guess+1  
        if guess_no==6:
            score=+50
            print("You win")
            break
    else:    
        print ("Fool! You loose")
    qn=qn+1
    print("\n\nRound 2: \n") 
print(f"Your Score is {score}")     
