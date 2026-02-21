import random
print("Welcome to the black jack ".title())
def deck_of_cards():

    cards = [ 11 , 2 , 3, 4, 5, 6, 7, 8, 9, 10, 10 ,10 ,10]
    card = random.choice(cards)
    return card 

users_choice = []
computers_choice = [] 

for i in range(2):
    
    users_choice.append(deck_of_cards())
    computers_choice.append(deck_of_cards()) 
    
    
def score (cards):
    return sum(cards)

users_score = score(users_choice)
computers_score = score(computers_choice)

       
print(f"Your cards are {users_choice} total sum is {users_score}")
print(f"The Computers first card is {computers_choice[0]}")

if users_choice == 11 and users_score > 21:
    choice = input(" It/'s Ace Do you wanna change card to 1  ? type 'y' for yes and 'n' for no  ")
    if choice == 'y':
        users_choice.remove(11)
        users_choice.append(1)
        new_score = score(users_choice)
        print(f"Your cards are {users_choice} total sum is{new_score}")

Game_is_over = False
probability_of_win = ["Its a draw" , "computer wins"]

reveal_computers_cards = input("Do you wannah  revel the next computer card Type 'y' for yes or 'n' for No . if you type 'n' you will  get draw  or computer wins ! ")
Game_is_over = False
if reveal_computers_cards == "y":
    print(f"The computers second card is {computers_choice[1]}") 
    print(f"The computers score is {computers_score}")


else: 
    Probability = random.choice(probability_of_win)
    print(Probability)


    



Game_over = False 
if users_score == 0 or computers_score == 0 or users_score > 21 :
   if users_score == 0 or users_score > 21:
       print("computer wins")
       Game_over = True
       
   else:
       print("you win")
       Game_over = True
       

if users_score == computers_score:
    print(f"Its a draw")
elif users_score > computers_score:
    print(f"You win ")
else:
    print(f"computer wins")
    





