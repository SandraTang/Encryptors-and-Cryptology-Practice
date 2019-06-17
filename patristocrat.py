#Monoalphabetic Substitution (English)
#"Patristocrat" Cipher
#by Sandra Tang

from random import randint


#intro
print "Monoalphabetic Substitution (English)"
print "\"Patristocrat\" Cipher"

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
words = ["the","of","and","a","to","in","is","you","that","it","he","was","for","on","are","as","with","his","they","I","at","be","this","have","from","or","one","had","by","word","but","not","what","all","were","we","when","your","can","said","there","use","an","each","which","she","do","how","their","if","will","up","other","about","out","many","then","them","these","so","some","her","would","make","like","him","into","time","has","look","two","more","write","go","see","number","no","way","could","people","my","than","first","water","been","call","who","oil","its","now","find","long","down","day","did","get","come","made","may","part"]

phrase_length = randint(7, 10)
phrase = ""

for i in range(phrase_length):
  phrase = phrase + words[randint(0, len(words)-1)].upper()

phrase = phrase.upper()

#phrase is built now

#now create a new alphabet
#a throw-away array
holder = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#blank array to fill in with letters from the throwaway
correlation = []

#fill in
for j in range(0,26):
  correlation.insert(randint(0, len(correlation)), holder[0])
  holder.pop(0)

encrypted_array = []
a = 0
for b in phrase:
  if b in alphabet:
    encrypted_array.append(correlation[alphabet.index(b)])
    a += 1

a = 0
encrypted = ""
for c in encrypted_array:
  encrypted = encrypted + c
  a += 1
  if a == 5:
    encrypted = encrypted + " "
    a = 0

print "Guess the original statement! This is the encrypted code:"
print encrypted

#guessing time

guess = ""

while not guess.upper() == phrase:
  guess = raw_input("Your encryption: ")

print "You did it! The encrypted message is %s" % phrase
