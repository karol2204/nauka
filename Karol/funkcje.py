"""
    Funkcja - to blok kodu do którego można odwołać się
              w każdej chwili, aby otrzymać pożądany przez nas wynik.

    definition


    def nazwa_funkcji():
       instrukcja1
       instrukcja2

    nazwa_funkcji()
   


def wiadomosc_powitalna(imie):
    print("Cześć,",imie,"miło mi powitać Cię w moim programie!")
    

imiona = ["Arku", "Wiolu", "Bartku"]

for imie in imiona:
    wiadomosc_powitalna(imie)
"""

def pole_prostokata(a, b):
    return(a*b)
poleProstokataA = pole_prostokata(2, 4)
poleProstokataB = pole_prostokata(7, 6)
print( " prostokąt A: ", 5 * poleProstokataA)
print( " prostokąt B: ", 5 * poleProstokataB)
print( "suma pól powierzchni", (5 * poleProstokataA) + (5 * poleProstokataB))


def dzielenie (a, b):
    if(b == 0):
        return
    return a / b
x = dzielenie(10, 6)
print(dzielenie(10, 6))
