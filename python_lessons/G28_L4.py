# Group 28 (u23531003, u23551195, u23575035, u23618117, u23664542)

'''
# Infinite Repeat (Infinite Loop)
Objective: Teach the value of using an infinite loop.
Action: Repeat any input using an infinite loop. 
'''
def infinite():
    while True:
        user_input = input("Enter a command (type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the program...")
            break
        else:
            print("Command received:", user_input)

def main():
    infinite()

if __name__ == "__main__":
    main()
