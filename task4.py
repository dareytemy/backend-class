#Credit Card Validity Check

# def creditCardValidity ():

VALID_CARD_LENGTH = 16
    
creditCardNumber = input("Enter the 16-digit number on your credit card: ")

# Verifying the validity of the user's input
while len(creditCardNumber) < VALID_CARD_LENGTH or len(creditCardNumber) > VALID_CARD_LENGTH or creditCardNumber.isnumeric() == False:
   print ("Credit card number should be numeric and 16-digit")
   creditCardNumber = input("Enter the 16-digit number on your credit card: ")

# Converts the items in the list to integers
creditCardList = [int(i) for i in creditCardNumber]

# creditCardList = [item for index, item in enumerate(creditCardNumber) if index % 2 == 0]

# Takes items in index 0,2,4,... and doubles the them
creditCardList = [item * 2 if index % 2 == 0 else item for index, item in enumerate(creditCardList)]

#Computes Validity of Credit Card
if sum(creditCardList) % 10 == 0:
    print ("Valid Credit Card!")
else:
    print("Invalid Credit Card")


# print(creditCardList)






        

