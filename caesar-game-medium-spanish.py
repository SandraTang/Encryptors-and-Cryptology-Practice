#Caesar Cipher Practice Program - Medium (Spanish)
#by Sandra Tang

print "Caesar Cipher Practice Program - Medium (Spanish)"

from random import randint

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

phrases = ["hola", "uno", "dos", "bueno", "buen", "tardes", "noches", "me", "mi", "tu", "llamo", "como", "usted", "estoy", "bien", "mucho", "gusto", "adios", "hasta", "luego", "perdido", "donde", "con", "pan", "por", "favor", "gracias", "lo", "el", "la", "siento", "salud", "de", "nada", "si", "no", "habla", "quien", "por", "que", "porque"]

words = randint(2,6)
decrypted = ""

for i in range(words):
  decrypted = decrypted + " " + phrases[randint(0, len(phrases)-1)].upper()

decrypted = decrypted[1:]
encrypted = ""

shift = randint(1, 25)

for char in decrypted:
  if char == " ":
    encrypted = encrypted + " "
  else:
    encrypted = encrypted + alphabet[(alphabet.index(char) + shift) % 27]

print encrypted

guess = ""

print "Try to crack the Caesar Cipher!"
print "The phrase you need to decrypt is two to five words put together."

while not guess.upper() == decrypted:
  guess = raw_input("Guess: ")

print "You guessed it! The decrypted phrase is %s" % decrypted
