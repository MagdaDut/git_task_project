'''
    This method will return a greeting
    input: the users message
'''
def greeting_card(message):
    cardLine = "******************************************"
    emptyLine = "*                                        *"
    cardLineLength = len(cardLine)
    messageLength = len(message)
    print(cardLine)
    print(emptyLine)
    print(emptyLine)

    #Print longer messages over two lines
    if messageLength > cardLineLength:
        print(message[:cardLineLength])
        print(message[cardLineLength:])
    else:
        #Format short messages to fit in the greeting card 
        spaces = cardLineLength - messageLength
        left_spaces = spaces // 2
        right_spaces = spaces - left_spaces - 2
        print("*" + " " * left_spaces + message + " " * right_spaces + "*")
        
    print(emptyLine)
    print(emptyLine)
    print(cardLine) 
print("Hello World!")
print("Git is awesomeness!")

user_input = input("Enter the most amazing greeting: ")

# Display the users amazing message
greeting_card(user_input)
