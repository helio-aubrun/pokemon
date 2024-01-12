class Joueur :
    def __init__ (self) :
        from json import load
        with open ("list_pkm_joueur.json", "r", encoding='utf-8') as file:
            self.__list_pkm = load(file)
        
    def get_list_pkm (self, id) :
        return self.__list_pkm [str (id)]
    

    def capture (self, id) :
        import json
        last_key = list(self.__list_pkm.keys())[-1]
        #test de limit du sac dujoueur
        if last_key < 6 :
            #ajout du pokemon dans le sac si la limiot n'est pas ateinte
            with open ("list_pkm_joueur.json", "w", encoding='utf-8') as list_pkm_joueur, open ("pokedex.json", "r") as pokedex :
                list_pokedex = json.load (pokedex)
                self.__list_pkm [str (last_key + 1)] = list_pokedex [str (id)]
        else :
            #ajout du pokemon dans le pc 
            try : 
                #ajout du pokemon a la fin du pc
                with open ("pc_joueur.json", "r") as pc :
                    list_pc = json.load (pc)
                    last_key_pc = list(list_pc.keys())[-1]
                with open ("pc_joueur.json", "w") as pc, open ("pokedex.json", "r") as pokedex :
                    list_pokedex = json.load (pokedex)
                    list_pc [str (int (last_key_pc) + 1)] = list_pokedex [str (id)]
                    json.dump (list_pc, pc)
            #creation du fichier pc_joueur.json et ajout du pokemon a la premier place
            except :
                print ("creation du nouveau pokemon dans le pc")
                with open ("pc_joueur.json", "w") as pc, open ("pokedex.json", "r") as pokedex :
                    list_pokedex = json.load (pokedex)
                    nouveau_pc = {"1" : list_pokedex [str (id)]}
                    json.dump (nouveau_pc, pc)






    
test = Joueur ()
print (test.get_list_pkm (2))