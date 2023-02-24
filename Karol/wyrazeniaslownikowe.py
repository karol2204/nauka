"""
    wyrażenie słownikowe
"""

names = {"Arkadiusz", "Wioletta", "Karol", "Bartłomiej", "Jakub", "Ania"}

numbers = [1, 2, 3, 4, 5, 6]

celcius = {'t1': -20, 't2': -15, 't3': 0, 't4': 12, 't5': 24}
"""
namesLength = {
    name : len(name)
    for name in names
    if name.startswith("A")
}

multipliedNumbers = {
    number : number*number
    for number in range(1, 70)
}

fahrenheit = {
    key: celcius * 1.8 + 32
    for key, celcius in celcius.items()
    if celcius > -5
    if celcius < 20    
}

namesLenght = {
    name: len(name)
    for name in names
    }

multipliedNumbers = {
    number: number*451
    for number in numbers
    }

celsjuszKelwin = {
    key: name + 273
    for key, name in celcius.items()
    if name > -5
    if name < 24
    }
"""

cwiczonko = {element
    for element in range (2, 471)
    if (element % 7 == 0)
    if (element % 5 != 0)
    }

print (cwiczonko)
    
