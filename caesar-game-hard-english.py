#Caesar Cipher Practice Program - Hard (English)
#by Sandra Tang

print "Caesar Cipher Practice Program - Hard (English)"

from random import randint

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

phrases = ["the","of","and","a","to","in","is","you","that","it","he","was","for","on","are","as","with","his","they","I","at","be","this","have","from","or","one","had","by","word","but","not","what","all","were","we","when","your","can","said","there","use","an","each","which","she","do","how","their","if","will","up","other","about","out","many","then","them","these","so","some","her","would","make","like","him","into","time","has","look","two","more","write","go","see","number","no","way","could","people","my","than","first","water","been","call","who","oil","its","now","find","long","down","day","did","get","come","made","may","part"]

words = randint(2,6)
decrypted = ""

for i in range(words):
  decrypted = decrypted + phrases[randint(0, len(phrases)-1)].upper()

encrypted = ""

shift = randint(1, 25)

for char in decrypted:
  encrypted = encrypted + alphabet[(alphabet.index(char) + shift) % 26]

print encrypted

guess = ""

print "Try to crack the Caesar Cipher!"
print "The phrase you need to decrypt is two to five words put together."

while not guess.upper() == decrypted:
  guess = raw_input("Guess: ")

print "You guessed it! The decrypted phrase is %s." % decrypted
