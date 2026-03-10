import random
def Game():
    
    difficulty=input("Enter difficulty level(Easy/Medium/Hard)")

    if difficulty=="Easy":
        num = random.randint(1,50)
        count=0
        def guess():
            nonlocal count
            count+=1
            if count>100:
                print("You are a Stupid Idiot")
                return
            num_guess=int(input("Enter your guess(1-50):"))
            if num==num_guess:
                print("Your guess was correct")
                print("You took",count,"guesses")
                replay=input("Play again Y/N:")
                if replay=="Y":
                    Game()
            elif num>num_guess:
                print("Your guess is too low")
                guess()
            else:
                print("Your guess is too high")
                guess()
            
        guess()
    elif difficulty=="Medium":
        num = random.randint(1,100)
        count=0
        def guess(): 
            nonlocal count
            count+=1
            if count>100:
                print("You are a Stupid Idiot")
                return
            num_guess=int(input("Enter your guess(1-100):"))
            if num==num_guess:
                print("Your guess was correct")
                print("You took",count,"guesses")
                replay=input("Play again Y/N:")
                if replay=="Y":
                    Game()
            elif num>num_guess:
                print("Your guess is too low")
                guess()
            else:
                print("Your guess is too high")
                guess()
        guess()
    else:
        num = random.randint(1,500)
        count=0
        def guess():
            nonlocal count
            count+=1
            if count>100:
                print("You are a Stupid Idiot")
                return
            num_guess=int(input("Enter your guess(1-500):"))
            if num==num_guess:
                print("Your guess was correct")
                print("You took",count,"guesses")
                replay=input("Play again Y/N:")
                if replay=="Y":
                    Game()
            elif num>num_guess:
                print("Your guess is too low")
                guess()
            else:
                print("Your guess is too high")
                guess()
        guess()
        

Game()      


 