import math
import random
from salle_cinema import SalleCinema


class SalleDeLuxe(SalleCinema):
    def __init__(self):
        super().__init__()
        self.__nbLoges_a_vendre = random.randint(1, 4)
        self.__prixLoge = 300   # valeur fixe
        self.__capacite = 20    # valeur fixe

    # -- Méthodes spécifiques aux loges --

    def calculerNbLogesRequises(self, nbPersonnes: int) -> int:
        """Calcule le nombre de loges nécessaires (arrondi au supérieur)."""
        return math.ceil(nbPersonnes / self.__capacite)

    def calculerVentesLoges(self, nbPersonnes: int) -> float:
        """
        Vend des loges pour un groupe et retourne le montant de la transaction.
        Lève RuntimeError si pas assez de loges disponibles.
        """
        nbLogesRequises = self.calculerNbLogesRequises(nbPersonnes)

        if nbLogesRequises > self.__nbLoges_a_vendre:
            raise RuntimeError("Le nombre de loges disponibles n'est pas suffisant")

        self.__nbLoges_a_vendre -= nbLogesRequises

        if self.__nbLoges_a_vendre == 0:
            print("Complet ! Plus de loges disponibles")

        return nbLogesRequises * self.__prixLoge

    # -- Affichage --

    def afficher(self):
        super().afficher()
        print(f"[Loges disponibles : {self.__nbLoges_a_vendre} \u2013 Capacité par loge : {self.__capacite}]")
