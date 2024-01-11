import json
from math import floor
class pkm():

    def __init__(self, id, lv=1):
        self.nom = id.get("nom")
        self.type = id.get("Type")
        self.talent = id.get("talent")
        self.pv = floor(abs(((2*id.get("pv")+31)*lv)/100)+lv+10)
        self.atk = floor(abs(abs((2*id.get("atk")+31)*lv / 100)+5))
        self.defense = floor(abs(abs((2*id.get("def")+31)*lv / 100)+5))
        self.atk_spe = floor(abs(abs((2*id.get("atk_spe")+31)*lv / 100)+5))
        self.def_spe = floor(abs(abs((2*id.get("def_spe")+31)*lv / 100)+5))
        self.spe = floor(abs(abs((2*id.get("spe")+31)*lv / 100)+5))
        self.exp = id.get("exp")
        self.lv = lv
        self.atk_possible = []
        self.atk_apprise = []
        self.evo = id.get("evo")
        self.id = id.get("id")

    '''def levelup(self):
        self.lv+=1
        self.__init__(self.id, self.lv)
        print (self.pv)'''

    def evol (self):
        with open("pokedex.json","r") as f :
            pokedex = json.load(f)
        new_id = str(self.id+1)
        self.__init__(pokedex[new_id], self.lv)

class pkm_dress(pkm):

    def __init__(self, id, lv=1):
        pkm.__init__(self, id, lv=1)
        self.barre_exp = 0
        self.lv = lv
    
    '''def gain_exp(self):
        exp_gagné = (adv.exp * adv.lv) // (7 * joueur.nb_pk)
        self.barre_exp+=exp_gagné
        while self.barre_exp <= self.lv*100 and self.lv >100:
            self.lv+=1
            self.__init__(self.id, self.lv)
        if self.lv >= self.evo:
            with open("pokedex.json","r") as f :
                pokedex = json.load(f)
            self.id+=1
            self.__init__(self.id, self.lv)'''

class pkm_adv(pkm):

    def __init__(self, id, attaques, lv=1):
        pkm.__init__(self, id, lv=1)
        self.lv = lv
        self.attaques = attaques

with open("pokedex.json", "r") as f:
    pokedex = json.load(f)
pokemon_30 = pokedex.get("30")
if pokemon_30:
    test = pkm(pokemon_30, 99)
    print(f"Nom du Pokémon : {test.nom}")
    print(f"Type du Pokémon : {test.type}")
    print(f"pv : {test.pv}")
    test.evol ()
    print(f"Nom du Pokémon : {test.nom}")
    print(f"Type du Pokémon : {test.type}")
    print(f"pv : {test.pv}")