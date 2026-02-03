print("welcome to the tip calculator")
Totalbill = float(input ("What was the total bill? $"))
tip = int(input ("How much tip you want to pay 10 ,12 or 15?"))
split = int(input ("How many people to split the bill ?"))
each_pay= Totalbill*(1+tip/100)/split
print(f"Each person should pay : ${round(each_pay,2)}") #or instead you can also right {each_pay:.2f}


    
                                   



