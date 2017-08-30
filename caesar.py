#Tehty https://inventwithpython.com/chapter14.html mallin avulla

import sys

#Vakio, joka määrittää siirtojen ylärajan
MAX_SHIFT = 26

#Caesar -salakirjoituksen funktio, joka käy läpi käyttäjän antaman viestin ja muuttaa viestin siirtojen perusteella
def caesar(message, shift):
    cipher = ''
    for ch in message:
        if ch.isalpha():
            num = ord(ch) + shift
            if ch.isupper():
                if num > ord('Z'):
                    num -= MAX_SHIFT
                elif num < ord('A'):
                    num += MAX_SHIFT
            if ch.islower():
                if num > ord('z'):
                    num -= MAX_SHIFT
                elif num < ord('a'):
                    num += MAX_SHIFT
            cipher += chr(num)
        else:
            cipher += ch
    return cipher

#Main -funtkio, josta voidaan salata selkoteksti, purkaa salakirjoitus tai poistua ohjelmasta
if __name__=="__main__":
    message = ""
    shift = 0

    while True:
        try:
            choice = int(input("1 - Salaa\n2 - Pura salaus\n0 - Lopeta\n"))
            if choice == 1:
                message = input("Anna selkotekstisi: ")
                while shift > 26 or shift < 1:
                    shift = int(input("Anna siirrosten maara (1-26): "))
                    if shift > 26 or shift < 1:
                        print("Virheellinen siirrosten maara")
                print(caesar(message, shift))
            elif choice == 2:
                message = input("Anna salattu tekstisi: ")
                for shift in range(1, MAX_SHIFT + 1):
                        print("{} ".format(shift) + caesar(message, shift))
            elif choice == 0:
                sys.exit(0)
        except ValueError:
            print("Syottovirhe")
