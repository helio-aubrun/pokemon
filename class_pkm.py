import json
import class_attaque
from math import floor
class pkm():

    def __init__(self, id, lv=1):
        self.nom = id.get("nom")
        self.type = id.get("Type")
        self.talent = id.get("talent")
        self.pv = floor(abs(((2*id.get("pv")+31)*lv)/100)+lv+10)
        self.pv_max = self.pv = floor(abs(((2*id.get("pv")+31)*lv)/100)+lv+10)
        self.atk = floor(abs(abs((2*id.get("atk")+31)*lv / 100)+5))
        self.defense = floor(abs(abs((2*id.get("def")+31)*lv / 100)+5))
        self.atk_spe = floor(abs(abs((2*id.get("atk_spe")+31)*lv / 100)+5))
        self.def_spe = floor(abs(abs((2*id.get("def_spe")+31)*lv / 100)+5))
        self.spe = floor(abs(abs((2*id.get("spe")+31)*lv / 100)+5))
        self.exp = id.get("exp")
        self.lv = lv
        self.evo = id.get("evo")
        self.id = id.get("id")
        self.atk_id = id.get("attaques")
        self.attaques = []
        for i in range(len(id.get("attaques"))):
            self.attaques.append(class_attaque.Attaque(id.get("attaques")[i]).attaque)
        self.sauvage = True
        self.hp_max = floor(abs(((2*id.get("pv")+31)*lv)/100)+lv+10)

    def levelup(self):
        self.lv+=1
        self.__init__(self.id, self.lv)
        print (self.pv)

    def heal(self):
        self.pv = self.pv_max

    def evol (self):
        with open("pokedex.json","r") as f :
            pokedex = json.load(f)
        new_id = str(self.id+1)
        self.__init__(pokedex[new_id], self.lv)

    def loose_pv(self,damage):
        self.pv-=damage

class pkm_dress(pkm):

    def __init__(self, id, lv=1):
        self.barre_exp = 0
        self.lv = lv
        self.sauvage = False
        pkm.__init__(self, id, self.lv)
    
    def gain_exp(self, poke_adv):
        exp_gagné = (poke_adv.exp * poke_adv.lv)
        self.barre_exp+=exp_gagné
        print ("exp gagné", exp_gagné)
        print ("exp actuel", self.barre_exp)
        while self.barre_exp <= 0.8 * (self.lv**3) and self.lv >100:
            self.lv+=1
            self.__init__(self.id, self.lv)
        if self.lv >= self.evo:
            with open("pokedex.json","r") as f :
                pokedex = json.load(f)
            new_id = str(self.id+1)
            self.__init__(pokedex[new_id], self.lv)

class pkm_adv(pkm):

    def __init__(self, id, lv=1):
        self.lv = lv
        self.sauvage = False
        pkm.__init__(self, id, self.lv)