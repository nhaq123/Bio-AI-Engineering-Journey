list = ["apple", "ronaldo", "education", "python", "programming" ]
import random

 
choice = random.choice(list)
print(choice)
print("Welcome to Hangman game")

list1 = []
print(f"The word has {len(choice)} letters")
for i in range(len(choice)):
    list1.append("_")
print(list1)

guess = input("Guess the word: ").lower()



for i in range(len(choice)):
    if guess == choice[i]:
        list1[i] = guess
print(list1)
         

        
        

    
