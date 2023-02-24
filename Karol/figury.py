
import math

def pole_kwadratu(a):
    return a * a

def pole_prostokata(a, b):
    return a * b

def pole_kola(r):
    return math.pi * r ** 2

def pole_trojkata(a, h):
    return 0.5 * a * h

def pole_trapezu(a, b, h):
    return (a + b) / 2 * h



while(True):
    print("1-OBLICZ POLE TRÓJKĄTA")
    print("2-OBLICZ POLE KWADRATU")
    print("3-OBLICZ POLE KOŁA")
    print("4-OBLICZ POLE PROSTOKĄTA")
    print("5-OBLICZ POLE TRAPEZU")
    print("6-ZAKOŃCZ")
    
    order=int(input("CO CHCESZ ZROBIĆ: "))
    
    if (order == 1):
        a = int(input("wpisz długość boku: "))
        h = int(input("Wpisz wysokość: "))
        pole_trojkata(a, h)
        print("pole trójkąta wynosi: ", pole_trojkata(a, h))
    elif (order == 2):
        a = int(input("wpisz długość boku: "))
        pole_kwadratu(a)
        print("Pole kwadratu: ", pole_kwadratu(a)) 
    elif (order == 3):
        r = int(input("Wpisz promień: "))
        pole_kola(r)
        print("Pole koła: ",pole_kola(r))
    elif (order == 4):
        a = int(input("Wpisz długość krótszego boku: "))
        b = int(input("Wpisz długość dłuższego boku: "))
        pole_prostokata(a, b)
        print("Pole prostokąta: ", pole_prostokata(a, b))
    elif (order == 5):
        a = int(input("Wpisz długość krótszego boku: "))
        b = int(input("Wpisz długość dłuższego boku: "))
        h = int(input("Wpisz wysokość: "))
        pole_trapezu(a, b, h)
        print("Pole Trapezu: ",  pole_trapezu(a, b, h))
        pole_trapezu
    elif (order == 6):
        print("KONIEC")
        break
    print("\n")
        


    
