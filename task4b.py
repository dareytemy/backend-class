VALID_CARD_LENGTH = 16

# A function for the sum of digits for numbers greater than 10
def sumDigit(number):

    result = 0

    while number != 0:
        result += number % 10
        number = number // 10

    return result


def cardInput(cardNumber):
    if not cardNumber .isnumeric():
        return False
    if len(cardNumber) != VALID_CARD_LENGTH:
        return False
    

    # Converts the card number to an integer and then to a list
    cardNumber = [int(number) for number in cardNumber]
    
    # This doubles the value in the list with indices of 2,4,6,8,........
    cardNumberDoubled = [number * 2 if index % 2 == 0 else number for index, number in enumerate(cardNumber)]
    
    # print(cardNumber)
    # print(cardNumberDoubled)
    

    # finalList = [sumDigit(number) if  (index & 2 == 0) and number > 9 else number for index, number in enumerate(cardNumberDoubled)]
    finalList = [sumDigit(number) if number > 9 else number for number in cardNumberDoubled]

    return sum(finalList) % 10 == 0
    
    #if sum(finalList) % 10 == 0:
    #     print("Valid card details")
    #else:
    #   print("Invalid card details")

    # print (finalList)


while True:
    cardNumberUserInput = input("Please enter your 16-digit card numnber: ")

    if cardInput(cardNumberUserInput):
        print ("Valid card details")
        break
    else:
        print ("Card number should be 16-digit and numbers")


# cardInput("1234567890987654")
# cardInput("4137889471755904")