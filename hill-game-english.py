#Hill Cipher Practice Program (English)
#by Sandra Tang

print "Hill Cipher Practice Program (English)"

from random import randint

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
phrases = ["the", "and", "you","that", "was","for","are","with","his","they","this","have","from","one","had","word","but","not","what","all","were","when","your","can","said","there","use","each","which","she","how","their","will","other","about","out","many","then","them","these","some","her","would","make","like","him","into","time","has","look","two","more","write","see","number","way","could","people","than","first","water","been","call","who","oil","its","now","find","long","down","day","did","get","come","made","may","part"]
keys = ["that", "dogs", "with", "have", "from", "your", "they", "know", "want", "been", "good", "much", "some", "time", "true", "clap", "free", "must"]

decrypted = ""
decrypted = phrases[randint(0, len(phrases)-1)].upper()
word = decrypted
d_array = []
for c in decrypted:
  d_array.append(c)

key = ""
key = keys[randint(0, len(keys)-1)].upper()
key_word = key
k_array = []
for c2 in key:
  k_array.append(c2)

for i in range(0, len(d_array)):
  d_array[i] = alphabet.index(d_array[i])

for i2 in range(0, len(k_array)):
  k_array[i2] = alphabet.index(k_array[i2])

even = True
if len(d_array) % 2 == 1:
  d_array.append(0)
  even = False

encrypted = []
for j in range(0, int(len(d_array)/2)):
  d_array[j] = (k_array[0]*int(d_array[j]) + k_array[1]* int(d_array[j+1]))%26
  d_array[j+1] = (k_array[2]*int(d_array[j]) + k_array[3]* int(d_array[j+1]))%26

for i3 in range (0, len(d_array)):
  d_array[i3] = alphabet[d_array[i3]]

encrypted = ""
for c3 in d_array:
  encrypted = encrypted + str(c3)

if not even:
  encrypted = encrypted[:len(encrypted)-1]

#Instructions

print "The word to encrypt is: " + word
print "The word for the key matirx is " + key_word
print "Encrypt the word!"
print

#Interaction

guess = ""

while not guess.upper() == encrypted:
  guess = raw_input("Your Answer: ")

print "You're correct! The encrypted code is %s" % encrypted
