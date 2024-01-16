import class_pkm
import json

class dress_enemy():

    def __init__(self, nom):
        self.nom = nom
        self.equipe = []

    def afficher_team(self):
        print (f"Equipe de {self.nom}")
        for poke in self.equipe:
            print (poke.nom)

    def ajout_team(self):
        while not input("Ajouter o/n : ") == "n":
            id = input("id : ")
            lv = int(input("lv : ")) 
            with open("pokedex.json", "r") as f:
                pokedex = json.load(f)
            new_poke = class_pkm.pkm_adv(pokedex.get(id),lv)
            self.equipe.append(new_poke)
        self.afficher_team()