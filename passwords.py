import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? "))
nr_numbers = int(input("How many numbers would you like in your password? "))
nr_symbols = int(input("How many symbols would you like in your password? "))


password = ""

for char in range(0, nr_letters):
    letter = random.choice(letters)
    password += letter

for num in range(0, nr_numbers):
    number = random.choice(numbers)
    password += number
for sym in range(0, nr_symbols):
    symbol = random.choice(symbols)
    password += symbol

print("Your password is: ",password)

listPassword = list(password)
#print(listPassword)
random.shuffle(listPassword)
#print(listPassword)
final_password = ""


for char in listPassword:
    final_password += char   

print("Your final password is: ",final_password)



