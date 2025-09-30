# A pythagorean triplet is a set of three natural numbers,
# a < b < c for which: a^2 + b^2 = c^2. There exists only one
# Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for a in range(1,1000):
    end = False
    if end == True:
        break
    else: 
        for b in range(1,1000):
            c = 1000 -a -b
            if a**2 + b**2 == c**2:
                print(a*b*c) # Answer
                end = True
            else:
                continue




