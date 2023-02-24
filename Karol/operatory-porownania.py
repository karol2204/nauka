"""
>    większy niż	
<    mniejszy niż
==   równy
!=   nierówny
>=   większy bądź równy
<=   mniejszy bądź równy

"""
choose = input("* - mnożenie,  / - dzielenie, + - dodawanie, - dejmowanie, ** - potęgowanie, // - dzielnie w dół: ")

a = int(input("Pierwsza liczba: "))
b = int(input("Druga liczba: "))



if (choose == "*"):
    print(a * b)
elif (choose == "/"):
    if (b == 0):
        print ("Zły dzielnik")
    else:
        print(a / b)
elif (choose == "+"):
    print(a + b)
elif (choose == "-"):
    print (a - b)
elif (choose == "**"):
    print (a ** b)
elif (choose == "//"):
    print (a // b)
    if (b == 0):
        print ("Zły dzielnik")
    else:
        print (a // b)
else:
    print ( "nie dokonałeś własciego wyboru" )
print (choose)
