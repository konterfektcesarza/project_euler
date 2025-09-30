# Find the sum of all the primes below two million

# First let's define a function that checks if a number is in fact prime 
# They way to optimize the time complexity is to only check for possible
# divisors up to square root of the number we are checking. 
# Since we can represent every non-prime number as a*b (a,b is natural nad != 1,n)
# if a > sqrt(n) then b < sqrt(n) and so we are basically checking
# the same possible divisors
def prime_check (n):
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return(False)
        if i == int(n**0.5) and n%i != 0:
            return(True)
        else:
            continue

# A simple while loop that adds all the primes met on the way to the number 2000000
primes = {2,3}
potential_prime = 4
while potential_prime < 2000000:
    if prime_check(potential_prime) == True:
        primes.add(potential_prime)
        potential_prime += 1
    else:
        potential_prime += 1

# Answer
print(sum(primes))
        