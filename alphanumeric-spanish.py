#Letter Numbers Quiz Game (Spanish)
#By Sandra Tang

from random import randint

print "Letter Numbers Quiz Game (Spanish)"

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

print "Alphanumeric Quiz"

print "State the correlating number to the letter."

while 2 == 2:
  answer = randint(0, len(alphabet)-1)
  print alphabet[answer]
  guess = ""
  
  while not answer == guess:
      guess = raw_input("Guess: ")
      guess = int(guess)
  
  print "You got it! Here's another."
  print
