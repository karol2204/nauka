from enum import IntEnum

Menu_Tydzień = IntEnum('Tydzień', 'Poniedziałek Wtorek Środa Czwartek Piątek Sobota Niedziela')

while(True):
    wybor = int(input("""Wybierz dzień tygodnia:
    1. Poniedziałek
    2. Wtorek
    3. Środa
    4. Czwartek
    5. Piątek
    6. Sobota
    7. Niedziela
    """))
    if (wybor == Menu_Tydzień.Poniedziałek):
        print("Niebieski")
    elif (wybor == Menu_Tydzień.Wtorek):
        print("Czerwony")
    elif (wybor == Menu_Tydzień.Środa):
        print("Żółty")
    elif (wybor == Menu_Tydzień.Czwartek):
        print("Zielony")
    elif (wybor == Menu_Tydzień.Piątek):
        print("Brązowy")
    elif (wybor == Menu_Tydzień.Sobota):
        print("Habrowy")
    elif (wybor == Menu_Tydzień.Niedziela):
        print("Biały")
    else:
        print("Nie ma takiej pozycji")
    print('\n')

