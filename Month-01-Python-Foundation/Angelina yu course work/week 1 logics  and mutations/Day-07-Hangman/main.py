list = ["apple", "ronaldo", "education", "python", "programming" ]
import random 
stages = [
    
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """
]

 
choice = random.choice(list)
print(choice)
print("Welcome to Hangman game") 
attempts = 6
print (f"You have {attempts} attempts to guess the word")

list1 = []
print(f"The word has {len(choice)} letters")
for i in range(len(choice)):
    list1.append("_")
print(list1) 
while "_" in list1: #assign a variabble call it as false check while not variable
    guess = input("Guess the word: ").lower()


    if guess in choice:
       for i in range(len(choice)):
       
          if guess == choice[i]:
             list1[i] = guess
          

       print(list1) 
    else:
        print("Wrong guess, try again")
        attempts-=1
        print(f"you have {attempts} attempts left")
        print(stages[6 - attempts - 1]) # Display the current hangman stage
        

        if attempts == 0:
            print ("Game over")
            break
        else:continue  
     #if "_" in list1: 
     #    print("Congratulations! You've guessed the word.")
     #    break
        