import os
import numpy as np

#OUTPUT INDICES
NUMBER = 0
FIZZ = 1
BUZZ = 2
FIZZBUZZ = 3

class Cli:
  def __init__(self, parser, model, bits):
    self.parser = parser
    self.model = model
    self.bits = bits
    print('Bienvenue sur votre fizzbuzz neuronal ! Rentrez un nombre \
inférieur à ' + str(2 ** self.bits) + ' pour accéder à sa prédiction fizzbuzz, ou bien \
tapez "quit" pour quitter le programme.')

  def run(self):
    while True:
      userInput = input('Quel est votre nombre ? (entre 0 et ' + str(2 ** self.bits) + ' exclus)\n')
      data = self.parser.processLine(userInput.replace(' ', ''))
      if (int(data) >= 2 ** self.bits):
        print("Erreur: Le nombre reçu est trop grand, il doit être entre 0 et " + str((2 ** self.bits) - 1) + " inclus")
      elif (int(data) == -1):
        print("Erreur: L'entrée reçue n'est ni un nombre positif, ni une commande connue.\n\
Entrez 'quit' pour sortir du programme.")

      else:
        bits = [int(bit) for bit in np.binary_repr(int(data), self.bits)]
        prediction = self.model.predict([bits])[0]
        
        if (prediction[NUMBER] == 1):
          print(data)
        elif (prediction[FIZZ] == 1):
          print('Fizz!')
        elif (prediction[BUZZ] == 1):
          print('Buzz!')
        elif (prediction[FIZZBUZZ] == 1):
          print('FizzBuzz!')