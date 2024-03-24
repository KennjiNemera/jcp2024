# Group 28 (u23531003, u23551195, u23575035, u23618117, u23664542)

'''
1# Movements (Activate multiple actions in a Function)
Objective: Teach how these movements work.
Movements: Turn left, turn right, move forward, move backward
Restrictions: You cannot move left or right directly.
'''

# Init Global Variables

current_x = 0
current_y = 0
direction = 0
dir_array = [[1,0],[0,1],[-1,0],[0,-1]] # up, right, down, left
dir_name = ["Up", "Right", "Down", "Left"]

# Output Functions

def print_position():
    global current_x, current_y, direction, dir_array, dir_name
    print("Currently on: [", current_x, ",", current_y, "]")

def print_direction():
    global current_x, current_y, direction, dir_array, dir_name
    print("Facing: ", dir_name[direction], " ", direction)

def print_commands():
    print("1 - Move Forward")
    print("2 - Move Backward")
    print("R - Turn Right")
    print("L - Turn Left")

# Member Functions

def move_forward():
    global current_x, current_y, direction, dir_array, dir_name
    current_x = current_x + dir_array[direction][0]
    current_y = current_y + dir_array[direction][1]

def move_backward():
    global current_x, current_y, direction, dir_array, dir_name
    current_x = current_x - dir_array[direction][0]
    current_y = current_y - dir_array[direction][1]

def turn_left():
    global current_x, current_y, direction, dir_array, dir_name
    direction = direction - 1
    if direction < 0:
        direction = 3

def turn_right():
    global current_x, current_y, direction, dir_array, dir_name
    direction = direction + 1
    if direction > 3:
        direction = 0

# Main Function

def main():
    while (True):
        print("=================================")
        print_position()
        print_direction()
        print("Would you like to move?")
        cmd = input("0 to exit, any other key to continue\n")
        if cmd == "0":
            print("Movement has ended")
            break
        print_commands()
        cmd = input("Enter command here:\n")
        if (cmd not in ["1", "2", "R", "L"]):
            print("Invalid command! Retry\n")
            continue
        if (cmd == "1"):
            move_forward()
        if (cmd == "2"):
            move_backward()
        if (cmd == "R"):
            turn_right()
        if (cmd == "L"):
            turn_left()
        

if __name__ == '__main__':
    main()
