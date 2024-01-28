import class_pkm
import json
import random

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
        #self.afficher_team()


    def random_team(self, taille):
        team = []
        while len(team) < taille:
            with open('pokedex.json', 'r') as f:
                data = json.load(f)

                last_key = list(data.keys())[-1]
            id_pokemon = random.randint(1, int (last_key))
            id_pokemon = str(id_pokemon)
            with open("pokedex.json", "r") as f:
                pokedex = json.load(f)
            new_poke = class_pkm.pkm(pokedex.get(id_pokemon),50)
            team.append(new_poke)
        self.equipe = team
        #self.afficher_team()

    def ajout_team_game(self, id):
        with open("pokedex.json", "r") as f:
            pokedex = json.load(f)
        new_poke = class_pkm.pkm_adv(pokedex.get(id),50)
        self.equipe.append(new_poke)
        #self.afficher_team()