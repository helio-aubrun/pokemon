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