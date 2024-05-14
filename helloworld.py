'''
    This method will return a greeting
    input: the users message
'''
def greeting_card(message):
    print("******************************************")
    print("*                                        *")
    print("*                                        *")
    print("*" + message + "*")
    print("*                                        *")
    print("*                                        *")
    print("******************************************") 
print("Hello World!")
print("Git is awesomeness!")

user_input = input("Enter the most amazing greeting: ")

# Display the users amazing message
greeting_card(user_input)
