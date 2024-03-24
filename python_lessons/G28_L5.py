# Group 28 (u23531003, u23551195, u23575035, u23618117, u23664542)

'''
5# While Statement
Objective: Teach the value of ‘while’ as a reasoning statement.
Action:  Perform any action while a specific state is applied. (True/False)
'''

import math

def while_func():
    val = 1
    while (val < 1e9):
        print(val)
        val = int(math.ceil(val * 1.1))

def main():
    while_func()

if __name__ == "__main__":
    main()
