# What is the value of the first triangle number to have over five hundred divisors?


# Create a while loop iterates over triangle numbers. For each such number we create a list of divisors.
previous = 21
current = 7
while True:
    divisors = set()
    triangle = current + previous
    for i in range(1,int(triangle**0.5) + 1): # no need to check for more: each divisor <= sqrt(n) has a corresponding divisors >= sqrt(n)
        if triangle % i == 0:
            divisors.add(i)
    if len(divisors) > 250: # if we have more than 250 divisors <= sqrt(n), then there exists also more than 250 divisors >= sqrt(n)
        print(triangle) # Answer
        break
    else:
        previous = triangle 
        current += 1

