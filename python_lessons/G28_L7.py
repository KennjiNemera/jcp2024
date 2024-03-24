# Group 28 (u23531003, u23551195, u23575035, u23618117, u23664542)

'''
7# If Statement
Objective: Teach the value of ‘if/else’ as a reasoning statement.Action: If this input is in this state (e.g. True)- then perform this action, else/if the input is in another state (e.g. False) - perform a different action.
'''

def check_age(age):
    # Checking if the user is eligible to vote
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote yet.")

def main():
    # Asking user's age
    age = int(input("Please enter your age: "))
    check_age(age)

if __name__ == "__main__":
    main()
