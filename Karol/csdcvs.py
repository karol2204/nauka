a = 1
while a < 4:
    for i in range (4):
        liczbaDodawana = int(input("Podaj cyfre: "))
        if (liczbaDodawana > 0):
            print("Podaj następną cyfrę: ")
        elif (liczbaDodawana < 0):
            print("Podaj cyfrę dodatnią:")
            
a += 1
