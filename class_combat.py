import class_pkm
import class_attaque
import random
import json
import class_dress_enemy
import ia

class combat():

    def __init__(self):
        self.testx = True

    def speed (self):
        #choisi qui commence en fonction de la vitesse
        if self.poke1.spe > self.poke2.spe:
            self.first = self.poke1
            self.last = self.poke2
        elif self.poke1.spe < self.poke2.spe:
            self.first = self.poke2
            self.last = self.poke1
        else :
            #si vitesse egale alors choix aleatoire
            pokemons = [self.poke1, self.poke2]
            self.first = random.choice(pokemons)
            pokemons.remove(self.first)
            self.last = pokemons[0]

    def affinity (self,attaque,poke_def):
        self.attaque = attaque
        self.poke_def = poke_def
        prod = 1
        i= 0
        #parcour la liste des types pour renvoyer le multiplicateur de degat
        for i in range(len(self.poke_def.type)):
            if self.attaque.type == "Plante" and self.poke_def.type[i] == "Eau":
                prod = prod * 2
            elif self.attaque.type == "Eau" and self.poke_def.type[i] == "Feu":
                prod = prod *  2
            elif self.attaque.type == "Feu" and self.poke_def.type[i] == "Plante":
                prod = prod *  2
            elif self.attaque.type == "Spectre" and self.poke_def.type[i] == "Spectre":
                prod = prod * 2
            elif self.attaque.type == "Plante" and self.poke_def.type[i] == "Plante":
                prod = prod * 0.5
            elif self.attaque.type == "Plante" and self.poke_def.type[i] == "Feu":
                prod = prod * 0.5
            elif self.attaque.type == "Feu" and self.poke_def.type[i] == "Feu":
                prod = prod * 0.5
            if self.attaque.type == "Feu" and self.poke_def.type[i] == "Eau":
                prod = prod * 0.5
            elif self.attaque.type == "Eau" and self.poke_def.type[i] == "Eau":
                prod = prod * 0.5
            elif self.attaque.type == "Eau" and self.poke_def.type[i] == "Plante":
                prod = prod * 0.5
            elif self.attaque.type == "Normal" and self.poke_def.type[i] == "Spectre":
                prod = prod * 0
            elif self.attaque.type == "Spectre" and self.poke_def.type[i] == "Normal":
                prod = prod * 0
            else:
                prod = prod * 1

        return prod
        
    def precision (self,attaque):
        self.attaque = attaque
        number = random.randint(1, 100)
        if self.attaque.precision >= number:
            return True
        else:
            return False
        
    def fin_combat (self):
        if self.poke1.pv <= 0 or self.poke2.pv <= 0 :
            #le poke1 sera toujours le poke joueur
            #if self.poke2.pv <= 0 :
                #self.poke1.gain_exp(self.poke2)
            #print ("Combat fini")
            False
    
    def stab (self, attaque, poke):
        #si un poke utilise une attaque de sont type, les degats sont boostés
        i=0
        for i in range(len(poke.type)):
            if attaque.type == poke.type[i]:
                return 1.5
        else:
            return 1
    
    def calcul_damage (self,attaque,poke_att,poke_def):
        #les attaques n'inflige pas toujours le max de degats, number est la puissance atribué aleatoirement
        number = random.uniform(0.85, 1)
        #cumule du stab et de l'affinité des types
        cm = self.stab(attaque, poke_att)*self.affinity(attaque, poke_def)*number
        #calcule des degats en fonction de la categorie de l'attaque, physique ou special
        if self.precision(attaque):
            if attaque.classe == "Physique":
                damage = round(abs((abs(abs((abs(poke_att.lv*0.4+2)*poke_att.atk*attaque.puissance)/poke_def.defense)/50)+2)*cm))
                #print (damage)
            elif attaque.classe == "Spécial":
                damage = round(abs((abs(abs((abs(poke_att.lv*0.4+2)*poke_att.atk_spe*attaque.puissance)/poke_def.def_spe)/50)+2)*cm))
                #print (damage)
            return damage
        else:
            return 0
    
    def choose_attack(self, poke1, poke2, n):
        self.poke1 = poke1
        self.poke2 = poke2
        id = self.poke1.atk_id[n]
        atk_poke1 = class_attaque.Attaque(id)
        #attaque choisie par l'IA
        id = self.poke2.atk_id[int (random.randint (0, len (poke2.attaques)-1))]
        atk_poke2 = class_attaque.Attaque(id)
        self.dammage(atk_poke1, atk_poke2)
        
            
    def dammage(self,atk_poke1, atk_poke2):
        self.speed()
        #print (self.first.nom)
        # en fonction de qui attaque en premier, appele la methode loose_pv de la class pkm avec la methode calcul_damage et verifie si le combat est fini
        if self.first == self.poke1:
            self.poke2.loose_pv(self.calcul_damage(atk_poke1,self.poke1,self.poke2))
            #print (self.calcul_damage(atk_poke1,self.poke1, self.poke2),"pv inflige, pv restant :",self.poke2.pv)
            self.fin_combat ()
            if self.testx:
                self.poke1.loose_pv(self.calcul_damage(atk_poke2,self.poke2,self.poke1))
                #print (self.calcul_damage(atk_poke2,self.poke2,self.poke1),"pv inflige, pv restant :",self.poke1.pv)
                self.fin_combat ()
        elif self.first == self.poke2:
            self.poke1.loose_pv(self.calcul_damage(atk_poke2,self.poke2,self.poke1))
            #print (self.calcul_damage(atk_poke2,self.poke2, self.poke1),"pv inflige, pv restant :",self.poke1.pv)
            self.fin_combat ()
            if self.testx:
                self.poke2.loose_pv(self.calcul_damage(atk_poke1,self.poke1,self.poke2))
                #print (self.calcul_damage(atk_poke1,self.poke1,self.poke2),"pv inflige, pv restant :",self.poke2.pv)
                self.fin_combat ()

    #calcule des degat et aplication pour le combat graphic
    def damage_graph (self, pkm_off, pkm_def) :

        return 
            
    def combat_dress(self, dress1, dress2):
        nb_ko1 = 0
        nb_ko2 = 0
        #regarde le nombre de poke KO de chaque equipe et return False si tous KO
        for poke in range(len(dress1.equipe)):
            if dress1.equipe[poke].pv <= 0:
                nb_ko1 += 1
                if nb_ko1 == len(dress1):
                    return False
        for poke2 in range(len(dress2.equipe)):
            if dress2.equipe[poke2].pv <= 0:
                nb_ko2 += 1
                if nb_ko2 == len(dress1):
                    return False

    def switch(self,n, dress1):
        self.poke1 = dress1.equipe[n]



'''if __name__ == "__main__":
    #test des methodes
    with open("pokedex.json", "r") as f:
        pokedex = json.load(f)
    pokemon_29 = pokedex.get("42")
    pokemon_10 = pokedex.get("15")
    test = class_pkm.pkm_dress(pokemon_29, 39)
    test2 = class_pkm.pkm(pokemon_10,100)
    print(f"Nom du Pokémon : {test.nom}")
    print(f"Type du Pokémon : {test.type}")
    print(f"pv : {test.pv}")
    print(f"lv : {test.lv}")
    print(f"Nom du Pokémon : {test2.nom}")
    print(f"Type du Pokémon : {test2.type}")
    print(f"pv : {test2.pv}")
    fight = combat()
    #fight.en_combat(test, test2)
    red = class_dress_enemy.dress_enemy("Red")
    red.ajout_team()
    ethan = class_dress_enemy.dress_enemy("Ethan")
    ethan.ajout_team()
    fight.combat_dress(red, ethan)'''