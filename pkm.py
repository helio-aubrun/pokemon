class pkm():

    def __init__(self, id, lv=1):
        self.nom = id.get("nom")
        self.type = id.get("Type")
        self.talent = id.get("talent")
        self.pv = id.get("pv")
        self.atk = id.get("atk")
        self.defense = id.get("def")
        self.atk_spe = id.get("atk_spe")
        self.def_spe = id.get("def_spe")
        self.spe = id.get("spe")
        self.exp = id.get("exp")
        self.lv = lv
        self.atk_possible = []
        self.atk_apprise = []
        self.evo = id.get("evo")

class pkm_dress(pkm):

    def __init__(self, id, lv=1):
        pkm.__init__(self, id, lv=1)
        self.barre_exp = 0
    
    def gain_exp(self):
        exp_gagné = (adv.exp * adv.lv) // (7 * joueur.nb_pk)
        self.barre_exp+=exp_gagné
        while self.barre_exp <= self.lv*100 and self.lv >100:
            self.barre_exp-=(self.lv*100)
            self.lv+=1
        if self.lv >= self.evo:
            

class pkm_adv(pkm):

    def __init__(self, id, attaques, lv=1):
        pkm.__init__(self, id, lv=1)