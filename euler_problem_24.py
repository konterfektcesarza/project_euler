import math as m

# For a given first position there are 9! (362880) permutations of the rest of digits
# So 1_000_000 // 362880 = the first digit

# For a given second poition there are 8! (40320) permutations
# There are 1_000_000 - (2 * 362880) = 274240  iterations left
# 274240 // 40320 = the second digit

# So basically instead of computating all 1_000_000 permuations, we iteratively count how many
# iterations will happen for a given position

the_number = ""

position = 1
iterations_left = 999_999 # for 1_000_000 -> overindexing

digits_left = [i for i in range(10)]

while position != 11:
    n_perm = m.factorial(10 - position)
    digit = digits_left.pop(iterations_left // n_perm)
    the_number += str(digit)
    position += 1
    iterations_left %= n_perm

print(int(the_number))
