from random import randint
class Pokemon :
    def __init__ (self, nom, vie, atck, deff, atck_spe, deff_spe, speed, atribut, lvl, xp) :
        self.__nom = nom
        self.__vie = vie
        self.__atck = atck
        self.__deff = deff
        self.__atck_spe = atck_spe
        self.__deff_spe = deff_spe
        self.__speed = speed 
        self.__atribut = atribut
        self.__lvl = lvl
        self.__xp = xp

    def to_dict(self):
        return {
            'nom': self.__nom,
            'vie': self.__vie,
            'atck': self.__atck,
            'deff': self.__deff,
            'atck_spe': self.__atck_spe,
            'deff_spe': self.__deff_spe,
            'speed': self.__speed,
            'atribut': self.__atribut,
            'lvl': self.__lvl,
            'xp': self.__xp
        }
    @staticmethod
    def from_dict(data):
        return Pokemon(
            data['nom'],
            data['vie'],
            data['atck'],
            data['deff'],
            data['atck_spe'],
            data['deff_spe'],
            data['speed'],
            data['atribut'],
            data['lvl'],
            data['xp']
        )
    
    def info(self):
        print("Nom: ", self.__nom)
        print("Vie: ", self.__vie)
        print("Atck: ", self.__atck)
        print("Deff: ", self.__deff)
        print("Atck Spe: ", self.__atck_spe)
        print("Deff Spe: ", self.__deff_spe)
        print("Speed: ", self.__speed)
        print("Atribut: ", self.__atribut)
        print("Lvl: ", self.__lvl)
        print("Xp: ", self.__xp)

import json
'''
# Create a Pokemon object
pokemon = Pokemon('Pikachu', 100, 55, 40, 55, 50, 90, 'Electric', 5, 100)

# Convert the Pokemon object to a dictionary
pokemon_dict = pokemon.to_dict()

# Save the dictionary to a JSON file
with open('pokemon.json', 'w') as f:
   json.dump(pokemon_dict, f)
'''

# Load the dictionary from a JSON file
with open('pokemon.json', 'r') as f:
   pokemon_dict = json.load(f)

# Convert the dictionary to a Pokemon object
pokemon = Pokemon.from_dict(pokemon_dict)

pokemon.info ()