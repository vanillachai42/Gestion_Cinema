class Film:

    def __init__(self, titre: str, categorie: str, duree: int):
        self.__titre = titre
        self.__categorie = categorie
        self.__duree = duree
        self.__prix = 13 

    # -- Getters --

    def getTitre(self) -> str:
        return self.__titre

    def getPrix(self) -> float:
        return self.__prix

    # -- Affichage --

    def __str__(self) -> str:
        return f"{self.__titre} [{self.__categorie}] \u2013 durée : {self.__duree}mn"
