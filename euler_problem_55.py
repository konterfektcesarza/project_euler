# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
# Not all numbers produce so quickly.
# It is thought (not proven) that some numbers never produce a palidnrome.
# Such number is called a Lychrel number.
# For this problem, assume that a number is a Lychrel number, if if doesn't 
# become a palindrome in less than 50 iterations.
# How many Lychrel numbers are there below 10_000?

all_lyrchels = 0

for i in range(1,10000):
    lyrchel = True
    a = i
    for n in range(49):
        b = int(str(a)[::-1])
        summa = a + b
        if summa == int(str(summa)[::-1]):
            lyrchel = False
            break
        a = summa
    if lyrchel == True:
        all_lyrchels += 1

print(all_lyrchels) # Answer