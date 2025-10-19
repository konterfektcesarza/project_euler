# What is the sum of the digits of the number 2^1000?

a = str(2**1000)

summation = 0

for n in a:
    b = int(n)
    summation += b

# Answer    
print(summation)
