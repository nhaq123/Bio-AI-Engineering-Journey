


def add (n1 , n2):
   return n1 +n2

def sub (n1, n2):
    return n1-n2
def multi(n1,n2):
   return n1*n2
def div(n1,n2):
    return n1/n2


operation = { "+" : add,
"-" : sub,
"*" : multi,
"/" : div, }


def The_recursion():
    num1 = int(input("Enter your first number "))
    should_continue =True
    while should_continue:

        
        
        num2 = int(input("Enter your next number"))
        for choose in operation:
         print(choose)

        
        
        decison = input("Enter the symbol of the operation as given above ") 

        calculation_direction = operation[decison]
        

        
        
        output = calculation_direction(num1 ,num2)
        
        print(f"The {decison} of {num1 , num2} is {output}")
        continue_process = input("Type 'y' for continue or 'n' for exit" )
        if continue_process == "y":
            num1 = output
        else:
            should_continue = False
            The_recursion()

        

The_recursion ()