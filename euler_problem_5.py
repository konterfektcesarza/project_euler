# What is the smallest positive number that is evenly
# evenly divisible by all of the numbers from 1 to 20?

# First let's define a set of numbers in range 1-20
# that suffice for checking if a number is divisible by
# all the numbers from 1 to 20, so that the algorhytm 
# is not redundant. 
check_list = set()
for i in range(20,1,-1):
    divisor = False
    for n in check_list:
        if n%i == 0:
            divisor = True
        else:
            continue
    if divisor == False:
        check_list.add(i)
    else:
        continue

# Now a simple loop that stops when the number we are 
# looking for is divisible by all items in the set.
loop = sorted(check_list)
number = max(check_list)
divisible = False
while divisible == False:
    for i in loop:
        if number % i != 0:
           number += max(check_list)
           break
        if i == max(check_list):
            divisible = True
            break
        else:
            continue

# Answer
print(number)


