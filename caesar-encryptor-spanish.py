#Caesar Cipher Encryptor (Spanish)
#by Sandra Tang

print "Caesar Cipher Encryptor (Spanish)"

from random import randint

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

decrypted = raw_input("What do you want to encrypt? ").upper()

d_valid = True

for c in decrypted:
  if not (c.isalpha() or c == "Ñ"):
    d_valid = False

while not d_valid:
  print "Letters only! Try again. "
  decrypted = raw_input("What do you want to encrypt? ").upper()
  d_valid = True
  for c in decrypted:
    if not (c.isalpha() or c == "Ñ"):
      d_valid = False

encrypted = ""

shift = raw_input("What is the shift? It should be an integer. ")
shift_int = True

try:
  val_shift = int(shift)
except ValueError:
  shift_int = False
  
while shift_int == False:
  print "That's not an integer. Try again."
  shift = raw_input("What is the shift? ")
  shift_int = True
  try:
    val_shift = int(shift)
  except ValueError:
    shift_int = False

for char in decrypted:
  if char in alphabet:
    encrypted = encrypted + alphabet[(alphabet.index(char) + int(shift)) % 27]
  else:
    encrypted = encrypted + " "
    

print "The encrypted code is %s." % encrypted
