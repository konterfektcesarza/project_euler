# Starting with the number 1 and moving to the right in a clockwise 
# direction a 5 by 4 spiral is formed as follows:

#  21 22 23 24 25
#  20  7  8  9 10
#  19  6  1  2 11
#  18  5  4  3 12
#  17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonal is 101 
# What is the sum of the numbers on the diagonals ina  1001 by 1001 spiral 
# formed in the same way? 

# Zauważmy, że dla takiej 1001x1001 spirali mamy tak naprawdę rdzeń "1" w środku, 
# oraz 500 warstw z 4 ineresującymi nas liczbami (wierzchołkami warstwy).
# Zadanie sprowadza się do wyznaczenia algorytmu przechodzenia wartości x_k do x_k+1 
# oraz dodawaniu ich do naszej sumy 

# Algorytm:
# W każdej wartswie zaczynamy od 1 pierwszego wierzchołka, a wzór na 
# następne wierchołki to rekurencyjne x_k+1 = x_k + 2*numer_warstwy 
# Robimy tak 3 razy, a następnie przeskakujemy do nastepnej warstwy 
# Nowy startowy wierzchołek to za każdym razem ostatni wierzchołek z 
# warstwy + 2*numer_warstwy 


suma = 1 # Rdzeń spirali 
wierzcholek_startowy = 3 
numer_warstwy = 1 
while numer_warstwy <= 500:
    for i in range(4):
        dodaj = wierzcholek_startowy + i*2*numer_warstwy
        suma += dodaj
        if i == 3: 
            numer_warstwy += 1
            wierzcholek_startowy = dodaj + 2*numer_warstwy 


print(suma) # Odpowiedź: 
