#This is a comment


# My solution
number = input("Enter the number you wish to double: ")
ans = (int(number) * 2)
# print ("Your answer is: "+ str(ans))
print ("Your answer is: ", ans)

# An optimised solution
number = float(input("Enter the number you wish to double: "))
ans = (number * 2)
print ('Your answer is: ', ans)


# A further optimised solution - This can be used if you don't need the value again. Instead of storing it in a variable
number = float(input("Enter the number you wish to double: "))
print ('Your answer is: ', number * 2)

