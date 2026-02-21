print("Welcome To The Number Guessing Game")
import random
print("I am thinking the number between 1 to 100")
Numbers = []
for i in range(1,101):
    Numbers.append(i)
game_level = input("What level you want 'easy' or 'hard' ")




def easyplay():
    attempts = 10 
    computers_guess= random.choice(Numbers) 
    

    
    while attempts != 0 :
        
        
        users_guess = int(input("Guess the number between 1 to 100"))
        

        if users_guess > computers_guess:
            print("Too High  Try again")
            attempts = attempts - 1
            print(f"You have {attempts} left ")

        elif users_guess< computers_guess:
            print("Too Low Try again")
            attempts = attempts - 1
            print(f"You have {attempts} left ")

        else:
            print("you win")
            option = input("Did you want to continue to play the game again typye 'y' for yes and 'n' for n no")
            if option == "y":
                easyplay()
            else:
                break

        if attempts == 0:
            print("Game over")
            break

def hardplay():
    attempts = 5
    computers_guess= random.choice(Numbers) 
    

    
    while attempts != 0 :
        
        
        users_guess = int(input("Guess the number between 1 to 100"))
        

        if users_guess > computers_guess:
            print("Too High  Try again")
            attempts = attempts - 1
            print(f"You have {attempts} left ")

        elif users_guess< computers_guess:
            print("Too Low Try again")
            attempts = attempts - 1
            print(f"You have {attempts} left ")

        else:
            print("you win")
            option = input("Did you want to continue to play the game again typye 'y' for yes and 'n' for n no")
            if option == "y":
                easyplay()
            else:
                break

        if attempts == 0:
            print("Game over")
            break




    
            











   
if game_level == 'easy':
    print("You have ten attempts to guess the number")
    easyplay()
else:
    print("You have 5 attempts to guess the number ")
    hardplay()