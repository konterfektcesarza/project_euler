# Problem description: https://projecteuler.net/problem=30

writable = []

# How do we define the upper bound?
# Max for 1 digit value -> 59049
# So k-digit number, the upper bound is k * 59049

# Let's consider a 4 digit number:
# max = 236196  ---> so all sums of 4 digits are beneath the bound

# It seem like as long as len("k * 59049") > k we are good
# Let's find the value of k that violates that condition

k = 1
while len(f'{k*59049}') > k:
    k += 1
print(k)

# Out = 6 ---> we only have to check up to 6 digit numbers
# 6 * 59049 = 354_294

for i in range(2,354_294): # 1 is an exception
    seq = [int(d)**5 for d in str(i)]
    if sum(seq) == i:
        writable.append(i)

print(sum(writable))
