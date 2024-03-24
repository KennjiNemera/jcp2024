# Group 28 (u23531003, u23551195, u23575035, u23618117, u23664542)

'''
3# Repeat (Loop)
Objective: Teach the value of using a loop.
Action: Repeat any input using a loop.
'''
# Define a function
def greet(name):
    """Function to greet the user."""
    print("Hello,", name, "!")
    
# Loop to greet multiple users
def greet_users(user_list):
    """Function to greet multiple users."""
    for user in user_list:
        greet(user)

# List of users
users = ["Alice", "Bob", "Charlie", "David"]

# Main Functions
def main():
    greet_users(users)

if __name__ == "__main__":
    main()
