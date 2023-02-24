slownik = {}


a = 1
while(True):
    print("1-Dodać definicje")
    print("2-Szukaj definicji")
    print("3-Usuń definicje")
    print("4-Zakończ")
    
    order=int(input("Co chcesz zrobić?: "))
    
    if (order == 1):
        klucz = input("Wpisz pojęcie: ")
        definicja = input("Podaj definicje: ")
        slownik[klucz] = definicja
        print("Definicja dodana pomyślnie.")
    elif (order == 2):
        klucz = input("szukaj słowa: ")
        if klucz in slownik:
            print(slownik[klucz])
        else:
            print("Nie znam pojęcia: ", klucz)
    elif (order == 3):
        klucz = input("Jakie słowo chcesz usunąć: ")
        if klucz in slownik:
            del slownik[klucz]
            print("Usunięto definicje o nazwie: ", klucz)
        else:
            print("Nie znam pojęcia: ", klucz)
    elif (order == 4):
        print("koniec")
        break
    else:
        print ("podałeś pozycje z poza menu: ")
    print("\n")
        
