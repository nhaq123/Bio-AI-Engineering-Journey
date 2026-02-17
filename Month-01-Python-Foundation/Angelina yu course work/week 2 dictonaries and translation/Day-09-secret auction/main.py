import os
bidders_there= True
bidders_data = {}

def find_highestbidder( bidder):
    highest_amount = 0
    
    for  bids  in bidder:
        money  = bidder[bids] 
        if money > highest_amount:
            highest_amount = money
    print(f"The winner is { bids} of amount  ${highest_amount}")


while bidders_there:
    print("Welcome to the auction!")
    Name = input("Enter your Name : ")
    Money = int(input('How much you are going to bid : $ '))
    
    
    bidders_data[Name] = Money
    
    
    result = input("Does there any bidders type 'yes or 'no' ").lower()



    if result == "yes":
     
     os.system('cls' if os.name == 'nt' else 'clear')
     
     
    elif result == "no":
           find_highestbidder(bidders_data)
       
       
           print("Have a nice day ")
           bidders_there = False
       






                      
                        
                      


    
  


