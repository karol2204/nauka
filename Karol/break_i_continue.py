"""
break

continue


wynik = 0

i = 0

while i < 3:
    x = int(input("Podaj dodatnią liczbę:"))
    if (x > 0):
        wynik += x
    else:
        print("Miała być liczba dodatnia, zapytam się o liczbę dodatnią ponownie")
        continue
    print("Aktualny wynik dodawania to:", wynik)
    i += 1

"""
wynik = 0

i = 0

while i < 4:
    x = int(input("podaj liczbę dodatnią:"))
    if (x%2 == 0 and x > 0):
        wynik += x
    else:
        print ("podaj liczbę dodatnią")
        continue
    print ("wynik", wynik)
    i += 1 
    
