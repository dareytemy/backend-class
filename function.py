#Functions in Python

#Function definition

def add(num1, num2):
    sum = num1 + num2
    return sum

# The variable //sum used here is a local variable
sum = add (2,5)
print ("The sum is:", sum)

#This prints the result directly on the screen 
print(f"The sum is: {add (2,5)}")


#This is a greeting function
def greeting(name):
    name= input("Enter your name: ")
    print (f"Hello, {name}")
 
# This calls the greeting function   
greeting ("")


# Giving more than one paramters to a function

def sum(*args):
    initialSum = 0
    for num in args:
        initialSum += num
    return initialSum

print (sum (2, 5), sum (2, 5, 7))
