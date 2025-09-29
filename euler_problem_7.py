# What is the 10001st prime number?


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

# Now we are looping through all primes up to a point when the array where we
# save them is of lenght 10001. We start with 2 and 3 already in the array in order
# for our the previously defined function to work properly.
primes = [2,3]
start = 4
while len(primes) < 10001:
    if prime_check(start) == True:
        primes.append(start)
        start += 1
    else:
        start += 1

# Answer         
print(max(primes))
