import random

class IAPlayer:
   def choose_attack(self, available_attacks):
       return random.choice(available_attacks)