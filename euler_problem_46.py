import math

def check_composed(a):
    if a < 2:
        return False 
    for i in range(2,int(math.sqrt(a)) + 1):
        if a % i == 0:
            return True
    return False

start = 33 
found = False
while True:
    start += 2
    if check_composed(start) == True:
        potential_primes = []
        for i in range(2,start):
            if check_composed(i) == False:
                potential_primes.append(i)
        unable = True 
        for p in potential_primes:
            square = math.sqrt((start - p)/2)
            if square == int(square):
                unable = False
        if unable == True:
            found = True
    if found == True:
        print(start)
        break   
    else:
        continue


