
class Attaque :

    def __init__ (self, id) :
        from json import load
        self.__id = id
        with open ("attaque_list.json", "r", encoding='utf-8') as f:
            dictionaire = load (f)
        self.attaque = dictionaire [id]
        self.nom = self.attaque ["nom"]
        self.type = self.attaque ["type"]
        self.discription = self.attaque ["discription"]
        self.puissance = self.attaque ["puissance"]
        self.precision = self.attaque ["precision"]
        self.pp = self.attaque ["pp"]
        self.classe = self.attaque ["classe"]

    def get_id(self):
        return self.__id

    def get_nom(self):
        return self.nom

    def get_type(self):
        return self.type

    def get_discription(self):
        return self.discription

    def get_puissance(self):
        return self.puissance

    def get_precision(self):
        return self.precision

    def get_pp(self):
        return self.pp

    def get_classe(self):
        return self.classe
    
