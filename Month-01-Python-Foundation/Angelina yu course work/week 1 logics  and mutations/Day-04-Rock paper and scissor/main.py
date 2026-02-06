rock = '''
  --------
------------
  --------
  --------'''
paper = '''
-------------
-------------
-------------'''
scissors = '''
-        -
 -       -
  -      -
    -   -
      - '''
import random
game_images = [rock, paper, scissors]
user_choice = int(input("what do you choose? Type 0 for rock, 1 for paper and 2 for scissors"))
computer_choice = random.randint(0,2)

if user_choice >=3  or user_choice < 0:

    print("You typed an invalid number, you lose")



else:
    print("you chose")
    print(game_images[user_choice])
    print("computer chose")
    print(game_images[computer_choice])
    if user_choice>computer_choice:
        print("You win")
    elif user_choice<computer_choice:
        print("You lose")
    elif user_choice==computer_choice:
        print("it\'s a draw")
    elif user_choice == 0 and computer_choice == 2:
        print("you win")
    
        



