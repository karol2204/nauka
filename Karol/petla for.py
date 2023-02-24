wynik = 0
"""
i = 0
while i < 4:
    x = int(input("Podaj Liczbe: "))
    wynik += x
    i += 1

print("wybik dodawania to: ", wynik)


x =0
for i in range(5):
    x = int(input("Podaj Liczbe: "))
    wynik += x
    print (i%2 == 0)
    

print("wybik dodawania to: ", wynik)

"""

for i in range(30):
    if (i%5 == 0 and not i%3 == 0):
        print("liczba ",i)
    elif (i%5 == 0 and i%3 == 0):
        print("liczba ",i)
