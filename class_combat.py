import class_pkm
import class_attaque
import random
import json
class combat():

    def __init__(self,poke1,poke2):
        self.poke1 = poke1
        self.poke2 = poke2

    def speed (self):
        if self.poke1.spe > self.poke2.spe:
            self.first = self.poke1
            self.last = self.poke2
        elif self.poke1.spe < self.poke2.spe:
            self.first = self.poke2
            self.last = self.poke1
        else :
            pokemons = [self.poke1, self.poke2]
            self.first = random.choice(pokemons)
            pokemons.remove(self.first)
            self.last = pokemons[0]

    def affinity (self,attaque,poke_def):
        self.attaque = attaque
        self.poke_def = poke_def
        if self.attaque.type == "Plante" and self.poke_def.type == "Eau":
            return 2
        elif self.attaque.type == "Eau" and self.poke_def.type == "Feu":
            return 2
        elif self.attaque.type == "Feu" and self.poke_def.type == "Plante":
            return 2
        elif self.attaque.type == "Spectre" and self.poke_def.type == "Spectre":
            return 2
        elif self.attaque.type == "Plante" and self.poke_def.type == "Plante":
            return 0.5
        elif self.attaque.type == "Plante" and self.poke_def.type == "Feu":
            return 0.5
        elif self.attaque.type == "Feu" and self.poke_def.type == "Feu":
            return 0.5
        if self.attaque.type == "Feu" and self.poke_def.type == "Eau":
            return 0.5
        elif self.attaque.type == "Eau" and self.poke_def.type == "Eau":
            return 0.5
        elif self.attaque.type == "Eau" and self.poke_def.type == "Plante":
            return 0.5
        elif self.attaque.type == "Normal" and self.poke_def.type == "Spectre":
            return 0
        elif self.attaque.type == "Spectre" and self.poke_def.type == "Normal":
            return 0
        else:
            return 1
        
    def precision (self,attaque):
        self.attaque = attaque
        number = random.randint(1, 100)
        if self.attaque.precision >= number:
            return True
        else:
            return False
        
    def fin_combat (self):
        True
        if self.poke1.pv <= 0 or self.poke2.pv <= 0 :
            print ("Combat fini")
            self.testx = False
    
    def stab (self, attaque, poke):
        if attaque.type == poke.type:
            return 1.5
        else:
            return 1
    
    def calcul_damage (self,attaque,poke_att,poke_def):
        number = random.uniform(0.85, 1)
        cm = self.stab(attaque, poke_att)*self.affinity(attaque, poke_def)*number
        if attaque.classe == "Physique":
            damage = round(abs((abs(abs((abs(poke_att.lv*0.4+2)*poke_att.atk*attaque.puissance)/poke_def.defense)/50)+2)*cm))
            print (damage)
        elif attaque.classe == "Spécial":
            damage = round(abs((abs(abs((abs(poke_att.lv*0.4+2)*poke_att.atk_spe*attaque.puissance)/poke_def.def_spe)/50)+2)*cm))
            print (damage)
        return damage
    
    def en_combat(self):
        self.testx = True
        while self.testx:
            for i in range (0, len (self.poke1.attaques)):
                print(f"attaques : {self.poke1.attaques[i]["nom"]}")
            n = int(input("joueur 1 choisi attaque "))
            id = self.poke1.atk_id[n-1]
            atk_poke1 = class_attaque.Attaque(id)
            for i in range (0, len (self.poke2.attaques)):
                print(f"attaques : {self.poke2.attaques[i]["nom"]}")
            n = int(input("joueur 2 choisi attaque "))
            id = self.poke1.atk_id[n-1]
            atk_poke2 = class_attaque.Attaque(id)
            self.speed()
            print (self.first.nom)
            if self.first == self.poke1:
                self.poke2.loose_pv(self.calcul_damage(atk_poke1,self.poke1,self.poke2))
                print (self.calcul_damage(atk_poke1,self.poke1, self.poke2),"pv inflige, pv restant :",self.poke2.pv)
                self.fin_combat ()
                self.poke1.loose_pv(self.calcul_damage(atk_poke2,self.poke2,self.poke1))
                print (self.calcul_damage(atk_poke2,self.poke2,self.poke1),"pv inflige, pv restant :",self.poke1.pv)
                self.fin_combat ()
            elif self.first == self.poke2:
                self.poke1.loose_pv(self.calcul_damage(atk_poke2,self.poke2,self.poke1))
                print (self.calcul_damage(atk_poke2,self.poke2, self.poke1),"pv inflige, pv restant :",self.poke1.pv)
                self.fin_combat ()
                self.poke2.loose_pv(self.calcul_damage(atk_poke1,self.poke1,self.poke2))
                print (self.calcul_damage(atk_poke1,self.poke1,self.poke2),"pv inflige, pv restant :",self.poke2.pv)
                self.fin_combat ()

with open("pokedex.json", "r") as f:
    pokedex = json.load(f)
pokemon_29 = pokedex.get("1")
pokemon_10 = pokedex.get("4")
test = class_pkm.pkm(pokemon_29, 50)
test2 = class_pkm.pkm(pokemon_10,50)
print(f"Nom du Pokémon : {test.nom}")
print(f"Type du Pokémon : {test.type}")
print(f"pv : {test.pv}")
''"test.evol ()"''
print(f"Nom du Pokémon : {test.nom}")
print(f"Type du Pokémon : {test.type}")
print(f"pv : {test.pv}")
print(f"Nom du Pokémon : {test2.nom}")
print(f"Type du Pokémon : {test2.type}")
print(f"pv : {test2.pv}")
fight = combat(test,test2)
fight.en_combat()