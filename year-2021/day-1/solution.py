import numpy as np



'''
    PROCESS INPUTS
'''

# Open and parse input text
with open("measurements.txt", "r") as f:
    raw_lines = f.read()

# Convert to integers
measurements = list(map(
    int,
    
    raw_lines.split("\n")
))



'''
    PART ONE: PERFORM COUNT

    Complexity: O(n)
    
    Simply compare the current number and the next to count the number of 
    increases.
'''
'''
increases = sum([
    int(measurements[i] < measurements[i + 1])

    for i in range(len(measurements) - 1)
])

print(increases)
'''



'''
    PART TWO: CONVOLVE AND PERFORM COUNT

    Complexity: O(n * m)
    
    Convolve first and then perform the operation.
'''

# Convolution calculates the sum of three consecutive numbers
convolved = np.convolve(
    np.array(measurements), 
    np.ones(3), 
    mode='valid'
)

# Perform the same operation as part 1
increases = sum([
    int(convolved[i] < convolved[i + 1])

    for i in range(len(convolved) - 1)
])

print(increases)