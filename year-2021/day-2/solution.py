import numpy as np



'''
    PROCESS INPUTS
'''

# Open and parse input text
with open("instructions.txt", "r") as f:
    raw_lines = f.read()

# Split by new line and direction and step
instructions = [
    [line.split()[0], int(line.split()[1])]

    for line in raw_lines.split('\n')
]



'''
    PART ONE: TRAVEL WITH DIRECTIONS

    Complexity: O(n)
    
    Iterate through the instructions and keep track of current coordinates.
'''
'''
# Positions is an array of horizontal distance and depth coordinates
# Horizontal distance is only affected by "forward" commands, and thus a boolean
# is sufficient, septh coordinates can be coded with a dictionary of directions, 
# where the "forward" command does not affect anything
positions = np.array([
    [
        step * int(direction == "forward"), 
        step * {
            "up": -1, 
            "down": 1,
            "forward": 0
        }[direction]
    ]

    for direction, step in instructions
])

# Sum all of the coordinate changes for the final coordinate (assuming the ship
# begins at [0, 0]) and multiply the coordinates
print(np.prod(np.sum(positions, axis=0)))
'''


'''
    PART TWO: TRAVEL WITH AIM

    Complexity: O(n)
    
    Keep track of aim while doing the same process. The solution above does not
    work, since it assumes that there are only cardinal directions to work with.
    There is now a cumulative variable to be kept.
'''

aim = 0
x, y = 0, 0

# Iterate through the instructions
for direction, step in instructions:
    # Aim is only changed by "down" and "up"
    aim += step * (1 if (direction == "down") else -1 if (direction == "up") else 0)
    
    # Take a step based on the aim and step
    if direction == "forward":
        x += step
        y += step * aim

print(x * y)