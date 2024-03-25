from distutils.command.clean import clean
import sys
import random
import string

password = []
charakters_left = -1

def update_characters_left(number_of_character):
    global charakters_left
    if number_of_character <0 or number_of_character > charakters_left:
        print("liczba znaków wykracza poza zakres: < 0 ;", charakters_left, ">")
        sys.exit(0)
    else:
        charakters_left -= number_of_character
        print("Pozstało jeszcze: ", charakters_left, "znaków")

password_length = int(input("Ile znaków ma mieć hasło? "))

if password_length < 6 :
    print("Hasło za krótkie. Użyj minimum 6 znaków.")
    sys.exit(0)
else:
    charakters_left = password_length
    
# Małe znaki
lowercase_letters = int(input("Ile małych liter ma mieć hasło?"))
update_characters_left(lowercase_letters)

# Duże znaki
uppercase_letters = int(input("Ile dużych liter ma mieć hasło?"))
update_characters_left(uppercase_letters)

# Znaki specjalne
special_characters = int(input("Ile znaków specjalnych ma mieć hasło?"))
update_characters_left(special_characters)

# Cyfry
digits = int(input("Ile cyfr ma mieć hasło?"))
update_characters_left(digits)

if charakters_left > 0:
    print("Nie wszystkie znaki zostały wykorzystane.Hasło zostanie uzupełnione o małe litery.")
    lowercase_letters += charakters_left
    
print()
print("Długość hasła wynosi: ", password_length, "a w nim: ")
print("Małe litery: ", lowercase_letters)
print("Duże litery: ", uppercase_letters)
print("Znaki specjalne: ", special_characters)
print("Cyfry: ", digits)

for _ in range(password_length):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(password)
print("Wygenerowane hasło:", "".join(password))