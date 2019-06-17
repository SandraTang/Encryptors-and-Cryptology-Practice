#Affine Cipher Practice Program (English)
#by Sandra Tang

from random import *

#choose a
possible_a = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
a = possible_a[randint(0, len(possible_a)-1)]

#choose b
b = randint(1, 25)

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
words = ["the","of","and","a","to","in","is","you","that","it","he","was","for","on","are","as","with","his","they","I","at","be","this","have","from","or","one","had","by","word","but","not","what","all","were","we","when","your","can","said","there","use","an","each","which","she","do","how","their","if","will","up","other","about","out","many","then","them","these","so","some","her","would","make","like","him","into","time","has","look","two","more","write","go","see","number","no","way","could","people","my","than","first","water","been","call","who","oil","its","now","find","long","down","day","did","get","come","made","may","part"]

phrase_length = randint(1, 3)
phrase = ""

for i in range(phrase_length):
  phrase = phrase + " " + words[randint(0, len(words)-1)].upper()

phrase = phrase[1:]

#play the game
print "Affine Cipher Practice Program (English)"
print "Encrypt the following phrase with the Affine Cipher."
print phrase
print "The value of a: " + str(a)
print "The value of b: " + str(b)

#solve it
numbers = []

#change letters to numbers
for c in phrase:
  if c == " ":
    numbers.append(" ")
  else:
    numbers.append(alphabet.index(c))

encrypted = []

#numbers to encrypted numbers
for x in numbers:
  if x == " ":
    encrypted.append(" ")
  else:
    encrypted.append( ((int(a)*int(x))+int(b))%26 )

code = ""

for n in encrypted:
  if n == " ":
    code = code + " "
  else:
    code = code + alphabet[n]

#guessing time

guess = ""

while not guess.upper() == code:
  guess = raw_input("Your encryption: ")

print "You did it! The encrypted code is %s" % code
