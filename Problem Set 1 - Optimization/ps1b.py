###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # create a table where rows represents the incremental target weight and columns represent each egg
    table = [[0 for i in range(0,len(egg_weights) + 1)] for j in range(0, target_weight +1)]
    
    # Include base cases
    for i in range(1, target_weight+1):
        table[i][0] = float('inf')
    # going through each incremental value:
    for i in range(1, target_weight + 1):
        # going through the different eggs:
        for j in range(0, len(egg_weights)):
            if egg_weights[j] > i:
                table[i][j+1] = table[i][j]
            if i - egg_weights[j] >= 0:
            # the solution to the problem will be the min of the 
            # state of the world where I take the new coin vs 
            # if I were to no take the coins
                table[i][j+1] = min(1 + table[i - egg_weights[j]][j+1], table[i][j])
            else:
                table[i][j+1] = table[i][j]
    return table[target_weight][len(egg_weights)]

def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    res = float("Inf")
    if target_weight == 0:
        return 0
    if target_weight in memo:
        sub_res = memo[target_weight]
        if sub_res < res:
                res = sub_res
    else:
        for i in range(0,len(egg_weights)):
            if egg_weights[i] <= target_weight:
                sub_res = 1 + dp_make_weight(egg_weights, target_weight - egg_weights[i])
                memo[target_weight] = sub_res
                if sub_res < res:
                    res = sub_res
    return res
    
    
    
    

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()

