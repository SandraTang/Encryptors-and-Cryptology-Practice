#Affine Cipher Encryptor (Spanish)
#by Sandra Tang

from random import randint

# (ax + b) % m

#intro
print "Affine Cipher Encryptor (Spanish)"

#value of a
a = raw_input("Value of a: ")
a_int = True

try:
   val = int(a)
except ValueError:
   a_int = False
   
while a_int == False:
  print "That's not an int. Try again."
  a = raw_input("Value of a: ")
  a_int = True
  try:
    val = int(a)
  except ValueError:
    a_int = False

#value of b
b = raw_input("Value of b: ")
b_int = True

try:
   val = int(b)
except ValueError:
   b_int = False
   
while b_int == False:
  print "That's not an int. Try again."
  b = raw_input("Value of b: ")
  b_int = True
  try:
    val = int(b)
  except ValueError:
    b_int = False

word = raw_input("What do you want to encrypt?").upper()

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = []

for c in word:
  if c == " ":
    numbers.append(" ")
  else:
    numbers.append(alphabet.index(c))

encrypted = []

for x in numbers:
  encrypted.append( ((int(a)*int(x))+int(b))%27 )

code = ""

for n in encrypted:
  code = code + alphabet[n]

print "The affine encryption of " + word + " is " + code + "."
