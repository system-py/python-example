import os
import time
from playsound import playsound

morse = {
    'a': '.- ',
    'b': '-... ',
    'c': '-.-. ',
    'd': '-.. ',
    'e': '. ',
    'f': '..-. ',
    'g': '--. ',
    'h': '.... ',
    'i': '.. ',
    'j': '.--- ',
    'k': '-.- ',
    'l': '.-.. ',
    'm': '-- ',
    'n': '-. ',
    'o': '--- ',
    'p': '.--. ',
    'q': '--.- ',
    'r': '.-. ',
    's': '... ',
    't': '- ',
    'u': '..- ',
    'v': '...- ',
    'w': '.-- ',
    'x': '-..- ',
    'y': '-.-- ',
    'z': '--.. ',
    '1': '.---- ',
    '2': '..--- ',
    '3': '...-- ',
    '4': '....- ',
    '5': '..... ',
    '6': '-.... ',
    '7': '--... ',
    '8': '---.. ',
    '9': '----. ',
    '0': '----- ',
    '.': '.-.-.- ',
    ',': '--..-- ',
    '?': '..--.. ',
    ' ': '/ ', }

veri = input("Morse için veri giriniz: ")


def morse_cevir():
    morse_verisi = ""
    for veri_chr in (veri.lower()):
        morse_chr = morse[veri_chr]
        morse_verisi = morse_verisi + morse_chr
    return morse_verisi


print(morse_cevir())

"""
for chr in morse_cevir():
    if chr == "-":
        os.system('cvlc --play-and-exit beep-06.mp3')
    if chr == ".":
        os.system("cvlc --play-and-exit beep-07.mp3")
    else:
        time.sleep(1)

"""

for chr in morse_cevir():
    if chr == "-":
        playsound('beep-06.wav')
    if chr == ".":
        playsound("beep-07.wav")
    else:
        time.sleep(0.5)

print("Veri = %s" % veri + " "+"Morse verisi = %s" % morse_cevir())

