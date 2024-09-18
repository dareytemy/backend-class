# A calculator that allows users to enter numbers (float or integer) and stops when they enter an alphabet, then prints the sum and product of the already entered numnber.

initialSum = 0
initialProduct = 1

print ("Enter numbers one by one, enter an alphabet or special character to see the magic")


while True: #This is an infinite loop control
    enterAnything = input("Enter a number: ")
    
    try: #Tests a block of code for errors- Try Except block
        number = float(enterAnything)
        initialSum += number
        initialProduct *= number
    
    #The code that should run when they error happens
    except ValueError:
        break


print (f"The sum of the numbers you entered: {initialSum}")
print (f"The sum of the numbers you entered: {initialProduct}")