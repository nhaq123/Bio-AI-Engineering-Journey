print("Welcome to the treasure island!")
print("your mission is to find the treasure.!")
choice_1 =input('you\'re at a cross road. where do you want to go? type "left" or "right"').lower()
if choice_1 == "left":
  choice_2 =  input('you\'ve come to a lake. there is an island in the middle of the lake. type "wait" to the boat or "swim across" the river.').lower()
  if choice_2 == "wait":
    choice_3= input("you arrived at the island unharmed .which door you want to select 'red', 'blue' or 'green'").lower()
    if choice_3 == "red":
        print("It\'s a room of full fire .Game over")
    elif choice_3 == "green":
        print("you found the treasure. You win!")
    elif choice_3 == "blue":
        print("you enter in a room of beasts.Game over")
    else:
        print("You choosed the differnt door that doesnt esxist")
  else:
    print("you got attacked by the angry trout , Game Over .")   
else:
   print("you fell into a hole.game over ")           

        
              
        
  
     

