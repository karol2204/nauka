weight_p =int(input("wpisz wagę psa: "))

print("1- niekastrowane")
print("2- kastrowane")
print("3- z nadwagą")
print("4- leczenie otyłości")
print("5- w okresie rekonwalescencji")
print("6- lekko trenujący")
print("7- średnio trenujący")
print("8- ciężko trenujący")

activity_p = int(input("wybierz psaujące "))

rer = 70 * (weight_p)**0.75
#print(round(rer))

if activity_p == 1:
    der = round(rer) * float(1.8)
    print(round(der))
elif activity_p == 2 :
    der = round(rer) * float(1.6)
    print(round(der))
elif activity_p == 3 :
    der = round(rer) * float(1.4)
    print(round(der))
elif activity_p == 4:
    der = round(rer) * float(1)
    print(round(der))
elif activity_p == 5 :
    der = round(rer) * float(1.4)
    print(round(der))
elif activity_p == 6 :
    der = round(rer) * float(2)
    print(round(der))
elif activity_p == 7 :
    der = round(rer) * float(3)
    print(round(der))
elif activity_p == 8 :
    der = round(rer) * float(6)
    print(round(der))
else:
    print("nieprawodłowy wybór")














#1- niekastrowane #k = 1,8
#2- kastrowane #k = 1,6
#3- mało aktywne, z nadwagą #k = 1,4
#4- leczenie otyłości #k = 1,0
#5- w okresie rekonwalescencji #k =  1,4
#6- lekko trenujący #k = 2,0
#7- średnio #k = 3
#8- ciężko) #k = 6)
