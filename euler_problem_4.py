# check if the product is in fact a palindrome 
def palindrom_check(number):
    to_check = str(number)
    if to_check == to_check[::-1]:
        return(True)
    else:
        return(False)
                
# loop from the highest possible 3-digit number products to the lowest
palindroms = set()
for i in range(999 , 99, -1):
    for n in range (999, 99, -1):
        product = i*n
        if palindrom_check(product) == True:
            palindroms.add(product)
            break
        else:
            continue

print(max(palindroms))
