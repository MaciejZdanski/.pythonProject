import cryptomath
import random
import time

SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""


def main():
    mode = input("Wybierz tryb pracy (encrypt/e lub decrypt/d): ")
    if mode.lower() not in ['encrypt', 'e', 'decrypt', 'd']:
        print("Nieprawidłowy tryb pracy.")
        return

    if mode.lower() in ['encrypt', 'e']:
        myMessage = input("Podaj wiadomość do zaszyfrowania: ")
    else:
        myMessage = input("Podaj wiadomość do odszyfrowania: ")

    key_type = input("Wybierz rodzaj klucza (własny/w lub catalan/c): ")
    if key_type.lower() not in ['własny', 'w', 'catalan', 'c']:
        print("Nieprawidłowy rodzaj klucza.")
        return

    if key_type.lower() in ['własny', 'w']:
        myKey = int(input("Podaj wartość klucza (z przedziału 1111-9999): "))
    else:
        catalan_index = int(input("Podaj numer wyrazu w ciągu catalana: "))
        myKey = catalan(catalan_index)

    start_time = time.time()

    if mode.lower() == 'encrypt' or mode.lower() == 'e':
        translated = encryptMessage(myKey, myMessage)
        print('Zaszyfrowana wiadomość:')
        print(translated)

        with open('cryptogram.txt', 'w') as f:
            f.write(translated)

    else:
        translated = decryptMessage(myKey, myMessage)
        print('Odszyfrowana wiadomość:')
        print(translated)

    end_time = time.time()
    print("Czas wykonania: ", end_time - start_time)


def catalan(n):
    if n == 0:
        return 1
    catalan_numbers = [0] * (n + 1)
    catalan_numbers[0] = 1

    for i in range(1, n + 1):
        catalan_numbers[i] = 0
        for j in range(i):
            catalan_numbers[i] += catalan_numbers[j] * catalan_numbers[i - 1 - j]

    return catalan_numbers[n]


def getKeyParts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return keyA, keyB


def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        exit('Klucz A nie może być równy 1. Wybierz inny klucz.')
    if keyB == 0 and mode == 'encrypt':
        exit('Klucz B nie może być równy 0. Wybierz inny klucz.')
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        exit('Klucz A musi być większy lub równy 0, a klucz B musi być z przedziału (0, %s).' % (len(SYMBOLS) - 1))
    if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
        exit('Klucz A (%s) i rozmiar zestawu symboli (%s) nie są względnie pierwsze. Wybierz inny klucz.' % (
            keyA, len(SYMBOLS)))


def encryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    ciphertext = ''

    for symbol in message:
        if symbol in SYMBOLS:
            symIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            ciphertext += symbol
    return ciphertext


def decryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'decrypt')
    plaintext = ''
    modInverseOfKeyA = cryptomath.findModInverse(keyA, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            symIndex = SYMBOLS.find(symbol)
            plaintext += SYMBOLS[(symIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
        else:
            plaintext += symbol
    return plaintext


if __name__ == '__main__':
    main()
