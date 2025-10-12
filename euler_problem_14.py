# The following iterative sequence is defined for the set of positive integers:
# n == even -> n/2
# n == odd -> 3n + 1
# It is thought that all starting numbers finish at 1
# Which starting number under 1 000 000 propduces the longest chain? 

current_highest = [1,1]
for n in range (1,1000000): # Start from 1 not 0 in order to avoid infinite loop since 0%2 = 0 and n never equals 1
    start_n = n
    combination_len = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
            combination_len += 1           
        elif n % 2 != 0: # "Elif" instead of "if" so that when n//2 == 1 the loop stops immediately
            n = 3*n + 1
            combination_len += 1            
    if combination_len > current_highest[1]:
        current_highest[0] = start_n; current_highest[1] = combination_len

# Answer
print(current_highest)