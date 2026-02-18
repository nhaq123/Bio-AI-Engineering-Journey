month = int(input("Give the month number "))

year = int(input("In Which year you want to find the days "))

def leap_year(year):
    if year % 4 == 0:
        if year % 100 ==0:
            if year % 400 ==0:
                return True
            else:
                return False
        else:
            return True
            
    else:
        return False
    


def month_in_days(month):
    days = [31, 28,31, 30,31,30,31,30,31,30,31,30 ]
    if month == 2 and leap_year(year) :
        return 29
    else:
        return days[month - 1]
        
    

output = month_in_days(month)

print(f"The month has {output} days")






    


    


    
    
    
