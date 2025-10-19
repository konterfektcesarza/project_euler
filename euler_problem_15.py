# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20x20 grid?

# Initially i was thinking of writing an algorhytm that would move through the grids and store
# all the possible unique paths to the endpoint. But then i realised that it's really 
# a trivial combinatorics problem. Whatever the possible path may be, it always consists
# of 20 moves to the right and 20 moves down. So you may simply express it as choosing
# 20 indexes out of 40 that are of one type of the move.

import math as m

# Answer
print(m.comb(40,20))

