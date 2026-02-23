
#Functions go here

def yes_no(question):

    """Checks user response to a question is yes/no (y/n) returns 'yes' or 'no'"""

    while True:
        response = input(question).lower()
        #check if user says yes/no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please type yes or no")


def instructions():
    """Prints instructions"""

    print("""
*** Instructions ***

Roll the dice and try to win!
    """)


#Main Routine

# ask user if they want instructions (check if they say yes/no)
want_instructions = yes_no("Would you like to see the instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

print()
print("Program continues")