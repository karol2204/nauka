import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


temp_letters = random.sample(letters,nr_letters)

temp_symbols = random.sample(symbols,nr_symbols)

temp_numbers = random.sample(numbers,nr_numbers)


#password = letters_choice + symbols_choice + numbers_choice
password = temp_letters + temp_symbols + temp_numbers
random.shuffle(password)
print("".join(password))

letters2 = []
for letter in range(0,nr_letters):
    letters2 += random.choice(letters)
#print(letters2)

numbers2 = []
for letter in range(0,nr_numbers):
    numbers2 += random.choice(numbers)
#print(numbers2)

symbols2 = []
for letter in range(0,nr_symbols):
    symbols2 += random.choice(symbols)
#print(symbols2)

password = letters2 + numbers2 + symbols2
random.shuffle(password)
print("".join(password))
