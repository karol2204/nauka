"""
Znajdź liczby od 2 do 470 włącznie, które są:
- podzielne przez 7, ale nie są podzielne przez 5

Z czego skorzystasz?
1) generatora
2) wyrażenia listowego
3) wyrażenia zbioru
4) wyrażenia słownikowego

Zastanów się, czy odpowiedź na to pytanie jest zawsze taka sama?

range(100, 471)

7
14
21
28
35
...

5
10
15
20
25
30
35
---

7 % 7 == 0
14 % 7 == 0
21 % 7 == 0

35 % 5 == 0

7 % 5 == 2
14 % 5 == 4

numbers = [1, 2, 3, 4, 5, 6]
numery = [
    number
    for number in range(2, 471)
    if (number % 7 == 0)
    if (number % 5 != 0)
    ] 
print(mnozenie)
"""
def mnozenie(numery): 
    numery = [
            number
            for number in range(2, 471)
            if (number % 7 == 0)
            if (number % 5 != 0)
            ]
    return(numery)
    
print(5 * mnozenie)
