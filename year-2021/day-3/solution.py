from collections import Counter
from attr import has
from matplotlib.pyplot import close
import numpy as np



'''
    PROCESS INPUTS
'''

# Open and parse input text
with open("report.txt", "r") as f:
    raw_lines = f.read()

# Split by new line
report = raw_lines.split('\n')



'''
    PART ONE: COMPUTE MOST COMMON OCCURRENCE

    Complexity: O(n ^ 2 log n)
    
    Using Counter, compute the most commonly occuring bit and compute the gamma
    and epsilon rates. The report, however, must first be transposed to help 
    with the calculation of the rates.

    The complexity is calculated by the complexity of the hash tables O(n log n)
    and the iteration through the report O(n). An optimization can be made here
    where the epsilon rate is the flipped bits of the gamma rate (since if 1
    is most common in any bit position, 0 would be least common).
'''

# Rearrange report
arranged_report = np.array([
    list(sample)

    for sample in report
]).T

# Calculate gamma and epsilon
# Gamma is calculated with hash tables, epsilon is calculated with gamma
gamma_raw = ''.join([
    Counter(row).most_common()[0][0]

    for row in arranged_report.tolist()
])

epsilon_raw = ''.join([
    "0" if (bit == "1") else "1"

    for bit in gamma_raw
])

#print(int(gamma_raw, 2) * int(epsilon_raw, 2))



'''
    PART TWO: FIND OXYGEN GENERATOR AND CO2 SCRUBBER RATING

    Complexity: O(n ^ 2 log n)
    
    Using a fairly straightforward method, the algorithm is optimized and more
    readable with Numpy functions, such as np.where and np.delete. 
'''

def retrieve_rates (replacement, most=True):
    pool = arranged_report.T

    n = len(pool[0])
    rating = [ '0' ] * n

    for pos in range(n):
        # Calculate most (or least) common
        slice = pool[:, pos]
        rating_bit = Counter(slice).most_common()[0 if most else -1][0]

        # Chcek for tie breaker
        # There is a tie if there are as many '0's as half of the total length
        # of the digits in that position
        tie_breaker = (sum(slice == '0') == (len(pool) / 2))
        rating[pos] = replacement if tie_breaker else rating_bit

        # Remove all non-matching samples
        pool = np.delete(
            pool, 
            np.where(pool[:, pos] != rating[pos]), 
            axis=0
        )

        # If there is one left, that is the rating
        if len(pool) == 1:
            rating = pool[0]
            break

    return int(''.join(rating), 2)



# Call the functions with respective arguments
oxygen_gen_rate = retrieve_rates('1', True)
co2_scrub_rate = retrieve_rates('0', False)

print(oxygen_gen_rate * co2_scrub_rate)