from time import time
from sys import exit
import cryptomath, random
from argparse import ArgumentParser
from catalan import catalan

SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
timeStart = time()


def main(myMode=None, cypher=None, localFile=''):
    myMessage = "Blue is the colour, football is the game We're all together, and winning is our aim So cheer us on through the sun and rain 'cause Chelsea, Chelsea is our name."
    #myMessage = """"fX<*h>}(rTH<Rh()?<?T]TH=T<rh<tT<*_))T?<ISrT))I~TSr<Ii<Ir<*h()?<?T*TI=T<_<4(>_S<ISrh<tT)IT=IS~<r4_r<Ir<R_]<4(>_SEf<0X)_S<k(HIS~"""
    if cypher == 'catalan':
        catalan()
    elif cypher == 'random':
        random()
    myKey = 2023
    myMode = 'encrypt' # ustawiamy 'encrypt' lub 'decrypt'

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    print('Key: %s' % (myKey))
    print('%sed text:' % (myMode.title()))
    print(translated)


def getKeyParts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)


def checkKeys(keyA, keyB, mode):  # Sprawdzenie poprawności klucza
    if keyA == 1 and mode == 'encrypt':
        exit('Szyfr afiniczny staje się niewiarygodnie słaby, gdy klucz A jest ustawiony na 1. Wybierz inny klucz.')
    if keyB == 0 and mode == 'encrypt':
        exit('Szyfr afiniczny staje się niewiarygodnie słaby, gdy klucz B jest ustawiony na 0. Wybierz inny klucz.')
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        exit('Klucz A musi być więszy niż 0, a klucz B musi być z przedziału (0 , %s.)' % (len(SYMBOLS) - 1))
    if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
        exit('Kklucz A (%s) and rozmiar zestawu symboli (%s) nie są względnie pierwsze Choose a different key.' % (keyA, len(SYMBOLS)))


def encryptMessage(key, message):  # Szyfrowanie wiadomości
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


def decryptMessage(key, message):  # Odszyfrowanie wiadomości
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


def getRandomKey():  # generowanie klucza
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB

if __name__ == '__main__':
    main()   
print('Time: ', time() - timeStart)
