# Find the difference between the sum of the squares of the first 
# one hundred natural numbers and the square of the sum

squares = []
summation = []

for i in range(101):
    squares.append(i**2)
    summation.append(i)

# Answer
print(sum(squares) - sum(summation)**2)