import figury1

from enum import IntEnum

Menu_Figury = IntEnum('Figury', 'Kwadrat Prostokąt Koło Trójkąt Trapez')

while(True):
    wybor = int(input("""Wybierz figurę, której pole chcesz obliczyć:
    1. Kwadrat
    2. Prostokąt
    3. Koło
    4. Trójkąt
    5. Trapez
    """))
    if (wybor == Menu_Figury.Kwadrat):
        a = float(input("Podaj bok kwadratu: "))
        print("Pole kwadratu wynosi:", figury1.pole_kwadratu(a))
    elif (wybor == Menu_Figury.Prostokąt):
        a = float(input("Podaj krótszy bok prostokąta: "))
        b = float(input("Podaj dłuższy bok prostokąta: "))
        print("Pole prostokąta wynosi:", figury1.pole_prostokata(a, b))
    elif (wybor == Menu_Figury.Koło):
        r = float(input("Podaj promień koła: "))
        print("Pole koła wynosi:", figury1.pole_kola(r))
    elif (wybor == Menu_Figury.Trójkąt):
        a = float(input("Podaj bok trójkąta: "))
        h = float(input("Podaj wysokość trójkąta: "))
        print("Pole trójkata wynosi:", figury1.pole_trojkata(a, h))
    elif (wybor == Menu_Figury.Trapez):
        a = float(input("Podaj bok trapezu a: "))
        b = float(input("Podaj bok trapezu b: "))
        h = float(input("Podaj podaj wysokość trapezu: "))
        print("Pole trapezu wynosi:", figury1.pole_trapezu(a, b, h))
    else:
        print("Nie ma takiej pozycji")
