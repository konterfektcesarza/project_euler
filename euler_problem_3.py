# What is the largest prime factor of the number 600851475143?


# First let's define a function that checks if a number is in fact prime 
# They way to optimize the time complexity is to only check for possible
# divisors up to square root of the number we are checking. 
# Since we can represent every non-prime number as a*b (a,b is natural nad != 1,n)
# if a > sqrt(n) then b < sqrt(n) and so we are basically checking
# the same possible divisors=
def prime_check (n):
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return(False)
        if i == int(n**0.5) and n%i != 0:
            return(True)
        else:
            continue

# Since we are looking for the highest possible divisor, it's more
# efficient to start from lowest a, and check for according highest b (remember n = a*b)
for i in range(2, 600851475143):
    if 600851475143 % i == 0:
        pos_prime_factor = int(600851475143/i)
        if prime_check(pos_prime_factor) == True:
            print(pos_prime_factor)
            break
        else:
            continue
    else:
        continue

# Answer: 6857
